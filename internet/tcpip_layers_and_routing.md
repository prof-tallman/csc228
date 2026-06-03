# TCP/IP Layers and Routing #

The purpose of this lesson is to teach students how internet communication is divided into layers and how packets are forwarded through a network. The lesson builds on the previous packet, address, DNS, and HTTP lesson. In the earlier lesson, students learned that messages are divided into packets and that DNS helps computers find IP addresses. This lesson explains what happens after the computer has an IP address: different layers prepare the data for transmission, and routers forward packets toward their destinations.

My goal is for this lesson to take no more than 50 minutes. The TCP/IP model activity should give students a concrete experience with encapsulation, while the routing activity should help them understand that packets often pass through intermediate devices rather than traveling directly from sender to receiver.

## Attribution ##

The routing activity below is adapted from two existing unplugged networking activities: the Network Routing Simulation Activity and Misha Leder's Message Routing activity from Children and Technology. The Network Routing Simulation Activity uses students as routers that exchange routing tables and forward messages. Misha Leder's activity uses tables as small networks, students as computers, and table representatives as routers who pass sticky-note messages.

This lesson has been adapted for educational, noncommercial classroom use and modified to fit this course. This attribution does not imply endorsement by the original authors or organizations. Before posting this lesson publicly, verify the license or reuse permissions for any handouts copied directly from the original sources.

## Learning Goals ##

By the end of this lesson, students should be able to:

* Explain why internet communication is divided into layers.
* Describe the basic role of the application, transport, internet, and link layers.
* Explain encapsulation using a message that receives additional information at each layer.
* Distinguish between TCP's role and IP's role at a high level.
* Explain that routers use routing tables to decide where to forward packets.
* Trace a packet through a small network using a simple routing table.

## Materials ##

* Index cards or small slips of paper
* Envelopes, folders, or folded paper to represent layer headers
* Sticky notes for messages
* Printed group role cards:

  * Application Layer
  * Transport Layer
  * Internet Layer
  * Link Layer
* Printed or projected routing table
* Whiteboard or projected network diagram
* Optional: string or painter's tape to show network links between routers

## Teacher Preparation ##

Before class, prepare a small network diagram. The network should have four to six routers and each router should have a simple routing table. Do not ask students to build the routing tables from scratch. Give them indivually printed routing tables and let them practice using the tables to forward packets. Also give each network a routing table that indicates all traffic should be sent to the default route.

Students who do not have an active role in the exercise should serve as watchers who observe the high-level behavior of the network.

For this lesson, the routing tables should be intentionally simplified. The goal is not to teach subnet masks, CIDR notation, BGP, OSPF, or real router configuration. The goal is for students to see that routers make forwarding decisions using destination information and a table of next hops.

### Configuration for Six Student Actors ###

This small-sized network is ideal for classes with less than twelve people.

**Network Diagram:**
```
Network A ---- R1 ---- R2 ---- Network B
 10.1.x.x        \    /         10.2.x.x
                  \  /
                   R3 ---- Network C
                            10.3.x.x
```

**Routing Table:**
| Destination Network | R1 Next Hop | R2 Next Hop | R3 Next Hop |
| ------------------- | ----------- | ----------- | ----------- |
| 10.1.x.x            | Local       | R1          | R1          |
| 10.2.x.x            | R2          | Local       | R2          |
| 10.3.x.x            | R3          | R3          | Local       |

### Configuration for Nine Student Actors ###

This medium-sized network is ideal for classes with twelve to fifteen people.

**Network Diagram:**
```
Network A ---- R1 ---- R2 ---- Network B
 10.1.x.x        \      |       10.2.x.x
                  \     |
                   R3 - R4 ---- Network C
                   |   /         10.3.x.x
                   |  /
                   R5 ---- Network D
                            10.4.x.x
```

**Routing Table:**
| Destination Network | R1 Next Hop | R2 Next Hop | R3 Next Hop | R4 Next Hop | R5 Next Hop |
| ------------------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 10.1.x.x            | Local       | R1          | R1          | R3          | R3          |
| 10.2.x.x            | R2          | Local       | R1          | R2          | R4          |
| 10.3.x.x            | R3          | R4          | R4          | Local       | R4          |
| 10.4.x.x            | R3          | R4          | R5          | R5          | Local       |

## Part 1: TCP/IP Model and Encapsulation (25 min) ##

The TCP/IP encapsulation activity below is adapted from Mobile CSP's Unit 6.3 Network Architecture lesson, especially its [TCP/IP Packet Routing POGIL activity](https://docs.google.com/document/d/1vCMjrLWMzU-bs1zv8Btu-rjrcvzQ21J0HarznLgL30g/edit?tab=t.0). That activity asks students to act as the application, transport, internet, and link layers while passing paper packets between groups. It is licensed under [CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/). The section below has been adapted from Teach Mobile CSP to more readily fit this course.. It has been updated to use a gift analogy and to include routing activity. This use is educational and does not imply endorsement by Teach Mobile CSP.

To save time, place each role card, routing table, and required materials at the appropriate station before class begins.

### Review from the Previous Lesson ###

Begin by asking students to summarize what they learned in the previous lesson. At this point, the class should still be working together as one big giant group.

Possible prompts:

* Why are large messages divided into packets?
* Why does each packet need an IP address?
* What does DNS do?
* Does DNS send the webpage?
* After DNS gives the computer an IP address, what still has to happen?

Emphasize that DNS only helps the computer find the address. The actual request and response still have to travel through the network.

In the last lesson, we focused mostly on packets and addresses. Today we will look inside the communication process more carefully. A packet does not appear all at once. It is built in layers. Each layer adds information needed for a different part of the communication process.

### Main Idea ###

Explain that internet communication is organized into layers. Each layer has a job. The layers work together, but each layer does not need to know every detail about the other layers.

Use the four-layer TCP/IP model:

| Layer       | Basic Question                                       | Example Role                                 |
| ----------- | ---------------------------------------------------- | -------------------------------------------- |
| Application | What data does the user or program want to send?     | HTTP request, email message, file data       |
| Transport   | How should the data be divided and tracked?          | TCP segments, port numbers, sequence numbers |
| Internet    | Where should the packet go to be delivered?          | IP addresses, routing                        |
| Link        | How does the packet move across the next connection? | Wi-Fi, Ethernet, local delivery              |

Tell students that this is a simplified model, with only four layers, but it is useful because it shows how different responsibilities are separated. The full model is called the *OSI Model* and it has seven layers. The TCP/IP model handles all of the same functionality as the larger OSI model, but in the case of the TCP/IP model, several of the OSI layers have been collapsed into one.

### The Christmas Gift Analogy ###

To understand encapsulation, imagine that Grandma in Missouri wants to send you a large Christmas gift. After buying the gift itself, she must package it correctly with wrapping paper, mailing boxes, and shipping labels for it to be transported across the country and arrive safely in Irvine. The packaged gift might travel a path like this:

```
Grandma's Computer in Springfield, MO
→ St. Louis Distribution Center
→ Los Angeles Distribution Center
→ Prof Tallman's Computer in Irvine, CA
```

Grandma's computer and my computer represent endpoint computers, so they have all four TCP/IP layers. But the distribution centers in St. Louis and Los Angeles represent routers, so they only have Internet and Link layers. The Christmas gift, and it's delivery through the postal system, is analogous to data sent over the internet.

#### Christmas Gift: Application Layer ####

The gift itself is like the data created by the application layer. It represents meaningful content that the sender wants the recepient to recieve. In internet communication, this might be an HTTP request, part of a webpage, an email message, an image, or some other data created by an application.

However, the gift by itself is not ready to travel across the country. Other information must be added so that it can be delivered correctly.

#### Christmas Gift: Transport Layer ####

First, the large gift is separated into parts that can be easily wrapped and shipped. Each piece is wrapped in elegant paper and given a personal note.

```
To: Grandma
From: Joshua

Merry Christmas!
This is gift 1 of 3. 
The other gifts are being shipped separately because they would not all fit safely in one box.
```

The individually wrapped gifts with personal notes are like the transport layer. The transport layer helps manage the communication between the sender and receiver. In the TCP/IP model, TCP layer can divide a larger message into smaller pieces and then help the receiver put them back together.

#### Christmas Gift: Internet Layer ####

Next, the wrapped gift is placed into shipping boxes. Each of the individually wrapped presents is placed in its own shipping box and each box receives its own shipping label. (Note: Although your grandma might have combined all of her gifts into one box, this particular grandma analyzed the probability and cost of a shipment being lost along the way and decided that she would rather only have to replace one of the gifts rather than replacing all of them).

```
From:
Grandma
Grandma's House
Springfield, MO

To:
Prof Tallman
Concordia University
Irvine, CA
```

These shipping boxes and lables are like the internet layer. The internet layer adds the source and destination IP addresses. These addresses tell the network where the packet came from and where it is supposed to go. The shipping box does not explain what the gift is. It simply gives the address information needed to move the package toward the correct destination.

#### Christmas Gift: Link Layer ####

Finally, when the box reaches the post office, it is placed into a mail bin, truck, or shipping container.

```
Next Stop: St. Louis Distribution Center
Carrier: USPS
Truck: Route 17
```

When the bin reaches the St. Louis Distribution Center, it will be moved to a new bin, truck, or shipping container. This next bin will be labeled for the next leg of the journey:

```
Next Stop: Los Angeles Distribution Center
Carrier: USPS
Truck: Route 153
```

This is like the link layer. The link layer is concerned with the next local step in the journey. It does not need to know the entire path from the sender to the final destination. It only needs to know where the package should go next.

As the package moves across the country, the gift is never rewrapped, never reboxed, and the shipping label with my destination address and Grandma's address always stays the same. However, the box may be moved from one mail bin to another, from one truck to another, and from one distribution center to another. Similarly, as an internet packet moves through a network, the destination IP address stays the same, but the local next-hop information can change at each step.

#### Christmas Gift Unwrapping ####

Eventually, my gift will arrive at the final mail distribution center, itself right on the Concordia campus. This final mail center will deliver it to me in my office. When I recieve Grandma's Christmas Gift in the mail, I will unbox it, read the personal note, and then happily unwrap it to find the loving gift sent from my Grandmother.

#### Christmas Gift Summary ####

The important idea is that the sender adds new information at each layer, intermediate routers process and modify the outermost data, then the :

| TCP/IP Layer | Christmas Gift Analogy                       | What It Adds / Processes                             |
| ------------ | -------------------------------------------- | ---------------------------------------------------- |
| Application  | The gift itself                              | The actual message or data                           |
| Transport    | Wrapping paper and personal note             | Conversation information and reliability information |
| Internet     | Shipping box and address label               | Source and destination IP addresses                  |
| Link         | Mail bin, truck, or local shipping container | Next-hop or local delivery information               |

Internet communication works in a similar way. The sender starts with application data, and each layer adds the information needed for the data to travel. The receiver removes and uses that information in reverse order until the original application data is delivered.

In this activity, we assume the destination address is already known. In the previous lesson, DNS explained how a computer can find the address for a human-readable name. Here, the Application Layer knows who the gift is for, and the Internet Layer writes the destination address onto the shipping box.

### Materials ###

This exercise requires a few key materials that need to be fetched and organized ahead of time. The easier it is to distribute these materials to the appropriate individuals, the faster the exercise will go and the more focused the students will be.

| Role/Layer        | Object       | Materials                                                                              |
| ----------------- | ------------ | -------------------------------------------------------------------------------------- |
| Application Layer | Gift         | Grandma needs the gift and a shipping label, but the grandson does not need anything   |
| Transport Layer   | Wrapped Gift | Small, pre-wrapped boxes or bag just large enough to hold the gift and personal labels |
| Internet Layer    | Boxed Gift   | Everal empty cardboard boxes large enough to hold the wrapped gifts and shipping forms |
| Link Layer        | Binned Box   | Labeled mail bins that are big enough to hold the largest cardboard box                |

Several of the layers must add personal notes or labels to the gift. The general fields for these labels should be pre-printed but with blank lines where the students can write in the details. Use tape or blue-tack to affix the labels to the boxes and bins, but choose something that allows the labels should come off easily.

#### Routing Tables ####

This is a summary routing table for the entire mail delivery network. To match a TCP/IP network, each device in the network would only know its own routing table and would be ignorant of the other information--it would only see the information in the column belonging to it.

| Destination  | Grandma's Computer | St. Louis Distribution Center | Los Angeles Distribution Center | Grandson's Computer |
| ------------ | ------------------ | ----------------------------- | ------------------------------- | ------------------- |
| **Grandma**  | Local              | Grandma's Computer            | St. Louis                       | Los Angeles         |
| **Grandson** | St. Louis          | Los Angeles                   | Grandson's Computer             | Local               |

In the routing table, `Local` means "This box has arrived at the destination computer."

### Activity ###

Today we will send only one wrapped gift (e.g., an ugly Christmas sweater) so we can focus on encapsulation and routing. If there is time, we will run the exercise a second time and see what happens when one large message has to be split into multiple pieces, such as an ugly Christmas sweater, some baseball cards, and a candy bar.

As written, the activity requires at least twelve students. If you have fewer students, combine the Internet Layer and Link Layer roles into one person. This can reduce the number of students to eight. If you have more than twelve students, consider adding more intermediate mail distribution centers (routers) or ask the extra students to observe the activity, take notes, and provide a summary for the class.

* Four students will represent Grandma and her gift giving TCP/IP layers. Grandma is the Application Layer. There is also a Transport Layer (gift wrapping), an Internet Layer (mail packaging), and the link layer (delivery).
* Four students will act as the grandson and his gift receiving TCP/IP layers. The Application Layer is the grandson and there is also a Transport Layer, Internet Layer, and the Link Layer.
* Four students will act as the two intermediate mail distribution centers, one in St. Louis and another in Los Angeles. The mail distribution centers are the equivalent of routers. Routers do not have a Transport Layer or an Application Layer. Instead, each router only requires two students: one to act as the Internet Layer and the other as the Link Layer. 

Organize students into groups that will represent each entity. Quickly assign a specific job to each student. Give the groups instruction cards that explain the responsibilties of their role and any necessary supplies. Tell each group to wait until everyone is ready.

Tell the students that when their turn comes, they are to explain what they are doing so that the rest of the class can follow along. For instance, the Internet Layer might say, "I boxed the gift and wrote the source and destination addresses. Next, I looked up the next hop in my routing table. Now I am giving the boxed gift to the Link Layer and telling it the location of the next hop."

Once the exercise begins, keep an eye on the overall progress and give help as needed. There should only be one event happening at a time, giving time to observe and correct as needed. If there is time, have the grandson send a gift (or thank you letter) back to the grandmother. It might be important to remind the students that there are many more mail distribution centers (routers) and senders/recipients (computers) in the world than these examples. The routers would normally have multiple connections and longer routing tables.

#### Application Layer ####

In this activity, the Application Layer is a human being who is giving or receiving a gift. In a computer network, the Application Layer is a program running on a computer such as a web browser or video game. The the other three layers are code that is on the same computer, except that these layers are part of the operating system.

* If you are playing as the grandmother, then your job is to choose a gift for your darling grandson and hand it to your Transport Layer. In addition to the gift itself, you will also need to pass your grandson's full address so that the lower layers know where to send the gift.
* If you are playing the grandson role, then your job is to simply to receive the gift from your Transport Layer. You could write a thank you note and send it back to her--that would sure be polite--but it might go beyond the scope of this exercise and take too much time.

#### Transport Layer ####

For this exercise, the Transport Layer is a person who is pretending to be part of a computer operating system. Whether the operating system is Linux, Windows, or MacOS, it has code in the operating system that functions as the Transport Layer, Internet Layer, and Link Layer. The Application Layer would be a specific program like a web browser or video game. But all four of you are part of the same computer.

* When you receive a gift from the Application Layer, your role is to divide the gift into its individual parts and individually wrap each part. After you have wrapped the parts of the gift, add a personalized note to each one that explains who the gift is for, who it is from, and how many packages it has in total. Hand all of the wrapped and labeled gifts down to your Internet Layer.
* When you recieve a wrapped gift from the Internet Layer, your must read the personalized note and wait for all of the individual gifts to arrive. Then, your job is to to unwrap them all and pass the gift up to your Application Layer.

#### Internet Layer ####

For this activity, the Internet Layer is a person who is pretending to be part of a computer or a router. At this point, your role as Internet Layer is the most complicated. In a future class we will learn new details about the Transport Layer that will make it rise up to a difficulty that is comparable to yours. We will ignore the complexities of the Application Layer and Link Layer in this course.

Both computers and routers contain an Internet Layer, but only computers have the higher layers. Routers have no need for a Transport Layer or Application Layer. The Transport Layer code is part of the operating system.

* When you recieve a box from the Link Layer, your job is to examine the destination address on the gift box and route the box to the correct destination. If the routing table instructs you to keep it local, take the wrapped gift out of the box and pass it up to your Transport Layer. If the routing table instructs you to send the box to the next router, pass the box back down to the Link Layer and tell them the next hop to send the box.
* For those Internet Layers who are part of a **computer only**: When you recieve a wrapped gift from the Transport Layer, you must package the wrapped gift into a shipping box and fill out the *to* and *from* address fields. The *from* field is, obviously, yourself. The *to* address will be given to you, but you must write it on the shipping label. Next, your job is to examine the *to* address and lookup the next hop in your routing table. Then, pass the box down to your Link Layer and tell them exactly where to send it. Note: this role is for computer Link Layers only, routers will never receive a wrapped gift from the Tranpsort Layer because they do not have a Transport Layer.

#### Link Layer ####

In this exercise, the Link Layer is a person who is acting like they are part of the a computer or router. Both computers and routers contain an Internet Layer and a Link Layer, but only computers have Application and Transport Layers. The Link Layer is part of the operating system and contains code that is specific to the type of network connection--whether it is WiFi, Ethernet, fiber, or some other medium.

* If you receive a mail bin from another Link Layer, take the shipping box out of the mail bin and hand it up to your Internet Layer.
* If you receive a shipping box from your Internet Layer, put the box into the mail bin specified by the Internet Layer and then deliver it to the next hop along its path.

### Discussion ###

Ask the class:

* What did each layer add?
* Why not just put everything in one giant package?
* Which layer cared about the gift itself (e.g., the data)?
* Which layer cared about routing the package to the correct destination?
* Which layer cared about the entire gift being complete?
* Which layer cared only about the next local step?
* How does the post office distribution centers, LA and Chicago, know which bin/truck to place each package?
* Grandma's note indicated What would happen if one packet was missing?

Important points to emphasize:

* Encapsulation means that each layer adds its own information.
* TCP and IP are not the same thing even though they are often written side-by-side like this: TCP/IP.
* TCP is primarily concerned with reliable communication between programs (technically, the programs could be on the same computer).
* IP is primarily concerned with addressing and moving packets across networks.
* The upper layers do not need to know the details that happen at the lower layers.
* The lower layers do not need to understand the user's message or anything above them.
* Layering makes complex communication manageable because each layer has a specific responsibility.

## Transition to Routing

The internet layer added the destination IP address, but that does not mean the packet magically appears at the destination. A packet may need to pass through several routers before it reaches the correct network.

In the previous activity, the link layer handed the packet to the next hop. Now we need to understand how that next hop is chosen.

## Part 2: Routing Table Message Passing (20 min)

### Main Idea

Explain that a router is a device that forwards packets between networks. Routers do not usually know the full story of the message. They do not need to understand the webpage, email, or file being sent. They inspect addressing information and use a routing table to decide where the packet should go next.

A routing table answers a question like this:

```text
For this destination network, what is the next hop?
```

### Room Setup

Assign several students or groups to act as routers:

```text
R1, R2, R3, R4
```

Other students or groups act as computers attached to networks:

```text
Network A: 10.1.x.x
Network B: 10.2.x.x
Network C: 10.3.x.x
```

Draw the network diagram on the board. Give each router its own routing table.

### Packet Format

Each packet should have at least the following fields:

```text
From IP:
To IP:
Sequence:
Message:
```

Optional fields:

```text
Source Port:
Destination Port:
TTL:
```

The `TTL` field can be introduced as a simple countdown that prevents a packet from bouncing forever if something goes wrong. Each router subtracts 1 from TTL. If TTL reaches 0, the packet is discarded.

For this activity, use a starting TTL of 5.

### Student Instructions

Tell students:

You are now going to route packets through a small network. Your job is not to guess where the packet goes. Your job is to look at the destination IP address, compare it to your routing table, and pass the packet to the next hop listed in the table.

Rules:

* Routers may look only at the packet's addressing information.
* Routers should not read the message contents aloud.
* Routers must use their routing tables.
* If the destination network is local, deliver the packet to the correct computer.
* If the destination network is not local, forward the packet to the listed next hop.
* If TTL is being used, subtract 1 at each router.
* If TTL reaches 0, discard the packet and report that it expired.

### Round 1: Teacher-Guided Routing

Walk through one packet as a whole class.

Example:

```text
From IP: 10.1.0.1
To IP: 10.3.0.2
Sequence: 1 of 1
Message: Hello from Network A.
TTL: 5
```

Ask:

* What network is the destination on?
* Which router receives the packet first?
* What does that router's table say?
* What is the next hop?
* When does the packet reach the local destination network?

Make the path visible on the board.

### Round 2: Student Routing

Give several packets to different starting computers. Students route the packets at the same time.

Possible packets:

```text
10.1.0.1 -> 10.2.0.2
10.2.0.1 -> 10.3.0.1
10.3.0.2 -> 10.1.0.2
10.1.0.2 -> 10.3.0.1
```

After the packets arrive, ask each destination to report:

* Did the packet arrive?
* What path did it take?
* Did every router need to know the whole path?
* Did every router need to know the message contents?

### Round 3: Broken Route or Wrong Table Entry

Introduce one controlled failure.

Option A: Remove a link between two routers.

Option B: Give one router a bad routing-table entry.

Option C: Lower the packet's TTL so it expires before reaching the destination.

Ask students to observe what happens.

Discussion prompts:

* Where did the packet get stuck?
* Did the sender know the route ahead of time?
* Did the routers know the whole network?
* What could happen if a routing table is wrong?
* What would happen if routers disagreed about where packets should go?

Important points:

* Routing is hop-by-hop.
* Each router makes a local decision.
* The packet's destination address stays the same, but the next hop changes.
* Bad routing information can cause delay, failed delivery, or loops.
* Real networks need routing protocols so routers can learn and update paths.

## Optional Extension: Building Routing Tables (Advanced, 10-20 extra min)

If time allows, use a simplified version of the Network Routing Simulation Activity.

Instead of giving students completed routing tables, have each router start with only itself and its direct neighbors.

Example starting table for R1:

| Destination | Next Hop | Distance |
| ----------- | -------- | -------- |
| R1          | Local    | 0        |
| R2          | R2       | 1        |
| R3          | R3       | 1        |

Routers then compare tables with neighboring routers. If a neighbor knows a shorter path to a destination, the router updates its own table.

Simplified rule:

```text
If my neighbor can reach a destination in N hops,
then I can reach it through that neighbor in N + 1 hops.
```

Repeat until no routing table changes.

This extension is useful, but it may take too long for a 50-minute class. It is better as a follow-up lesson or a challenge activity.

## Conclusion (5 min)

Bring the class back together.

Ask students to explain the journey of a web request using the vocabulary from the lesson:

1. The application layer creates the request.
2. The transport layer prepares the data for reliable communication.
3. The internet layer adds IP addressing.
4. The link layer sends the packet to the next local hop.
5. Routers use routing tables to forward the packet toward the destination network.
6. The destination computer receives the packet and passes it back up the layers.
7. The application receives and uses the message.

Emphasize:

DNS helped us find the IP address in the previous lesson. TCP/IP explains how the message is prepared and addressed. Routing explains how packets move through the network one hop at a time.

## Key Terms

* TCP/IP model
* Layer
* Encapsulation
* Application layer
* Transport layer
* Internet layer
* Link layer
* TCP
* IP
* Port
* Sequence number
* Packet
* Router
* Routing table
* Next hop
* TTL

## Possible Exit Ticket

Answer in two or three sentences:

```text
What is the difference between TCP's job and IP's job?
```

Then answer:

```text
When a router receives a packet, what information does it use to decide where to send the packet next?
```

## Teacher Notes

This lesson should avoid overexplaining real-world protocol details. Students do not need to learn OSI layers, subnet masks, CIDR notation, NAT, ARP, BGP, OSPF, or TCP congestion control yet. Those topics can be introduced later.

The essential idea is that internet communication is modular. A message is prepared in layers, and then routers forward packets through the network using destination information and routing tables.
