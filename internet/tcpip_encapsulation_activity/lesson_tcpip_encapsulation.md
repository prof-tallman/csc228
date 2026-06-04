# TCP/IP Model and Encapsulation (30-40 min) #

Internet communication is organized into layers. Each layer has a specific job, and the layers work together to move data from one computer to another. This activity introduces the four-layer TCP/IP model and uses a Christmas gift analogy to show how data is prepared for delivery.

The main idea is encapsulation. A message starts as application data. Then each layer adds information needed for communication, addressing, or local delivery. When the message arrives, the receiver removes those layers in reverse order.

Use the four-layer TCP/IP model:

| Layer       | Basic Question                                       | Example Role                                 |
| ----------- | ---------------------------------------------------- | -------------------------------------------- |
| Application | What data does the user or program want to send?     | HTTP request, email message, file data       |
| Transport   | How should the data be divided and tracked?          | TCP segments, port numbers, sequence numbers |
| Internet    | Where should the packet go to be delivered?          | IP addresses, routing                        |
| Link        | How does the packet move across the next connection? | Wi-Fi, Ethernet, local delivery              |

This is a simplified model, with only four layers, but it is useful because it shows how different responsibilities are separated. The full model is called the *OSI Model* and it has seven layers. The TCP/IP model provides the same functionality as the larger OSI model, but some of the OSI responsibilities have been combined so that there are fewer layers.

## Materials ##

This exercise requires a few key materials that need to be organized ahead of time. Placing the materials at their designated location will make the exercise faster the help the students focus.

| Role/Layer        | Object       | Printout  | Materials                                                                                |
| ----------------- | ------------ | --------- | ---------------------------------------------------------------------------------------- |
| Application Layer | Gift | [Role Card](tcpip_encapsulation_activity/role_card_application_layer) | Grandma needs the gift and a shipping label, but the grandson does not need anything |
| Transport Layer   | Wrapped Gift | [Role Card](tcpip_encapsulation_activity/role_card_transport_layer) | Small, pre-wrapped boxes or bags just large enough to hold the gifts and personal labels |
| Internet Layer    | Boxed Gift | [Role Card](tcpip_encapsulation_activity/role_card_internet_layer) | Several empty cardboard boxes large enough to hold the wrapped gifts and shipping forms |
| Link Layer        | Binned Box | [Role Card](tcpip_encapsulation_activity/role_card_link_layer) | Labeled mail bins that are big enough to hold the largest cardboard box |

Several of the layers add notes or labels to the gift. The labels should be pre-printed but with blank lines where the students can write in the details. Use tape or blue-tack to affix the labels to the boxes and bins, but choose something that allows the labels to come off easily.

## Attribution ##

The TCP/IP encapsulation activity below is adapted from Mobile CSP's Unit 6.3 Network Architecture lesson, especially its [TCP/IP Packet Routing POGIL activity](https://docs.google.com/document/d/1vCMjrLWMzU-bs1zv8Btu-rjrcvzQ21J0HarznLgL30g/edit?tab=t.0). That activity asks students to act as the application, transport, internet, and link layers while passing paper packets between groups. It is licensed under [CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/). The section below has been adapted from Teach Mobile CSP to more readily fit this course with a gift-giving analogy. This use is educational and does not imply endorsement by Teach Mobile CSP.

## The Christmas Gift Analogy ##

### Introduction ###

To understand encapsulation, imagine that Grandma in Missouri wants to send you a large Christmas gift. After buying the gift, she must package it correctly with wrapping paper, mailing boxes, and shipping labels for it to be transported across the country and arrive safely in Irvine. The packaged gift might travel a path like this:

```
Grandma's Computer in Springfield, MO
→ St. Louis Distribution Center
→ Los Angeles Distribution Center
→ Grandson's Computer in Irvine, CA
```

The Christmas gift, and its delivery through the postal system, is analogous to data sent over the internet. Grandma's computer and the grandson's computer represent endpoints, so they have all four TCP/IP layers. But the distribution centers in St. Louis and Los Angeles represent routers, so they only have Internet and Link layers.

### Application Layer ###

The gift itself is like the data created by the application layer. It is the meaningful content that the sender wants delivered. In internet communication, this might be an HTTP request, part of a webpage, an email message, an image, or some other data created by an application.

However, the gift by itself is not ready to travel across the country. Other information must be added so that it can be delivered correctly.

### Transport Layer ###

First, the large gift is separated into parts that can be easily wrapped and shipped. Each piece is placed in a pretty bag or wrapped in elegant paper and given a personal note.

```
To: Joshua
From: Grandma

Merry Christmas!
This is gift 1 of 3. 
The other gifts are being shipped separately because they would not all fit safely in one box.
```

The individually wrapped gifts with personal notes are like the transport layer. The transport layer helps manage the communication between the sender and receiver. In the TCP/IP model, the TCP layer can divide a larger message into smaller pieces and give the receiver enough information to understand that the pieces belong together.

### Internet Layer ###

Next, the wrapped gift is placed into shipping boxes. Each of the individually wrapped presents is placed in its own shipping box and each box receives its own shipping label. (Note: Although your grandma might have combined all of her gifts into one box, this particular grandma analyzed the probability and cost of a shipment being lost along the way and decided that she would rather only have to replace one of the gifts rather than replacing all of them).

```
From:
Grandma
Grandma's House
Springfield, MO

To:
Grandson (Prof. Tallman)
Concordia University
Irvine, CA
```

These shipping boxes and labels are like the internet layer. The internet layer adds the source and destination IP addresses. These addresses tell the network where the packet came from and where it is supposed to go. The shipping box does not explain what the gift is. It simply gives the address information needed to move the package toward the correct destination.

### Link Layer ###

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

### Unwrapping ###

Eventually, my gift will arrive at the final mail distribution center and be delivered to me in my office. When I receive the gift in the mail, I will unbox it, read the personal note, and then happily unwrap it to find the loving gift sent from my grandmother.

### Summary ###

The important ideas from this analogy are that:

1. The sender adds new information at each layer
2. Intermediate distribution centers handle only the outer layers needed for delivery
3. And the receiver removes the layers in reverse order.

Internet communication works in a similar way. The sender starts with application data, and each layer adds the information needed for the data to travel. The receiver removes and uses that information in reverse order until the original application data is delivered.

| TCP/IP Layer | What It Adds / Processes                             | Christmas Gift Analogy                       |
| ------------ | ---------------------------------------------------- | -------------------------------------------- |
| Application  | The actual message or data                           | The gift itself                              |
| Transport    | Conversation information and reliability information | Wrapping paper and personal note             |
| Internet     | Source and destination IP addresses                  | Shipping box and address label               |
| Link         | Next-hop or local delivery information               | Mail bin, truck, or local shipping container |

In this analogy, we assumed that the destination address was already known. In reality, computers use DNS to find the address for a human-readable hostname. Here, the Application Layer already knows the gift's destination address, and the Internet Layer writes the destination address onto the shipping box.

## Activity ##

### Instructions ###

The simplest version of this activity sends only one wrapped gift, which is enough to demonstrate basic encapsulation. However, the full version below sends a larger Christmas gift that has been divided into three wrapped gifts, such as an ugly Christmas sweater, some baseball cards, and a candy bar. This lets students see that the Transport Layer can divide a larger message (gift) into smaller pieces while still keeping the main focus on encapsulation.

As written, the activity requires at least twelve students.

- Four students represent Grandma's computer: Application Layer, Transport Layer (gift wrapping), Internet Layer (mail packaging), and Link Layer (delivery).
- Four students act as the grandson's computer and his TCP/IP layers: application, transport, internet, and link.
- Four students represent intermediate mail distribution centers, two students for St. Louis and another two for Los Angeles. The mail distribution centers are the equivalent of routers. Routers only provide the Internet Layer and Link Layer. 

If you have fewer students, combine the Internet Layer and Link Layer roles at each location. If you have more students, add observers who watch the activity, take notes, and summarize what each layer did.

Organize students into groups and assign a specific job to each student. Give the groups instruction cards that explain what each student is doing. Tell each group to wait until everyone is ready.

Once the exercise begins, keep an eye on the overall progress and give help as needed. If there is time, have the grandson send a thank you letter back to the grandmother. It might be important to remind the students that there are many more mail distribution centers (routers) and senders/recipients (computers) in the world than these examples.

### Application Layer ###

In this activity, the Application Layer is represented by the person giving or receiving the gift. In a computer network, the Application Layer is a program running on a computer, such as a web browser, email client, or video game. This layer creates or receives the original data.

### Transport Layer ###

The Transport Layer is represented by the person who wraps the gift and adds a note explaining how the pieces belong together. In a computer network, the Transport Layer is part of the operating system. It helps manage communication between programs, including dividing larger messages into smaller parts and helping the receiver understand which parts belong together.

### Internet Layer ###

The Internet Layer is represented by the person who places the wrapped gift into a shipping box and adds the source and destination addresses. On a router or distribution center, the Internet Layer checks the destination address and decides where the box should go next. Both computers and routers have an Internet Layer, but routers do not need the Application or Transport Layers because they are not trying to understand the contents of the message.

### Link Layer ###

The Link Layer is represented by the person who places the boxed gift into a mail bin and delivers it to the next local stop. In a computer network, the Link Layer handles delivery across a specific connection, such as Wi-Fi, Ethernet, fiber, or another network medium. Both computers and routers have a Link Layer.

## Wrap-up Discussion ##

Ask the class:

- Why not just put everything in one giant package?
- Which layer cared about the gift itself (e.g., the data)?
- Which layer cared about delivering the package to the correct destination?
- Which layer cared about whether all parts of the gift had arrived?
- Which layer cared only about the next step in the journey?
- How much did each layer need to understand about the other layers in order to do its job?
- Grandma's note indicated that the gift had multiple parts. What would happen if one part of the gift was missing?

Important points to emphasize:

- Encapsulation means that each layer adds its own information. The kind of information depends on the responsibilities of the layer.
- TCP and IP are not the same thing even though they are often written side-by-side like this: TCP/IP.
- TCP is primarily concerned with reliable communication between two programs (technically, the programs could be on the same computer).
- IP is primarily concerned with addressing and delivering packets across networks.
- The upper layers do not need to know the details that happen at the lower layers.
- The lower layers do not need to understand the user's message or anything above them.
- Layering makes complex communication manageable because each layer has a specific responsibility.