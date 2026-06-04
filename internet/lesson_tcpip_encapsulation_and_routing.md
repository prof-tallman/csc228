# TCP/IP Encapsulation and Routing: Teacher Outline #

This lesson builds on the previous lesson about packets, addresses, DNS, and HTTP. In that lesson, students learned that messages are divided into packets and that DNS helps computers find the IP address for a human-readable name. This lesson answers the next question: once a computer knows the destination address, how is the message prepared and how does it move across the network?

The lesson has two parts:

1. **TCP/IP Encapsulation Activity**
   Students use a Christmas gift analogy to model how data moves down through the TCP/IP layers. The main idea is that each layer adds information needed for communication, addressing, or local delivery.

2. **Routing Table Walkthrough**
   Students trace packets through a small network using a topology diagram and routing table. The main idea is that routers forward packets one hop at a time using destination addresses and next-hop information.

The two activities should be taught in order. The first activity shows how a packet is prepared and passed from layer to layer. The second activity slows down and explains how routers decide where to send a packet next.

## Timing ##

The full lesson will likely take about **65–75 minutes**, depending on how much of each activity is completed.

| Section                       | Estimated Time |
| ----------------------------- | -------------: |
| Introduction and setup        |          5 min |
| TCP/IP Encapsulation Activity |      30–40 min |
| Transition to routing         |          5 min |
| Routing Table Walkthrough     |      20–30 min |
| Conclusion / exit ticket      |          5 min |

If time is short, use the one-gift version of the encapsulation activity and do only the teacher-guided routing example. If time allows, use the three-gift version, student routing practice, and the optional error example.

## Learning Goals ##

By the end of the lesson, students should be able to:

- Explain why internet communication is divided into layers.
- Describe the basic roles of the application, transport, internet, and link layers.
- Explain encapsulation using a concrete analogy.
- Distinguish between TCP's role and IP's role at a high level.
- Explain that routers use routing tables to decide where to forward packets.
- Trace a packet through a small network using a simple routing table.

## Materials ##

For the TCP/IP Encapsulation Activity:

- Role cards for Application, Transport, Internet, and Link layers
- Gift items or small objects
- Wrapping paper, gift bags, or envelopes
- Personal note labels
- Small shipping boxes or larger envelopes
- Address labels
- Mail bins, folders, trays, or containers for the Link Layer
- Delivery route cards

For the Routing Table Walkthrough:

- Printed student worksheet with network diagram and routing table
- Projected copy of the diagram and routing table, if possible
- Whiteboard or screen for tracing the packet path

## Teacher Preparation ##

Before class, prepare the TCP/IP role cards and place each activity station's materials together. The encapsulation activity works best if students do not have to wait while materials are found or explained.

For the routing activity, prepare a worksheet that includes the network diagram, default gateway table, routing table, and packet examples. Students should be able to look at the topology and routing table on the same page.

Do not try to teach subnet masks, CIDR notation, NAT, ARP, BGP, OSPF, or TCP congestion control in this lesson. Those topics can come later. The goal here is simpler: students should see that messages are prepared in layers and then forwarded through the network one hop at a time.

## Introduction to Part 1: TCP/IP Encapsulation ##

Begin by reminding students what they learned in the previous lesson:

- Large messages are divided into packets.
- Packets need addressing information.
- DNS helps computers find IP addresses for domain names.
- DNS does not send the webpage; it only helps the computer find the address.

Then introduce today's question:

> Once the computer knows the destination address, what actually happens to the message? How is it prepared for travel, and how does it move through the network? How does the GET request actually get (no pun intended) to the server? How does the HTML response make it back to the client?

Explain that internet communication is organized into layers. Each layer has a specific job. A message starts as application data, and then each layer adds information needed for communication, addressing, or local delivery. When the message arrives, the receiver removes those layers in reverse order.

Use the TCP/IP Encapsulation Activity to make this visible. The Christmas gift analogy should help students see that the original data remains inside, while each layer adds something useful around it.

## Part 1: TCP/IP Encapsulation Activity ##

Use the separate [TCP/IP Encapsulation Activity](tcpip_encapsulation_activity/lesson_tcpip_encapsulation.md) teacher version and role cards.

During the activity, keep the focus on encapsulation rather than routing-table decisions. The distribution centers still act like routers, but they follow a simple delivery route. Students will learn how routing decisions are made in the next activity.

## Transition to Part 2: Routing ##

Use this transition after the encapsulation activity:

> In the gift analogy, each distribution center knew where to send the box next. We used a simple delivery route so we could focus on the layers. But real routers do not just magically know where to send packets. They use routing tables. Now we are going to slow down and look at how a router uses the destination address to choose the next hop.

Emphasize the connection:

- In Part 1, the packet moved from hop to hop.
- In Part 2, students will see how the next hop is chosen.
- The destination address stays the same, but the next hop can change at each router.

Explain that a router forwards packets between networks. It does not need to understand the message contents. It looks at the destination network, checks its routing table, and sends the packet to the next hop. The main question at each router is:

> For a given destination network, what is the next hop?

How do packets get from a computer to a router? Computers are configured with a default gateway that helps packets reach the first router. The default gateway is the router that connects the local network to the internet.

## Part 2: Routing Table Walkthrough

Use the separate [TCP/IP Routing Table Walkthrough](tcp_routing_activity/lesson_tcpip_routing_activity.md) teacher version and student worksheet.

Walk through the first packet as a class. Then, if time allows, have students trace additional packets in small groups or discuss what would happen if a routing table had incorrect data. 

## Conclusion

Bring the class back together and ask students to explain the journey of a web request using the vocabulary from the lesson:

1. The application layer creates the request.
2. The transport layer prepares the data for communication.
3. The internet layer adds source and destination IP addresses.
4. The link layer sends the packet to the next local hop.
5. Routers forward the packet using routing tables.
6. The destination computer receives the packet and passes it back up the layers.
7. The application receives and uses the message.

Emphasize the larger picture:

> DNS helps the computer find the destination address. TCP/IP explains how the message is prepared and addressed. Routing explains how packets move across the network one hop at a time.

## Key Terms

- TCP/IP model
- Layer
- Encapsulation
- Application layer
- Transport layer
- Internet layer
- Link layer
- TCP
- IP
- Packet
- Router
- Routing table
- Next hop
- Default gateway

## Possible Exit Ticket

Answer in two or three sentences:

> Why does the TCP/IP model divide the network functionality into layers?

And:

> What is the difference between TCP's job and IP's job?

Lastly:

> When a router receives a packet, what information does it use to decide where to send the packet next?

## Teacher Notes

Keep the lesson focused on the big picture. Students do not need to master real router configuration or all details of the TCP/IP stack yet.

The essential idea is that internet communication is modular. A message is prepared in layers, and then routers forward packets through the network using destination information and routing tables.

## Attribution and Acknowledgements ##

This lesson plan, including its topics, scope, core material, examples, and analogies, was designed by Prof. Tallman. One activity was adapted from an online computer science curriculum licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), as noted in that activity. AI was used to help draft introductory, summary, and transition material; compare possible activity designs; and proofread for clarity, incomplete sentences, and spelling errors.