# TCP/IP Encapsulation Activity: Role Cards #

## Transport Layer ##

**Role:** Prepare application data for end-to-end communication.

### Sending Procedure ###

- **Input:** Original item from the Application Layer
- **Output:** Wrapped item(s) with transport notes

1. Receive the original item/message from the Application Layer.
2. Divide it into individual parts (as makes sense).
3. Wrap or bag each part.
4. Attach a note identifying the sender, receiver, and total number of related parts.
5. Pass the wrapped item(s) to the Internet Layer, each item one at a time in separate steps.

- **Report:** "Transport Layer prepared the data for delivery by wrapping it and marking which parts belong together."

### Receiving Procedure ###

- **Input:** Wrapped item(s) with transport notes
- **Output:** Original item for the Application Layer

1. Receive a wrapped item from the Internet Layer.
2. Read the attached notes.
3. Confirm that all related parts have arrived.
4. Remove the wrapping.
5. Pass the original item/message to the Application Layer.

- **Report:** "Transport Layer received the items, unwrapped them, and (if necessary) recombined them into one item."

---