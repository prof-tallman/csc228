# Small Business Cybersecurity Injection Lab

A deliberately vulnerable Flask application for a **supervised, isolated cybersecurity workshop** for small-business owners. The site presents one coherent fictional company portal and supports progressive SQL-injection and command-injection activities.

## Activities

### SQL injection

1. **READ — Customer Search**
   - Normal input: `Acme`
   - Discovery input: `'`
   - Guided payload: `' OR 1=1 --`
   - Demonstrates unauthorized disclosure / confidentiality.

2. **DELETE / DISRUPT — Order Cancellation**
   - Logged in as Acme Office Supply, customer 1.
   - Normal order: `1042`
   - Guided payload: `1042 OR 1=1 --`
   - Demonstrates how an authorization condition can be bypassed and multiple pending orders removed.
   - Use **Restore Lab** after this scenario.

3. **MODIFY / ACCOUNT TAKEOVER — Profile Update**
   - Logged in as Acme Office Supply, customer 1.
   - Target: Mountain View Dental, customer 3.
   - Select **Email** and try a normal value first.
   - Guided workshop payload:

     ```text
     takeover@evil.example' WHERE id = 3 --
     ```

   - Then use the simulated **Forgot Password** control to see where Mountain View Dental's reset would be sent.
   - The same technique can be explored with the POC or street-address field.

### Command injection

1. **DISCOVER — Vendor Lookup**
   - Normal input: `Acme`
   - Guided payload: `Acme; whoami`
   - Other harmless discovery commands: `Acme; pwd` and `Acme; ls`

2. **READ — Internal Notes**
   - Guided workshop payload:

     ```text
     Acme; cat /app/data/internal_notes.txt
     ```

   - Demonstrates that a vendor-search form can expose an unrelated file.

3. **DISRUPT — Shipping Queue**
   - Normal input: `Acme`
   - Workshop-only helper:

     ```text
     /app/workshop/clear_shipping_queue.sh
     ```

   - Guided payload:

     ```text
     Acme; /app/workshop/clear_shipping_queue.sh
     ```

   - The helper only clears the disposable workshop queue inside the container.

4. **MODIFY — Shipping Label**
   - Normal filename: `1057.txt`
   - Workshop-only helper:

     ```text
     /app/workshop/redirect_label.sh 1057
     ```

   - Guided payload:

     ```text
     1057.txt; /app/workshop/redirect_label.sh 1057 #
     ```

   - The generated label changes from the legitimate Mountain View Dental address to the clearly fake `500 Attacker Avenue` workshop address.

Each activity can be switched between **Vulnerable** and **Fixed** mode so participants can retry exactly the same input after the secure implementation is enabled.

## Quick start

From this folder:

```bash
docker build -t cyber-workshop .
docker run --rm -p 8080:8080 cyber-workshop
```

Open locally:

```text
http://localhost:8080
```

For participants on the same workshop network, replace `localhost` with the instructor computer's LAN IP address:

```text
http://192.168.1.25:8080
```

Instructor/debug view:

```text
http://192.168.1.25:8080/?instructor=1
```

If desired, expose ordinary HTTP port 80 on the host:

```bash
docker run --rm -p 80:8080 cyber-workshop
```

Participants can then browse to:

```text
http://192.168.1.25
```

## Restore Lab

The **Restore Lab** button reseeds:

- the SQLite database;
- all customer profiles;
- all orders;
- the vendor file;
- the internal-notes file;
- the shipping queue;
- generated shipping labels.

Use it between groups or after destructive scenarios.

The same reset can be performed by restarting the disposable container.

## Instructor notes

Detailed notes are included under:

```text
instructor_notes/sql_injection.md
instructor_notes/command_injection.md
```

## Secure implementation concepts

### SQL

The vulnerable routes concatenate user input directly into SQL. Fixed mode uses parameterized queries:

```python
cursor.execute(
    "SELECT id, company FROM customers WHERE company LIKE ?",
    (f"%{term}%",)
)
```

The important lesson is not that suspicious punctuation is filtered. It is that the database receives **SQL instructions and data separately**.

### Operating-system commands

The vulnerable routes build strings and execute them using `shell=True`:

```python
subprocess.run(command, shell=True, ...)
```

Fixed mode either avoids executing a command entirely or invokes the intended program with a list of arguments and `shell=False`:

```python
subprocess.run(["grep", "-i", "--", term, filename], shell=False, ...)
```

The shell never gets an opportunity to reinterpret punctuation in the user's value as another instruction.

## Containment

This application is intentionally unsafe. Keep it isolated.

The provided container:

- runs Flask as an unprivileged `workshop` user;
- contains only fake workshop data;
- requires no credentials or API keys;
- mounts no host directories by default;
- does not expose the Docker socket;
- does not use privileged mode;
- provides workshop-only scripts whose effects are limited to disposable files in `/app/data`.

Do **not** add production data, secrets, host-directory mounts, SSH keys, cloud credentials, or the Docker socket to this container.

For an in-person workshop, a dedicated guest/workshop Wi-Fi or VLAN with restricted Internet access is a good additional containment measure.

## Project structure

```text
app.py
lab_state.py
init_db.py
requirements.txt
Dockerfile
.dockerignore

data/
  business.db
  vendors.txt
  internal_notes.txt
  shipping_queue.txt
  labels/

workshop/
  clear_shipping_queue.sh
  redirect_label.sh

templates/
  index.html

static/
  style.css

instructor_notes/
  sql_injection.md
  command_injection.md
```
