# Running the Cybersecurity Workshop on macOS

## 1. Install Docker Desktop

Install **Docker Desktop for Mac**.

Docker Desktop provides both:

- the Docker engine;
- the `docker` command-line tool.

After installation, launch Docker Desktop and leave it running while you use the workshop.

---

## 2. Verify Docker

Open Terminal and run:

```bash
docker --version
```

Then test that Docker can start a container:

```bash
docker run hello-world
```

If the `hello-world` container runs successfully, Docker is ready.

---

## 3. Unzip the Workshop Project

Unzip the downloaded workshop project.

Then open Terminal and change into the project directory.

For example:

```bash
cd ~/Downloads/cyber-workshop
```

Use the actual path where you extracted the project.

---

## 4. Build the Workshop Container

From inside the project directory, run:

```bash
docker build -t cyber-workshop .
```

This creates a Docker image named:

```text
cyber-workshop
```

The first build may take longer because Docker may need to download the base image and install the required Python packages.

---

## 5. Run the Workshop

Start the workshop container with:

```bash
docker run --rm -p 8080:8080 cyber-workshop
```

The options mean:

- `--rm` — remove the container automatically when it stops;
- `-p 8080:8080` — make the workshop webserver available on port 8080 of your Mac.

Leave this Terminal window open while the workshop is running.

---

## 6. Test It on Your Mac

Open a web browser and visit:

```text
http://localhost:8080
```

You should see the workshop business portal.

For the instructor/debug view, use:

```text
http://localhost:8080/?instructor=1
```

---

## 7. Find Your Mac's Local IP Address

Participants on the same Wi-Fi network will need your Mac's local network address rather than `localhost`.

On many Macs, this command will show the Wi-Fi IP address:

```bash
ipconfig getifaddr en0
```

For example, it might return:

```text
192.168.1.42
```

Participants would then browse to:

```text
http://192.168.1.42:8080
```

Your instructor view would be:

```text
http://192.168.1.42:8080/?instructor=1
```

If `ipconfig getifaddr en0` returns nothing, the active network interface may be different.

You can inspect network interfaces with:

```bash
ifconfig
```

---

## 8. Allow Incoming Connections if macOS Asks

macOS may ask whether Docker, Terminal, or a related process is allowed to accept incoming network connections.

For the workshop, allow incoming connections so that participants on the same Wi-Fi network can reach the webserver.

---

## 9. Test from a Second Device Before the Workshop

Before the actual session, connect another laptop or phone to the same Wi-Fi network and browse to:

```text
http://YOUR-MAC-IP:8080
```

This verifies that:

- the Docker container is running;
- your Mac firewall is not blocking the connection;
- the wireless network allows devices to communicate with one another.

Some guest Wi-Fi networks use **client isolation**, which prevents one attendee's device from connecting directly to another device on the same wireless network. If that happens, the workshop site may work on your Mac but not on participant devices.

Testing the actual workshop network ahead of time is strongly recommended.

---

## 10. Stopping the Workshop

In the Terminal window where Docker is running, press:

```text
Control-C
```

Because the container was started with `--rm`, Docker will remove the stopped container automatically.

The Docker image will remain available, so the next time you run the workshop you usually only need:

```bash
docker run --rm -p 8080:8080 cyber-workshop
```

You only need to run `docker build` again after changing the project files.

---

# Quick Reference

Build:

```bash
docker build -t cyber-workshop .
```

Run:

```bash
docker run --rm -p 8080:8080 cyber-workshop
```

Local browser:

```text
http://localhost:8080
```

Instructor view:

```text
http://localhost:8080/?instructor=1
```

Find Wi-Fi IP:

```bash
ipconfig getifaddr en0
```

Participant URL:

```text
http://YOUR-MAC-IP:8080
```

Stop the workshop:

```text
Control-C
```
