# Router Maze: Timmy Goes to Timbuktu #

In class, we learned that routers do not need to know the entire path that a packet will take across the Internet. Each router looks at the packet's destination address, consults its routing table, and decides where to send the packet next.

In this assignment, you will work backward from a collection of routing tables to discover how a small, fictional internet is connected. Then you will help a packet named "Timmy" travel from his starting location to Timbuktu. Unfortunately, as you will find, someone has made a mistake in the routing tables.

The purpose of this assignment is not to memorize routing-table syntax. Instead, use the tables to reason carefully about where each packet will go.

## The Network ##

This Internet contains ten routers. Each router is named after the city where it is located and each city has one or more `/24` networks connected directly to it. You do not have a diagram of the network. Instead, you must determine how the routers are connected by examining their routing tables.

## Reading the Routing Tables ##

The table below combines the routing tables from all ten routers. Each column represents one router. Each row represents a destination network. An entry of `Direct` means that the router is directly connected to that network.

An entry containing the name of another city means:

> Send packets for this destination to the router in that city.

For example, suppose the Huaraz router contained this entry:

| Destination   | Huaraz |
| ------------- | ------ |
| `10.2.0.0/24` | Lima   |

This means that when Huaraz receives a packet destined for the `10.2.0.0/24` network, it sends the packet to the Lima router.

Remember that a router does not need to know the entire path to the destination. It only needs to determine the next hop. Also, do not assume that the route chosen by a router will always be the geographically shortest route.

## Routing Tables

Whenever one router lists another router as its next hop, it means that those two routers are directly connected.

In a real network, each router stores its own routing table. For this assignment, the ten routing tables have been combined into one larger table to make them easier to read. Each column represents the routing table for one router. Each router would be unaware of the other columns in the table.

| Network        | Huaraz | Lima   | Quito   | Managua | Atlanta |  Funchal   | Casablanca | Bamako     | Dakar    | Timbuktu |
| -------------- | ------ | ------ | ------- | ------- | ------- | ---------- | ---------- | ---------- | -------- | -------- |
| `10.1.0.0/24`  | Direct | Huaraz | Lima    | Quito   | Managua | Atlanta    | Funchal    | Timbuktu   | Managua  | Dakar    |
| `10.2.0.0/24`  | Lima   | Direct | Lima    | Quito   | Managua | Atlanta    | Funchal    | Timbuktu   | Managua  | Dakar    |
| `10.3.0.0/24`  | Lima   | Quito  | Direct  | Quito   | Managua | Atlanta    | Funchal    | Timbuktu   | Managua  | Dakar    |
| `10.4.0.0/24`  | Lima   | Quito  | Managua | Direct  | Managua | Atlanta    | Funchal    | Timbuktu   | Managua  | Dakar    |
| `10.5.0.0/24`  | Lima   | Quito  | Managua | Atlanta | Direct  | Atlanta    | Funchal    | Casablanca | Managua  | Dakar    |
| `10.6.0.0/24`  | Lima   | Quito  | Managua | Atlanta | Funchal | Direct     | Funchal    | Casablanca | Managua  | Bamako   |
| `10.7.0.0/24`  | Lima   | Quito  | Managua | Atlanta | Funchal | Casablanca | Direct     | Casablanca | Timbuktu | Bamako   |
| `10.8.0.0/24`  | Lima   | Quito  | Managua | Atlanta | Funchal | Casablanca | Bamako     | Direct     | Timbuktu | Bamako   |
| `10.9.0.0/24`  | Lima   | Quito  | Managua | Dakar   | Managua | Atlanta    | Bamako     | Timbuktu   | Direct   | Dakar    |
| `10.10.0.0/24` | Lima   | Quito  | Managua | Dakar   | Funchal | Casablanca | Bamako     | Timbuktu   | Managua  | Direct   |
| `10.12.0.0/24` | Lima   | Quito  | Managua | Atlanta | Funchal | Direct     | Funchal    | Casablanca | Managua  | Bamako   |
| `10.14.0.0/24` | Lima   | Quito  | Managua | Atlanta | Funchal | Casablanca | Direct     | Casablanca | Timbuktu | Bamako   |
| `10.16.0.0/24` | Lima   | Quito  | Managua | Atlanta | Funchal | Casablanca | Bamako     | Direct     | Timbuktu | Bamako   |
| `10.18.0.0/24` | Lima   | Quito  | Managua | Dakar   | Managua | Atlanta    | Bamako     | Timbuktu   | Direct   | Dakar    |
| `10.20.0.0/24` | Lima   | Quito  | Managua | Dakar   | Funchal | Casablanca | Bamako     | Timbuktu   | Timbuktu | Direct   |

Each city begins with a different letter of the alphabet, so it is acceptable to use the first letter as an abbreviation for the city.

## Part 1: Draw the Internet ##

Using only the routing tables, draw a diagram showing how the routers and local networks are physically connected. Do not use the geographic locations of the cities to decide which routers should be connected. Your diagram must come from the routing tables. Your diagram should include:

- All ten routers
- The `/24` local networks attached to each router
- A line between every pair of directly connected routers
- A line between every local network and its directly connected router

Keep in mind that a routing table normally stores the paths a router uses, not necessarily every physical connection that exists. There could be additional links that are not visible from the provided information. Ignore these undocumented physical connections. Your diagram should only include the physical connections that can be inferred from the routing tables.

It is somewhat standard to draw each router (city) inside a small circle and each `/24` local network with a small cloud around it. Draw lines between the routers and networks to indicate connections. However, if you would prefer to draw the network as a maze, such a drawing would illustrate the same information. For a maze, each router or network is an intersection and the connections should be drawn as passageways.

## Part 2: Follow Timmy ##

Timmy is a packet that begins at a computer with IP address `10.1.0.25`. Draw a "T" next to the local network where Timmy begins his journey. Timmy wants to reach a host whose destination address is `10.10.0.25`. Draw a star next to the local network where Timmy's destination host is located.

Beginning with Timmy's local network, use the routing tables to determine where each router sends Timmy next. Record his journey one router at a time. But be careful, there's currently a problem in the routing tables that prevents Timmy from reaching his destination.

### Timmy's Original Route ###

`10.1.0.25 → ___________________________________________________ → 10.10.0.25`

Something is wrong. Eventually, Timmy will begin visiting the same routers repeatedly instead of getting closer to his destination.

1. Which routers does Timmy repeatedly visit?
2. Which routing-table entry is incorrect, causing a loop?

## Part 3: Repair the Routing Tables ##

One of the routing-table entries has been entered incorrectly and it concerns Timmy's destination network, `10.10.0.0/24`. Use your network diagram and the other routing information to locate the mistake. For the incorrect entry, record:

| Router | Incorrect Next Hop | Correct Next Hop |
| ------ | ------------------ | ---------------- |
| `_____________` | `_____________` | `_____________` |

After making the correction, retrace Timmy's route from his starting network to his destination.

### Timmy's Corrected Route ###

`10.1.0.25 → ___________________________________________________ → 10.10.0.25`

3. Explain briefly why the corrected route works.

## Part 4: The Cable Breaks ##

Timmy can finally reach Timbuktu, but unfortunately the network has a new problem. The connection between Managua and Dakar has gone down after the long-distance cable carrying that connection was damaged. Packets can no longer travel directly between Managua and Dakar.

Do not add any new routers or physical connections. The network must be used as it already exists.

### Find Another Way

Timmy still needs to travel from `10.1.0.25` to `10.10.0.25`. Using your network diagram, find another path to Timbuktu that avoids the failed connection.

Determine the smallest routing-table change necessary to send Timmy along this alternate path.

Complete the following:

| Router Table to Change | Destination Network | Old Next Hop | New Next Hop |
| ---------------------- | ------------------- | ------------ | ------------ |
| `____________________________`| `____________________________`|  `____________________________`|  `____________________________`| 

Now trace Timmy's new route:

`10.1.0.25 → ___________________________________________________ → 10.10.0.25`

## Part 5: Explain What Happened ##

Answer the following questions briefly.

4. How were you able to determine which routers were directly connected without being given a network diagram?
5. Why did the original routing mistake cause Timmy to travel in a loop?
6. Does the Huaraz router need to know Timmy's complete route from his starting network to his destination?
7. When the cable failed, why was it possible to find another route without building a new physical connection?
8. What does this activity demonstrate about the difference between a physical network connection and a routing decision?

## What You Will Submit ##

Submit all parts of the assignment together. Your submission should include:

- Your completed network diagram with a "T" for Timmy's initial location and a star for the destination network
- Timmy's original route
- Your identification and correction of the incorrect routing-table entry
- Timmy's corrected route
- Your solution to the cable failure
- Your answers to the explanation questions

Your network diagram may be created digitally or drawn neatly by hand and photographed or scanned.
