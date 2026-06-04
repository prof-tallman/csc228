# TCP/IP Encapsulation Activity: Role Cards #

## Internet Layer ##

**Role:** Adds source/destination addressing and boxes the item for mail delivery.

**Route:** `Grandma` → `St. Louis` → `Los Angeles` → `Grandson`

### Sending Procedure ###

- **Input:** Wrapped item from the Transport Layer
- **Output:** Boxed item with source and destination addresses

1. Receive wrapped item from the Transport Layer.
2. Place each wrapped item into a shipping box.
3. Add the source and destination address label.
4. Use the delivery route to identify the next hop.
5. Pass the boxed item to the Link Layer and state the next hop.

- **Report:** "Internet Layer boxed the wrapped item, identified the next hop, and passed the box to the Link Layer."

### Receiving Procedure ###

- **Input:** Boxed item from the Link Layer, with source and destination addresses
- **Output:** Wrapped item for the Transport Layer **or** Boxed item for the Link Layer with source and destination address

1. Receive boxed item from the Link Layer.
2. Check the destination address.
3. If the box is addressed to this endpoint, open the box.
    - Remove the wrapped item.
    - Pass the wrapped item to the Transport Layer.
4. Otherwise, do *not* open the box.
    - Pass it back to the Link Layer
    - Tell the link layer the next hop along the route.

- **Report:** "Internet Layer checked the destination address, noticed it was the intended recipient, removed the item from the box, and passed it to the Transport Layer." **or** "Internet Layer checked the destination address and identified the next hop for the Link Layer."

---
