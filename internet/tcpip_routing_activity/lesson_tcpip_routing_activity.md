# Routing Table Walkthrough (20-30 min) #

Routers are devices that forward packets from one computer to another, across networks. Routers do not usually know the full story of the message. They do not need to understand the webpage, email, file, or other content being sent. They inspect addressing information and use a routing table to decide where the packet should go next.

A routing table answers a question like this:
> For this destination network, what is the next hop?

Routing is usually **hop-by-hop**. A router does not need to know every step in the complete path from sender to receiver. It only needs to know where to send the packet next.

## Materials ##

Give each student a printed worksheet containing:

- A network topology diagram
- The routing table for the network
- One or two example packets to trace
- A few discussion questions

The topology and routing table should be printed on the same sheet if possible so that students can look back and forth between the diagram and the table.

### Example Network ###

Use the following network diagram:

```
Network A ---- R1 ---- R2 ---- Network B
 10.1.x.x       |       |       10.2.x.x
                |       |
               R3 ---- R4 ---- Network C
                |       |       10.3.x.x
                |       |
Network D ---- R5 ---- R6 ---- Network E
 10.4.x.x                       10.5.x.x
```

For this example:

- Network A contains computers with addresses like `10.1.0.1` and `10.1.0.2`.
- Network B contains computers with addresses like `10.2.0.1` and `10.2.0.2`.
- Network C contains computers with addresses like `10.3.0.1` and `10.3.0.2`.
- Network D contains computers with addresses like `10.4.0.1` and `10.4.0.2`.
- Network E contains computers with addresses like `10.5.0.1` and `10.5.0.2`.

| Network   | Address Range | Default Gateway |
| --------- | ------------- | --------------- |
| Network A | 10.1.x.x      | R1              |
| Network B | 10.2.x.x      | R2              |
| Network C | 10.3.x.x      | R4              |
| Network D | 10.4.x.x      | R5              |
| Network E | 10.5.x.x      | R6              |

Each router is directly connected to the devices or networks shown by the lines in the diagram. For example, R1 is connected to Network A, R2, and R3. R4 is connected to R2, R3, R6, and Network C.

**Note:** Computers usually have very simple routing tables that specify to send all packets to the closest router. This special router is called the *default gateway*. For example, if `10.1.0.1` wants to send a packet to `10.5.0.2`, it first sends the packet to `Network A's` default gateway, `R1`. After that, `R1` uses its routing table.


### Routing Table ###

In this classroom example, students can see the whole routing table so that they can trace packets through the network. In a real network, each router would normally use its own routing table rather than looking at one large table for every router.

| Destination Network | R1 Next Hop | R2 Next Hop | R3 Next Hop | R4 Next Hop | R5 Next Hop | R6 Next Hop |
| ------------------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| `10.1.x.x`          | Local       | R1          | R1          | R3          | R3          | R4          |
| `10.2.x.x`          | R2          | Local       | R1          | R2          | R3          | R4          |
| `10.3.x.x`          | R3          | R4          | R4          | Local       | R6          | R4          |
| `10.4.x.x`          | R3          | R1          | R5          | R6          | Local       | R5          |
| `10.5.x.x`          | R3          | R4          | R5          | R6          | R6          | Local       |

In the routing table, `Local` means that the destination computer is on a network directly connected to that router.

## Teacher-Guided Walkthrough ##

Walk through one packet as a whole class.

Example packet:

```text
From IP: 10.1.0.1
To IP:   10.5.0.2
Message: Hello from Network A.
```

Ask students to identify the destination network:

```text
10.5.0.2 belongs to Network E, or 10.5.x.x.
```

Then trace the packet one router at a time. For each step, ask the students:

- What is the destination network?
- What does the current routing table say for `10.5.x.x`?
- Where should the router send the packet next?

### Step 1: Starting at R1 ###

The packet begins in Network A, so it first reaches R1.

R1's routing table says:

| Destination Network | R1 Next Hop |
| ------------------- | ----------- |
| `10.5.x.x`          | R3          |

So R1 sends the packet to R3.

### Step 2: Packet at R3 ###

Now the packet is at R3.

R3's routing table says:

| Destination Network | R3 Next Hop |
| ------------------- | ----------- |
| `10.5.x.x`          | R5          |

So R3 sends the packet to R5.

### Step 3: Packet at R5 ###

Now the packet is at R5.

R5's routing table says:

| Destination Network | R5 Next Hop |
| ------------------- | ----------- |
| `10.5.x.x`          | R6          |

So R5 sends the packet to R6.

### Step 4: Packet at R6 ###

Now the packet is at R6.

R6's routing table says:

| Destination Network | R6 Next Hop |
| ------------------- | ----------- |
| `10.5.x.x`          | Local       |

This means Network E is directly connected to R6. The packet can now be delivered to the destination computer, `10.5.0.2`.

The final path is:

```
10.1.0.1 → R1 → R3 → R5 → R6 → 10.5.0.2
```

## Student Activity ##

If there is time, have students trace a second packet with less teacher help. Assign source and destination networks to small groups of students.

| Source     | Destination   | Route (Solution)                                                |
| ---------- | ------------- | --------------------------------------------------------------- |
| `10.4.0.2` | `10.2.0.1`    | 10.4.0.2 (Network D) → R5 → R3 → R1 → R2 → 10.2.0.1 (Network B) |
| `10.2.0.7` | `10.5.0.12`   | 10.2.0.7 (Network B) → R2 → R4 → R6 → 10.5.0.12 (Network E)     |
| `10.5.0.1` | `10.3.0.4`    | 10.5.0.1 (Network E) → R6 → R4 → 10.3.0.4 (Network C)           |
| `10.3.0.4` | `10.1.0.221`  | 10.3.0.4 (Network C) → R4 → R3 → R1 → 10.1.0.221 (Network A)    |
| `10.1.0.9` | `10.2.0.178`  | 10.1.0.9 (Network A) → R1 → R2 → 10.2.0.178 (Network B)         |
| `10.3.0.1` | `10.3.0.4`    | Same local network: 10.3.0.1 → 10.3.0.4 (no router needed)      |

## Error Example (Optional) ##

If time allows, briefly show what could go wrong if a routing table has a bad entry.

For example, imagine that R3 has the wrong next hop for Network E:

| Destination Network | R3 Next Hop |
| ------------------- | ----------- |
| `10.5.x.x`          | R1          |

Ask students:

- What would happen to a packet at R3 that is trying to reach Network E?
- Would the packet move closer to the destination?
- Could the packet get delayed or sent in the wrong direction?
- How would this compare to putting a package in the wrong mail bin?

Do not spend too long on this section. The goal is only to show that routing tables matter and that bad routing information can cause failed delivery, delay, or loops.

## Wrap-up Discussion ##

Ask the class:

- Did the sender need to know the whole path to the destination?
- Did each router need to know the whole path?
- What information did each router use to make its decision?
- Did the routers need to understand the message contents?
- What stayed the same as the packet moved through the network?
- What changed at each hop?
- What could happen if a routing table were wrong?

Important points to emphasize:

- Routing is hop-by-hop.
- Each router makes a local decision using its own routing table.
- A routing table tells the router the next hop for a destination network.
- The packet's destination IP address stays the same as it travels.
- The next hop can change at each router.
- Routers do not need to understand the message contents.
- Bad routing information can cause delay, failed delivery, or loops.
- Real networks need routing protocols so routers can learn and update paths.