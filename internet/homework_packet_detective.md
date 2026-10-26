# Packet Detective #

In class, we have discussed how computers communicate by breaking information into packets and sending those packets across a network. A computer may communicate with several different systems while completing what seems like one simple task. For instance, in a typical web browsing session, a client must contact a DNS server to get the IP address of a website and then, once it has the website address, connect to the website directly.

In this activity, you will examine a collection of network packets captured while two users were visiting the same website. The packets have been randomly arranged and are not shown in the order in which they were sent or received.

Your job is to determine what happened.

## The Network ##

Four computers appear in the packet log:

* Two client computers (`Client 1` and `Client 2`)
* One DNS server
* Two web servers

The computers use the following IP addresses:

* `10.0.0.21`
* `10.0.0.34`
* `10.0.0.53`
* `199.34.228.159`
* `104.26.7.166`

You are not told which IP address belongs to which computer. You will need to determine that from the packets.

## Packet Log ##

| Packet | Source IP | Destination IP | Protocol | Information |
| ------ | -------------- | -------------- | -------- | ------------------------------------------------------------------------- |
| A | `199.34.228.159` | `10.0.0.21` | HTTP | `Activities begin at 9:00 AM.</body></html>` |
| B | `10.0.0.34` | `104.26.7.166` | HTTP | `GET /announcements.html` |
| C | `10.0.0.53` | `10.0.0.21` | DNS | `www.sequoiabrigadecamp.org = 199.34.228.159` |
| D | `104.26.7.166` | `10.0.0.34` | HTTP | `<html><body>Today's announcement: The ` |
| E | `10.0.0.21` | `10.0.0.53` | DNS | `What is the IP address of www.sequoiabrigadecamp.org?` |
| F | `199.34.228.159` | `10.0.0.21` | HTTP | `<html><body>Welcome to Sequoia Brigade Camp. The ` |
| G | `10.0.0.34` | `10.0.0.53` | DNS | `What is the IP address of www.cui.edu?` |
| H | `104.26.7.166` | `10.0.0.34` | HTTP | `library will close at 8:00 PM.</body></html>` |
| I | `10.0.0.21` | `199.34.228.159` | HTTP | `GET /index.html` |
| J | `10.0.0.53` | `10.0.0.34` | DNS | `www.cui.edu = 104.26.7.166` |
| K | `199.34.228.159` | `10.0.0.21` | HTTP | `weather is sunny today. Campfire begins at 8:00 pm. ` |

## Part 1: Identify the Computers ##

Determine the role of each IP address. For each computer, briefly explain what evidence in the packet log helped you identify its role.

| IP Address | Computer Role | Evidence |
| -------------- | ------------- | -------- |
| `10.0.0.21` | `________________` | `_______________________________________` |
| `10.0.0.34` | `________________` | `_______________________________________` |
| `10.0.0.53` | `________________` | `_______________________________________` |
| `104.26.7.166` | `________________` | `_______________________________________` |
| `199.34.228.159` | `________________` | `_______________________________________` |

## Part 2: Reconstruct the Conversations ##

The packets from both clients have been mixed together. Separate the packets into the two conversations.

### Client 1 ###

List the packet letters in the order in which the communication must have occurred:

`________________________________________`

### Client 2 ###

List the packet letters in the order in which the communication must have occurred:

`________________________________________`

Remember that the packet log itself is out of order. Use the source and destination addresses, protocols, requests, responses, and message contents to determine the correct sequence.

## Part 3: Reconstruct the Web Pages ##

Each web server response was divided into multiple packets. Put the pieces back together and write the complete web content received by each client.

### Client 1 Web Content ###

`________________________________________________________________`

`________________________________________________________________`

`________________________________________________________________`

### Client 2 Web Content ###

`________________________________________________________________`

`________________________________________________________________`

`________________________________________________________________`

## Part 4: Explain What Happened ##

Answer the following questions briefly.

1. Why does each client contact the DNS server before contacting the web server?

2. What information does the DNS server provide to the client?

3. How can you tell which computer is the web server?

4. How can you tell which packets belong to Client 1 and which belong to Client 2?

5. The packets in the log are out of order. How were you able to determine the correct order of the web content?

6. Why might a real network need a more reliable way to determine packet order than simply reading the contents?

## What You Will Submit ##

Submit your completed answers, including:

- The role of each IP address and your evidence
- The reconstructed packet order for both clients
- The reconstructed web content for both clients
- Your answers to the six explanation questions

You do not need to know any networking concepts beyond what we have discussed in class. Work from the evidence contained in the packet log and explain your reasoning clearly.
