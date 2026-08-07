# The Postcard Protocol #

In class, we used postcards to model how a message can be divided into small pieces and sent across a delivery network. Each postcard contained part of the message along with enough information to deliver it to the correct destination. That system had several shortcomings.

Suppose your family used these postcards to communicate regularly. You discover several problems with the system:

- Postcards may arrive in a different order than they were sent
- A postcard may occasionally be lost
- Simply sending the postcards does not tell the sender whether the complete message arrived successfully

Your task is to redesign the postcard communication system so that messages can be delivered reliably. The system should allow the recipient to reconstruct the original message correctly, even if the postcards arrive out of order or if one or more postcards are lost in transit. It should also provide a way for **both the sender and the recipient to know whether the entire message was delivered correctly**.

## Part 1: Design the Template ##

Create the template postcard (or templates) that your system will use. Your new postcard must still contain the information necessary to deliver the postcard and carry a portion of the message content (these are the original fields). However, you will need to add new fields that you think are necessary to make the communication reliable. Label each field clearly. For example, the original classroom postcard might have contained areas such as:

**Destination Address:**
[destination address goes here]

**Message Content:**
[part of the message goes here]

Your redesigned system will probably require additional fields.

You may create more than one type of postcard if your communication system needs different postcards for different purposes. If you have more than three different types of postcards, you are probably over-complicating the system.

## Part 2: Document the Protocol ##

Create a table or diagram that defines how your new postcard system works. You do not need to write in complete sentences but you must communicate clearly. At the very least, your table or diagram should contain this information...

1. The name of the field
2. What information goes in the field
3. What problem the field helps solve; or, in other words, why the field is necessary

...and the table/diagram might look something like this:

| Field Name | Information | Problem Solved |
| ---------- | ----------- | -------------- |
| Destination Address | Name and address of the recipient | Tells the post office where to deliver the postcard |
| Message Content | A small portion of the message | Carries as much of the message as can fit on a single postcard. |

## Part 3: Explain the Protocol ##

Write a short user guide that explains how to use your postcard system. Be clear and concise. Use paragraphs and/or bullets as needed. Your guide should explain how the complete system works from beginning to end. It should answer questions such as:

- How can the recipient determine the correct order of the postcards?
- How can the recipient tell whether all of the postcards have arrived?
- What happens if one of the postcards never arrives?
- How does the sender determine whether the complete message was received correctly?
- If something goes wrong, how does your system recover?

## What You Will Submit ##

When finished, submit all three parts of the assignment together. Each part of the assignment can be in a separate file if that makes it easier:

1. Your completed postcard template (or templates). If you created the template on a physical postcard or notecard, upload a photograph.
2. The table or diagram that explains the purpose of each field and why the field is important.
3. A short user guide that describes how two people would use your protocol to send a complete message reliably.

You do **not** need to use technical networking terminology. Design the system based on what you think is necessary to solve the problem. We will compare your solutions to the techniques used by real computer networks.
