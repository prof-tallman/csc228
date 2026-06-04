# TCP/IP Encapsulation Activity: Role Cards #

## Link Layer ##

**Role:** Delivers item to the next local hop.

### Sending Procedure ###

- **Input:** Boxed item from the Internet Layer
- **Output:** Binned item sent to the next Link Layer

1. Receive boxed item and next hop instructions from the Internet Layer.
2. Place the boxed item into the bin for the next hop.
3. Deliver the bin to the next Link Layer.

- **Report:** "Link Layer placed boxed item into bin and delivered the bin to the next hop."

### Receiving Procedure ###

- **Input:** Binned item from another Link Layer
- **Output:** Boxed item to the Internet Layer

1. Receive a bin from another Link Layer.
2. Remove the boxed item from the bin.
3. Pass the boxed item to the Internet Layer.

- **Report:** "Link Layer received the binned item, removed the box, and passed it to the Internet Layer."

---