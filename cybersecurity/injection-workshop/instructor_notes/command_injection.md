# Command Injection Workshop — Instructor Notes

## Audience and Goal

This activity is designed for small business owners who are comfortable with business operations but may know very little about computer security.

The goal is not to teach shell scripting. The goal is to help participants discover that a web application can accidentally treat **user-supplied data as operating-system instructions**.

The activity uses four stages:

1. **DISCOVER** — realize that the web application is constructing and running an operating-system command.
2. **READ** — make the server reveal information the user was not supposed to see.
3. **DISRUPT** — interfere with a normal business process.
4. **MODIFY** — alter a business-facing output in a way that demonstrates a realistic operational consequence.

The suggested order is:

**DISCOVER → READ → DISRUPT → MODIFY**

This gives participants a gradual increase in impact while preserving the core lesson:

> **The application was supposed to treat what we typed as data, but instead it allowed our data to become part of an operating-system command.**

---

# Core Teaching Idea

Throughout the activity, keep returning to the same question used in the SQL exercise:

> **What did the computer think you meant?**

The participant believes they are entering a vendor name, filename, address, or other ordinary business value.

The vulnerable application combines that input with a shell command.

A useful summary is:

> **Command injection happens when user input is mixed directly into a command that the operating system executes.**

This is closely related to SQL injection, but the interpreter is different.

With SQL injection, the database interprets the injected instructions.

With command injection, the operating system shell interprets them.

---

# Recommended Activity Structure

Each scenario should use several levels of discovery.

## Level 1 — Normal Use

Participants use the feature exactly as intended.

## Level 2 — Strange Input

Participants try unusual punctuation and observe unexpected behavior.

## Level 3 — Reveal the Command

Show the exact command the server constructed.

## Level 4 — Guided Challenge

Give participants a goal and partial hints rather than immediately giving the full input.

## Level 5 — Business Consequence

Translate the technical result into something a business owner can immediately understand.

## Level 6 — Fix and Retest

Switch to the secure implementation and have participants try the same input again.

---

# Scenario 1 — DISCOVER

## Business Story

The participant is using a small-business vendor lookup page.

The page might say:

```text
Vendor Lookup

Vendor name:
[ Acme                         ]

[ Search ]
```

The user believes the application is searching a vendor database.

Behind the scenes, however, this legacy feature searches a text file using an operating-system command:

```bash
grep -i "Acme" /app/data/vendors.txt
```

This is intentionally implemented poorly for the workshop.

---

## Learning Objective

Participants discover that the web interface is not merely "searching data."

It is constructing a command and asking the operating system to execute it.

This is the conceptual bridge into command injection.

---

## Level 1 — Normal Search

Have participants search for ordinary values:

```text
Acme
Dental
Supply
```

The application returns matching vendor records.

Ask:

- What does the application appear to be doing?
- Where do you think the data is stored?
- Does the participant have any reason yet to believe an operating-system command is involved?

The answer should be no.

---

## Level 2 — Strange Input

Give participants a small set of inputs to try:

```text
Acme
Acme;
Acme; whoami
```

The key input is:

```text
Acme; whoami
```

In the intentionally vulnerable version, the shell interprets the semicolon as the end of one command and the start of another.

A vulnerable command could become:

```bash
grep -i Acme /app/data/vendors.txt; whoami
```

The output may include both the vendor result and the name of the operating-system account running the web application.

---

## Level 3 — Reveal the Command

Show the server-side command.

Normal input:

```text
Acme
```

produces:

```bash
grep -i Acme /app/data/vendors.txt
```

Injected input:

```text
Acme; whoami
```

produces:

```bash
grep -i Acme /app/data/vendors.txt; whoami
```

Ask:

> Which characters came from the programmer, and which came from you?

Then ask:

> What did the semicolon mean to the shell?

Explain that the shell treats it as a separator between commands.

The user thought they supplied one search value.

The shell thought it received two commands.

---

## Level 4 — Simple Discovery Challenges

Keep these very basic.

### Challenge A — Who Is Running the Application?

Try:

```text
Acme; whoami
```

Ask:

> Why might an attacker care which account is running the server?

The goal is not to go deeply into privilege escalation.

The business-level answer is simply:

> The account determines what the application is allowed to read or change.

---

### Challenge B — Where Is the Application Running?

Try:

```text
Acme; pwd
```

This reveals the application's current working directory.

Ask:

> Why might learning the server's directory structure help an attacker understand the application?

---

### Challenge C — What Files Are Nearby?

In the isolated workshop container, an instructor may allow:

```text
Acme; ls
```

or a similarly constrained command.

This demonstrates that the injected command is interacting with the server itself, not merely with the vendor-search feature.

---

# Scenario 2 — READ

## Business Story

The vendor-search feature is still the entry point.

The server also contains a harmless workshop-only file representing internal business notes.

For example:

```text
/app/data/internal_notes.txt
```

The file might contain fictional information such as:

```text
Internal Purchasing Notes

Preferred freight vendor: Northstar Logistics
Warehouse alarm inspection: October 15
Accounting contact: Dana Reed
Backup shipment process: Call warehouse manager directly
```

Nothing should be real or sensitive.

---

## Learning Objective

Participants discover that command injection can allow a web application to expose files it was never designed to show.

The business consequence is unauthorized disclosure.

This maps naturally to **confidentiality**.

---

## Level 1 — Introduce the Goal

Ask:

> The vendor-search page is supposed to show only vendor records. Can you make it show a completely different file from the server?

Do not provide the full solution immediately.

---

## Level 2 — Hint

Remind them that they already discovered:

```text
;
```

can separate commands.

Then give them a simple shell concept:

```bash
cat filename
```

Explain that `cat` displays the contents of a text file.

---

## Level 3 — Guided Challenge

In the isolated workshop environment, a participant might try:

```text
Acme; cat /app/data/internal_notes.txt
```

The vulnerable command becomes:

```bash
grep -i Acme /app/data/vendors.txt; cat /app/data/internal_notes.txt
```

The page now displays the vendor search output followed by the internal notes.

---

## Instructor Questions

Ask:

> Did the application contain a button labeled "Show Internal Notes"?

No.

Ask:

> Did the participant bypass a login page for the notes?

Not necessarily.

The problem is that the vendor-search feature accidentally gave them a way to ask the operating system to read another file.

---

## Optional READ Challenges

You can provide a small list of safe workshop files and ask participants to identify which ones the application account can read.

For example:

```text
/app/data/vendors.txt
/app/data/internal_notes.txt
/app/data/shipping_schedule.txt
```

Do not include real operating-system secrets, credentials, SSH keys, browser profiles, or host-mounted files.

The goal is conceptual discovery, not system enumeration.

---

## Business Debrief

Ask:

> If a web application on your own system could read files beyond the page you intended, what kinds of information might be exposed?

Possible answers:

- exported customer data;
- internal reports;
- invoices;
- configuration files;
- employee schedules;
- backup files;
- application logs.

Keep the discussion focused on business impact.

---

# Scenario 3 — DISRUPT

## Business Story

The application now includes a fictional **Shipping Queue**.

Employees rely on a text file or generated queue to decide what packages need to be processed.

For example:

```text
Today's Shipping Queue

Order 1042 — Acme Office Supply
Order 1057 — Mountain View Dental
Order 1061 — Pacific Design Group
Order 1074 — Harbor Coffee
```

The queue is disposable workshop data.

---

## Learning Objective

Participants discover that command injection can interfere with business operations even if no customer database is stolen.

This maps naturally to **availability** and operational disruption.

---

## Level 1 — Show the Normal Business Process

Explain:

> The warehouse staff rely on this queue to know what to process.

Show the queue before the exercise.

For example:

```text
4 shipments waiting
$3,842 scheduled to ship
```

---

## Level 2 — Introduce a Harmless Maintenance Feature

The business portal might contain a feature such as:

```text
Find shipment by customer:
[ Acme ]

[ Search ]
```

Behind the scenes, the application uses a shell command to search the shipping queue.

The vulnerable pattern might resemble:

```python
command = f"grep -i {search} /app/data/shipping_queue.txt"
subprocess.run(command, shell=True, ...)
```

---

## Level 3 — Controlled Disruption Challenge

The workshop container can include a harmless helper script such as:

```text
/app/workshop/clear_shipping_queue.sh
```

That script affects only the disposable demonstration file.

A participant who understands command separation can be challenged:

> Can you make the vendor-search function run the workshop's queue-clearing command?

A guided input could be:

```text
Acme; /app/workshop/clear_shipping_queue.sh
```

This causes the disposable queue to be emptied or marked inactive.

The important point is not the particular shell syntax.

The point is that a search box caused an unrelated business process to change.

---

## Level 4 — Show the Business Effect

Before:

```text
SHIPPING QUEUE

4 shipments waiting
$3,842 scheduled to ship
```

After:

```text
SHIPPING QUEUE

0 shipments waiting
$0 scheduled to ship
```

Ask:

> What happens if employees trust this screen tomorrow morning?

Possible answers:

- shipments are missed;
- customers call;
- staff waste time troubleshooting;
- revenue is delayed;
- orders must be reconstructed.

---

## Alternative DISRUPT Scenarios

If a shipping queue does not fit the audience, use:

- appointment queue;
- invoice-processing queue;
- print queue;
- report-generation queue;
- support-ticket queue;
- scheduled delivery list.

The ideal scenario is something the audience recognizes as a real operational dependency.

---

## Business Debrief

Emphasize:

> The attacker did not have to "take down the server."

The web application can remain online while the business process it supports becomes unreliable.

This is often easier for small-business owners to relate to than a generic denial-of-service example.

---

# Scenario 4 — MODIFY

## Why This Scenario Comes Last

This should be the climax of the command-injection section.

DISCOVER proves that operating-system commands can be injected.

READ shows unauthorized access to information.

DISRUPT shows operational impact.

MODIFY demonstrates that the attacker may be able to change a business output that employees or customers trust.

---

## Business Story

Use a **shipping-label generation** workflow.

The business portal allows an employee to preview a pending shipment.

For example:

```text
ORDER #1057

Customer:
Mountain View Dental

Ship To:
1820 Main Street
Irvine, CA 92614

[ Generate Shipping Label ]
```

Behind the scenes, the application uses a small command-line helper to generate a label file.

For example:

```bash
/app/bin/make-label 1057
```

The generated label might be stored in:

```text
/app/data/labels/1057.txt
```

The workshop should use plain text rather than a real shipping system.

---

## Learning Objective

Participants discover that command injection can alter a downstream business artifact that people trust.

The consequence is not merely "the server ran another command."

The consequence is:

> The wrong package may be sent to the wrong place.

This maps naturally to **integrity**.

---

## Level 1 — Generate a Normal Label

Have participants generate the label normally.

Show:

```text
SHIP TO:

Mountain View Dental
1820 Main Street
Irvine, CA 92614
```

Explain that warehouse employees trust this output.

---

## Level 2 — Reveal the Command

Show the command the web application runs.

For example:

```bash
/app/bin/make-label 1057
```

Then show the vulnerable code pattern:

```python
command = f"/app/bin/make-label {order_id}"
subprocess.run(command, shell=True, ...)
```

Ask:

> What happens if the value inserted after `make-label` contains a command separator?

---

## Level 3 — Controlled Modification

For the workshop, include a harmless helper script designed specifically for the exercise:

```text
/app/workshop/redirect_label.sh
```

It should only modify a disposable label file inside the container.

For example, it might replace the shipping address with:

```text
500 Attacker Avenue
Testville, CA 90000
```

A guided input could be structured so that the participant causes the legitimate label command and then the workshop helper to run.

For example:

```text
1057; /app/workshop/redirect_label.sh 1057
```

The resulting label would now contain the fake address.

---

## Level 4 — Show the Business Effect

Display the label again.

Before:

```text
Mountain View Dental
1820 Main Street
Irvine, CA 92614
```

After:

```text
Mountain View Dental
500 Attacker Avenue
Testville, CA 90000
```

Ask:

> What happens if the warehouse employee trusts the label?

Then ask:

> Which system is actually "wrong" here?

The order database may still contain the correct address.

The problem is that the generated business artifact was altered after the application created it.

This helps participants understand that integrity failures can occur at many points in a workflow.

---

## Alternative MODIFY Scenarios

Other contained examples include:

- changing the destination on a generated delivery instruction;
- modifying a printable invoice;
- altering a generated customer notification;
- changing a local report used by employees;
- modifying a work-order printout;
- changing a generated pickup sheet.

Avoid teaching persistence, operating-system account takeover, credential replacement, startup-script modification, or other techniques that go beyond the business-learning objective.

---

# Secure Version

The central technical fix is to avoid passing user-controlled input through a shell whenever possible.

Vulnerable:

```python
command = f"grep -i {search} /app/data/vendors.txt"

result = subprocess.run(
    command,
    shell=True,
    capture_output=True,
    text=True
)
```

Secure:

```python
result = subprocess.run(
    ["grep", "-i", search, "/app/data/vendors.txt"],
    shell=False,
    capture_output=True,
    text=True
)
```

Now retry:

```text
Acme; whoami
```

The operating system should treat:

```text
Acme; whoami
```

as one literal search value.

It should not run `whoami`.

---

# Key Demonstration of the Fix

This is the command-injection equivalent of parameterized SQL.

In the vulnerable version:

```text
Acme; whoami
```

is interpreted approximately as:

```text
SEARCH FOR ACME
THEN
RUN WHOAMI
```

In the secure version, it means:

```text
SEARCH FOR THE LITERAL TEXT:

Acme; whoami
```

A useful phrasing for the audience is:

> **The semicolon did not become harmless because we removed it. It became harmless because we stopped asking a shell to interpret the user's input as part of a command.**

---

# SQL Injection vs. Command Injection

After both exercises, compare them directly.

| Vulnerability | Interpreter | Intended Input | Injected Effect |
|---|---|---|---|
| SQL Injection | Database | Search value or form field | Input becomes part of a SQL statement |
| Command Injection | Operating-system shell | Search value, filename, ID, etc. | Input becomes part of a shell command |

The shared lesson is:

> **Keep user-controlled data separate from executable instructions.**

---

# Suggested Overall Command-Injection Progression

```text
DISCOVER
Can I make the server run another harmless command?

        ↓

READ
Can I make the server show a file the web page was never meant to expose?

        ↓

DISRUPT
Can I interfere with a normal business workflow?

        ↓

MODIFY
Can I change a trusted business output?
```

This sequence roughly maps to:

| Scenario | Security Property | Business Meaning |
|---|---|---|
| READ | Confidentiality | Someone sees information they should not see |
| DISRUPT | Availability | A normal business process stops working |
| MODIFY | Integrity | Trusted information or output is changed |

---

# Suggested Instructor Pacing

## Before Any Injection

Let participants use the feature normally.

Avoid beginning with shell syntax.

Ask:

> What do you think the application does when you click Search?

Most participants will assume something like:

> It searches the data.

That assumption makes the later reveal more effective.

---

## During Discovery

Give small hints.

For example:

> In many command shells, a semicolon separates two commands.

Then ask:

> If the application places your text directly inside a command, what might happen?

Let them test the idea.

---

## When Showing the Command

Visually separate programmer-controlled text and participant-controlled text.

For example:

```text
PROGRAMMER:

grep -i

PARTICIPANT:

Acme; whoami

PROGRAMMER:

/app/data/vendors.txt
```

Then show how the shell interprets the combined result.

---

# Suggested Instructor Questions

After DISCOVER:

> Why does it matter that the website is able to run operating-system commands?

After READ:

> What files on a business server would you never expect a customer-facing search form to display?

After DISRUPT:

> Which business processes depend on small files, scripts, queues, or generated reports that employees simply assume are correct?

After MODIFY:

> If a warehouse worker trusts a generated label, what happens when the system producing that label can be manipulated?

Finally:

> Which is the real problem: the semicolon, or the fact that user data was sent through a command interpreter?

The desired answer is the latter.

---

# Reset and Safety

This lab should operate only against disposable workshop data.

Recommended controls:

- Run the vulnerable application inside a disposable container.
- Run the container as a non-root user.
- Mount no host directories into the vulnerable container.
- Do not expose the Docker socket.
- Do not run the container in privileged mode.
- Store no real credentials, SSH keys, API keys, or customer data inside it.
- Use only workshop-created helper scripts for DISRUPT and MODIFY scenarios.
- Give the application access only to files needed for the demonstrations.
- Provide a **Restore Workshop Environment** button.
- Rebuild or reset the container between workshop groups if needed.
- Keep the vulnerable application isolated from production systems.

The modification and disruption exercises should act only on disposable files inside the workshop environment.

---

# Final Takeaway

End the command-injection section with:

> **The application was supposed to treat what we typed as data. Instead, it allowed our data to become part of an operating-system command.**

Then compare the vulnerable and secure versions:

```text
BAD:
"Build a command string and ask a shell to interpret it."

BETTER:
"Run a specific program and pass the user's value as a separate argument."
```

Participants do not need to leave knowing shell syntax.

They should leave understanding that any application feature that mixes user input directly into an operating-system command can accidentally give that user influence far beyond the feature they were supposed to use.
