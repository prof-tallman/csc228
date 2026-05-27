# TCP Reliability Exercise #

The TCP Reliability Exercise is an activity that allows students to discover how reliable delivery is maintained when packets arrive out of order, are dropped in transit, or must be retransmitted. Students will observe how sequence numbers and acknowledgement numbers allow the client and server to reconstruct a complete response despite unreliable network delivery.

Each individual step in the exercise is relatively simple and straightforward. The difficulty is that students may pay such close attention to their individual roles that they lose sight of the larger learning objective. To guard against such losses, the remaining students should take notes, preparing a summary and explanation at the end.

As proposed, this exercise requires six student actors. Other students in the class should act as observers who take careful notes and, at the end, summarize the learning points for everyone. For particularly large classes, the students can be divided into smaller groups of actors and observers.  Or, the additional students can be added as new clients, servers, or routers (this approach will require the instructor to create new packet cards).

For this exercise, many of the details will be written on small notecards that are only available to the students acting as clients, routers, and servers. To allow the observers to follow what is happening, each notecard should be projected as slides or printed for all audience members.

#### Acknowledgements ####

After putting this exercise together, I discovered related activities at CS Unplugged's [Tablets of Stone—Network Communication Protocols](https://classic.csunplugged.org/documents/activities/network-protocols/unplugged-en-network_protocols-v3.1.pdf), which also models reliable communication over an unreliable delivery channel but it is more discovery based than observer based. The *Tablets of Stone* exercise seems like a better discovery-based activity with this *TCP Reliability Exercise* as a potential follow-on. Some other similar activities include:
* [AP Computer Science Principles](https://sites.google.com/ceismc.org/scc-apcomputerscienceprinciple/unit-2-computer-systems-and-networks/section-2-7-demonstrate-packet-switching)
* [CS Field Guide's Packet Attack Game](https://www.csfieldguide.org.nz/en/chapters/network-communication-protocols/transport-layer-protocols/)

Also, it should be noted that GenAI helped to polish up this exercise by identifying a few inconsistencies between the instructions and packet tables.

## Technical Simplifications ##

To simplify this exercise for a general audience, several technical details have been simplified:

1. In actual TCP communication, sequence and acknowledgement numbers track positions within a stream of bytes. For this exercise, each HTML response card will be treated as one numbered packet. When a client sends ACK=3, it means that the client has correctly received all response packets before packet #3 and is waiting for packet #3 next.

2. Although this activity targets the Transport Layer of the OSI and TCP/IP model, the instructions use the popular term *packet* in place of *segment* because the exercise is intended for a general audience where packet is more common. Remember, segments are the term at the Transport Layer, packets at the Network Layer, and frames at the Network Access/Data Link Layer.

3. Real TCP data segments contain several header fields and may use flags such as `ACK` or `PSH`. To keep this activity focused on reliability, data-carrying cards are labeled `DATA` rather than reproducing the full TCP header. A `DATA` card carries part of the request or webpage; an `ACK` card reports the next portion of the response that the client expects to receive.

4. In the fourth connection only, the server sends packet #2 and waits for its acknowledgement before sending packets #3 and #4. Real TCP may have multiple packets in transit at once, but this simplified pacing makes the effect of a lost acknowledgement visible during the activity.

5. This activity simplifies the network path and omits NAT. Treat the listed addresses as routable within our simulated network.

## Student Roles ##

### Students as Endpoints ###

Designate three students to be endpoints: two as clients and one as a web server. Each of the clients should be given a small number of GET requests on notecards. Their role will be to send the GET requests to the servers and then to receive HTML responses.

Likewise, the server students should be given their set of notecards that represent HTML responses. Each of the HTML responses should be split between a number of notecards, each representing an individual packet. Some of the server's notecards will need duplicate copies. When an original data packet is lost, the client's acknowledgements will continue to indicate the missing portion of the response, and the server will eventually send a replacement copy.

Note that the clients, in addition to their GET request notecards, will need notecards to represent TCP acknowledgements.

### Students as the Network ###

Three students will act as routers. These students must be given visible labels that distinguish them from each other. One easy way to do this is with colored cones or placards. If it is a small class and everyone knows each other's names, then simply using the names will work too. Each network student should be given instructions identifying which packet cards to deliver normally, delay, or drop.

## Instructions for Running the Activity ##

These four connections will expose students to several important situations:

| Connection | Summary | Client | Client Port | Request | What Happens |
| ---------- | ------- | ------ | ----------- | ------- | ------------ |
| A | Out-of-order delivery can be repaired by reassembly without retransmission | Alice | 51001 | GET /index.html | Packet #2 is delayed; packet #3 arrives first; packet #2 eventually arrives |
| B | Lost data packet requiring retransmission | Bob | 52001 | GET /schedule.html | Packet #2 is dropped; the server receives no progress beyond `ACK=2`; after waiting, it sends packet #2 again |
| C | Repeated ACK values visibly identify a missing gap among later-arriving data | Alice | 51002 | GET /photos.html | Packet #3 is dropped; packets #4 and #5 arrive; Alice repeatedly sends `ACK=3`; server sends packet #3 again | 
| D | Lost acknowledgements can cause unnecessary retransmission | Bob | 52002 | GET /faculty.html | Packet #2 arrives, but `ACK=3` is dropped; server eventually sends duplicate packet #2. |

### Round 1: Introduces Out-of-Order Delivery ###

Run the first connection (A) where Alice requests the homepage. Students should discover:

* The network may deliver packets out of order even when no data is permanently lost.
* The client’s acknowledgement identifies the next packet it still expects.
* Once the delayed packet arrives, the client can reconstruct the response without retransmission.

### Round 2: Introduces Packet Loss ###

Run the second connection (B) where Bob requests the course schedule. Students should discover:

* A missing packet prevents page assembly.
* ACK numbers indicate what the receiver still needs.
* The server can retransmit missing data.

### Round 3: Introduces Multiple Outstanding Packets ###

Run the third connection (C) where Alice requests the photo page. Students should discover:

* Later packets may arrive even when an earlier packet is missing.
* The client's repeated ACK value identifies the next missing part of the response.
* Sending the missing packet again allows the client to reconstruct the complete webpage.

### Round 4: Introduces Lost Acknowledgements ###

Run the fourth connection (D) where Bob requests the faculty page. Students should discover:

* Not every retransmission results from lost data.
* The client must recognize and discard duplicates.
* Reliable delivery requires both data packets and feedback packets.

## Round-by-Round Details ##

Each client will be provided with two GET requests and a series of acknowledgement packets. The server will be given HTML responses that have been divided among a handful packets.

This activity assumes that the client and server have already established a connection. We are starting when the client requests a web page.

### First Connection: Alice Requests the Home Page ###

Alice requests the Concordia home page. The server sends four response packets. Packet #2 is delayed in transit, so packet #3 reaches Alice first. Alice keeps packet #3 but cannot yet assemble the response in order because packet #2 is still missing. She sends `ACK=2` again to indicate that packet #2 is still the next packet she needs. When delayed packet #2 arrives, Alice now has packets #1 through #3 and sends `ACK=4`. Packet #4 is then delivered normally, allowing Alice to complete the webpage.
```
HTTP/1.1 200 OK
Content-Type: text/html

<html><head><title>CUI</title></head>
<body><h1>Welcome!</h1>
<p>Explore our programs.</p></body></html>
```

#### GET Request ####

| Field | Value |
| ----- | ----- |
| Packet ID | `A-GET` |
| SRC IP | `10.1.1.10` |
| SRC Port | `51001` |
| DST IP | `203.0.113.191` |
| DST Port | `80` |
| Packet Type | `DATA` |
| Payload | `GET /index.html HTTP/1.1<br>Host: www.cui.edu<br><br>` |
| Client Instruction | Deliver to the web server |

#### Server Response Cards ####

| Packet ID | SRC IP:Port | DST IP:Port | Packet Type | SEQ | Payload | Router Instruction |
| --------- | ----------- | ----------- | ----- | --- | ------- | ------------------ |
| `A-R1` | `203.0.113.191:80` | `10.1.1.10:51001` | `DATA` | `1` | `HTTP/1.1 200 OK<br>Content-Type: text/html<br><br>` | Deliver normally |
| `A-R2` | `203.0.113.191:80` | `10.1.1.10:51001` | `DATA` | `2` | `<html><head><title>CUI</title></head>` | **Router holds this packet** and delivers it only after `A-R3` has reached Alice and Alice has sent `A-ACK2-DUP`  |
| `A-R3` | `203.0.113.191:80` | `10.1.1.10:51001` | `DATA` | `3` | `<body><h1>Welcome!</h1>` | Deliver before `A-R2` |
| `A-R4` | `203.0.113.191:80` | `10.1.1.10:51001` | `DATA` | `4` | `<p>Explore our programs.</p></body></html>` | Deliver normally but only after the client has received `A-R2` and sent `A-ACK4` |

#### Client ACK Cards ####

| Packet ID | SRC IP:Port | DST IP:Port | Packet Type | ACK | Payload | Router Instruction |
| --------- | ----------- | ----------- | ----- | --- | ------- | ------------------ |
| `A-ACK2` | `10.1.1.10:51001` | `203.0.113.191:80` | `ACK` | `2` | Empty | Send after receiving `A-R1`; Alice has packet #1 and expects packet #2 next |
| `A-ACK2-DUP` | `10.1.1.10:51001` | `203.0.113.191:80` | `ACK` | `2` | Empty | Send after receiving `A-R3` while packet #2 is still missing; Alice keeps packet #3 but still needs packet #2 next |
| `A-ACK4` | `10.1.1.10:51001` | `203.0.113.191:80` | `ACK` | `4` | Empty | Send after receiving delayed packet `A-R2`; Alice now has packets #1 through #3 |
| `A-ACK5` | `10.1.1.10:51001` | `203.0.113.191:80` | `ACK` | `5` | Empty | Send after receiving `A-R4`; the response is complete |

### Second Connection: Bob Requests the Class Schedule ###

Bob requests the class schedule. The server sends three response packets, but packet #2 is dropped in transit. Packet #3 still reaches Bob, so Bob keeps packet #3 and sends `ACK=2` again because packet #2 is still the next missing portion of the response. The server does not receive an acknowledgement showing that Bob has received packet #2. After waiting, the server sends a replacement copy of packet #2. Once Bob receives it, he has all three packets and can assemble the complete response.

**This connection requires the instructor to simulate a time delay.** The server will have sent packets #1 through #3 but not have received an acknowledgement beyond `ACK=2`. After waiting, the instructor will need to indicate to the server that it is time to send replacement packet B-R2-RETX.

```
HTTP/1.1 200 OK
Content-Type: text/html

<html><body><h1>Class Schedule</h1>
<p>Networking: Tuesday 10:30</p></body></html>
```

#### GET Request ####

| Field | Value |
| ----- | ----- |
| Packet ID | `B-GET` |
| SRC IP | `10.2.2.20` |
| SRC Port | `52001` |
| DST IP | `203.0.113.191` |
| DST Port | `80` |
| Packet Type | `DATA` |
| Payload | `GET /schedule.html HTTP/1.1<br>Host: www.cui.edu<br><br>` |
| Student Instruction | Deliver to the web server |

#### Server Response Cards ####

| Packet ID | SRC IP:Port | DST IP:Port | Packet Type | SEQ | Payload | Router Instruction |
| --------- | ----------- | ----------- | ----- | --- | ------- | ------------------ |
| `B-R1` | `203.0.113.191:80` | `10.2.2.20:52001` | `DATA` | `1` | `HTTP/1.1 200 OK<br>Content-Type: text/html<br><br>` | Deliver normally |
| `B-R2` | `203.0.113.191:80` | `10.2.2.20:52001` | `DATA` | `2` | `<html><body><h1>Class Schedule</h1>` | **Drop this packet--do not deliver it to the client** |
| `B-R3` | `203.0.113.191:80` | `10.2.2.20:52001` | `DATA` | `3` | `<p>Networking: Tuesday 10:30</p></body></html>` | Deliver normally |
| `B-R2-RETX` | `203.0.113.191:80` | `10.2.2.20:52001` | `DATA` | `2` | `<html><body><h1>Class Schedule</h1>` | Server sends this replacement copy after Prof. Tallman gives a cue; deliver normally |

#### Client ACK Cards ####

| Packet ID | SRC IP:Port | DST IP:Port | Packet Type | ACK | Payload | Router Instruction |
| --------- | ----------- | ----------- | ----- | --- | ------- | ------------------ |
| `B-ACK2` | `10.2.2.20:52001` | `203.0.113.191:80` | `ACK` | `2` | Empty | Send after receiving `B-R1`; Bob has packet #1 and expects packet #2 next |
| `B-ACK2-DUP` | `10.2.2.20:52001` | `203.0.113.191:80` | `ACK` | `2` | Empty | Send after receiving `B-R3` while packet #2 is missing; Bob keeps packet #3 but still needs packet #2 next |
| `B-ACK4` | `10.2.2.20:52001` | `203.0.113.191:80` | `ACK` | `4` | Empty | Send after receiving `B-R2-RETX`; Bob now has packets #1 through #3 and the response is complete |

### Third Connection: Alice Requests a Photo Gallery ###

Alice requests the main photo gallery. The response is divided into five packets, but packet #3 is dropped in transit. Packets #4 and #5 still reach Alice. She keeps these later packets, but each time one arrives she continues sending `ACK=3`, indicating that packet #3 is still the next missing portion of the response. In this activity, after the server receives repeated ACK=3 messages, it sends another copy of packet #3. Once Alice receives the replacement copy, she has packets #1 through #5 and can assemble the completed webpage in order.

This request also uses a new client port, which helps students see that Alice may have more than one separate web conversation with the same server.

```
HTTP/1.1 200 OK
Content-Type: text/html

<html><body><h1>Campus Photos</h1>
<img src="library.jpg">
<img src="quad.jpg">
</body></html>
```

#### GET Request ####

| Field | Value |
| ----- | ----- |
| Packet ID | `C-GET` |
| SRC IP | `10.1.1.10` |
| SRC Port | `51002` |
| DST IP | `203.0.113.191` |
| DST Port | `80` |
| Packet Type | `DATA` |
| Payload | `GET /photos.html HTTP/1.1<br>Host: www.cui.edu<br><br>` |
| Student Instruction | Deliver to the web server |

#### Server Response Cards ####

| Packet ID | SRC IP:Port | DST IP:Port | Packet Type | SEQ | Payload | Router Instruction |
| --------- | ----------- | ----------- | ----- | --- | ------- | ------------------ |
| `C-R1` | `203.0.113.191:80` | `10.1.1.10:51002` | `DATA` | `1` | `HTTP/1.1 200 OK<br>Content-Type: text/html<br><br>` | Deliver normally |
| `C-R2` | `203.0.113.191:80` | `10.1.1.10:51002` | `DATA` | `2` | `<html><body><h1>Campus Photos</h1>` | Deliver normally |
| `C-R3` | `203.0.113.191:80` | `10.1.1.10:51002` | `DATA` | `3` | `<img src="library.jpg">` | **Router must drop this packet; do not deliver it to the client** |
| `C-R4` | `203.0.113.191:80` | `10.1.1.10:51002` | `DATA` | `4` | `<img src="quad.jpg">` | Deliver normally |
| `C-R5` | `203.0.113.191:80` | `10.1.1.10:51002` | `DATA` | `5` | `</body></html>` | Deliver normally |
| `C-R3-RETX` | `203.0.113.191:80` | `10.1.1.10:51002` | `DATA` | `3` | `<img src="library.jpg">` | After the server receives both `C-ACK3-DUP1` and `C-ACK3-DUP2`, send this replacement copy of packet #3 and deliver normally |

#### Client ACK Cards ####

| Packet ID | SRC IP:Port | DST IP:Port | Packet Type | ACK | Payload | Router Instruction |
| --------- | ----------- | ----------- | ----- | --- | ------- | ------------------ |
| `C-ACK2` | `10.1.1.10:51002` | `203.0.113.191:80` | `ACK` | `2` | Empty | Send after receiving `C-R1`; the client expects packet #2 next |
| `C-ACK3` | `10.1.1.10:51002` | `203.0.113.191:80` | `ACK` | `3` | Empty | Send after receiving `C-R2`; the client expects packet #3 next |
| `C-ACK3-DUP1` | `10.1.1.10:51002` | `203.0.113.191:80` | `ACK` | `3` | Empty | Send after receiving `C-R4` while packet #3 is missing; the client keeps packet #4 but still expects packet #3 next |
| `C-ACK3-DUP2` | `10.1.1.10:51002` | `203.0.113.191:80` | `ACK` | `3` | Empty | Send after receiving `C-R5` while packet #3 is missing; the client keeps packet #5 but still expects packet #3 next |
| `C-ACK6` | `10.1.1.10:51002` | `203.0.113.191:80` | `ACK` | `6` | Empty | Send after receiving `C-R3-RETX`; the client now has packets #1 through #5 and the response is complete |

### Fourth Connection: Bob Requests the Faculty Page ###

Bob requests the computer science faculty page. For this round, the server sends packet #2 and waits for Bob to acknowledge it before continuing with packet #3. Bob receives packet #2 correctly and sends `ACK=3`, but that acknowledgement is dropped in transit. Because the server never receives confirmation that packet #2 arrived, it waits and then sends another copy of packet #2. Bob recognizes that he already received this packet, discards the duplicate data, and sends `ACK=3` again. This time the acknowledgement reaches the server, which continues by sending packets #3 and #4.

This round demonstrates that retransmission does not always mean the original data packet was lost. Sometimes the data arrives successfully, but the acknowledgement is the packet that disappears.

**This connection requires the instructor to simulate a time delay.** The server sent packet #2 and is waiting for `ACK=3` before continuing. After waiting a noticeable time, send `D-R2-RETX`.

```
HTTP/1.1 200 OK
Content-Type: text/html

<html><body><h1>Faculty</h1>
<p>Computer Science Department</p>
</body></html>
```

#### GET Request ####

| Field | Value |
| ----- | ----- |
| Packet ID | `D-GET` |
| SRC IP | `10.2.2.20` |
| SRC Port | `52002` |
| DST IP | `203.0.113.191` |
| DST Port | `80` |
| Packet Type | `DATA` |
| Payload | `GET /faculty.html HTTP/1.1<br>Host: www.cui.edu<br><br>` |
| Student Instruction | Deliver to the web server |

#### Server Response Cards ####

| Packet ID | SRC IP:Port | DST IP:Port | Packet Type | SEQ | Payload | Router Instruction |
| --------- | ----------- | ----------- | ----- | --- | ------- | ------------------ |
| `D-R1` | `203.0.113.191:80` | `10.2.2.20:52002` | `DATA` | `1` | `HTTP/1.1 200 OK<br>Content-Type: text/html<br><br>` | Deliver normally |
| `D-R2` | `203.0.113.191:80` | `10.2.2.20:52002` | `DATA` | `2` | `<html><body><h1>Faculty</h1>` | Deliver normally; after sending this packet, wait for `ACK=3` before sending packet #3 |
| `D-R2-RETX` | `203.0.113.191:80` | `10.2.2.20:52002` | `DATA` | `2` | `<html><body><h1>Faculty</h1>` | After Prof. Tallman gives a cue, send this duplicate copy of packet #2 by delivering normally |
| `D-R3` | `203.0.113.191:80` | `10.2.2.20:52002` | `DATA` | `3` | `<p>Computer Science Department</p>` | Deliver normally only after the server receives `D-ACK3-AGAIN`. |
| `D-R4` | `203.0.113.191:80` | `10.2.2.20:52002` | `DATA` | `4` | `</body></html>` | Deliver normally after the client receives D-R3 and sends D-ACK4 |

#### Client ACK Cards ####

| Packet ID | SRC IP:Port | DST IP:Port | Packet Type | ACK | Payload | Router Instruction |
| --------- | ----------- | ----------- | ----- | --- | ------- | ------------------ |
| `D-ACK2` | `10.2.2.20:52002` | `203.0.113.191:80` | `ACK` | `2` | Empty | Deliver normally after the client receives `D-R1` |
| `D-ACK3` | `10.2.2.20:52002` | `203.0.113.191:80` | `ACK` | `3` | Empty | Send after receiving `D-R2` but it is dropped by a router; **router, do not deliver to the server** |
| `D-ACK3-AGAIN` | `10.2.2.20:52002` | `203.0.113.191:80` | `ACK` | `3` | Empty | Send normally after receiving duplicate packet `D-R2-RETX`; the client already has packet #2, so it discards the duplicate data and acknowledges packet #2 again |
| `D-ACK4` | `10.2.2.20:52002` | `203.0.113.191:80` | `ACK` | `4` | Empty | Deliver normally after the client receives `D-R3` |
| `D-ACK5` | `10.2.2.20:52002` | `203.0.113.191:80` | `ACK` | `5` | Empty | Deliver normally after the client receives `D-R4`; the response is complete |

## Card Layout ##

Each physical packet should be printed on a 3x5 or 5x7 card using this format:

```
PACKET ID: C-R4

SRC IP:    203.0.113.191
SRC PORT:  80

DST IP:    10.1.1.10
DST PORT:  51002

Type:      DATA
SEQ#:      4

PAYLOAD:
<img src="quad.jpg">

ROUTER INSTRUCTION ON BACK:
Deliver normally.
```

For an ACK card:

```
PACKET ID: C-ACK3-DUP1

SRC IP:    10.1.1.10
SRC PORT:  51002

DST IP:    203.0.113.191
DST PORT:  80

Type:      ACK
ACK#:      3

MEANING:
I am still waiting for response packet #3.
```
