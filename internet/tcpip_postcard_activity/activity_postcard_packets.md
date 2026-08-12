# The Postcard Packets Activity #

This activity uses postcards as a simple analogy for data packetization. Students work with a longer message that has been divided across several postcards and consider what information is necessary for each piece to reach its destination. I composed my set of postcards while on vacation, so the activity has a bit of authenticity and fun to it.

The activity focuses on two basic ideas: dividing a larger message into smaller pieces and addressing each piece individually. Other networking concepts such as sequence numbers, acknowledgements, reliability, and routing are intentionally omitted. Students may discover some of these ideas on their own, but the topics have been purposely reserved for future lessons.

## Materials ##

To prepare for this activity, you must first choose between giving distinct messages to different groups, or distributing identical sets to every group. If every group receives the same message, it may be easier to compare and discuss their findings as a class. Using unique messages can make the activity more interesting and also allows groups to trade messages. Once you have made this decision, here are the supplies you will need:

- One set of prepared postcards for every 3–4 students
- Use at least four postcards per set... and probably no more than eight

## Introduce Postcards ##

Each set of postcards should contain one complete message divided across several cards. Each postcard should contain only one or two sentences. Four postcards per set works well: there are enough pieces to make reconstruction interesting without making the activity cumbersome. Groups may all receive the same message, or several different versions can be prepared. The order of the sentences should be intentionally somewhat ambiguous. Students should be able to identify a likely beginning and ending, but the correct order of the middle portions should not be obvious. 

Avoid resolving the packet-ordering problem during this activity. If students suggest numbering the cards, adding sequence information, requesting missing cards, or other solutions, acknowledge the ideas but save the deeper discussion for a later lesson on reliability.

## Example Postcard Contents ##

The postcards should have messages that are something like this:

### Group #1 ###

1. Dear Dog, I hope that you are enjoying your time at home.
2. We are having fun on the vacation but certainly miss you.
3. Today we saw a herd of bison and a large bear, but no moose.
4. You are better off at home with Grandma and Grandpa because Dad is doing the cooking. Love, your family.

### Group #2 ###

1. Dear Dog, How are you getting along at home?
2. The driving days are very long and we sometimes get into arguments.
3. Dad is getting a little stinky and can be cranky at times.
4. I hope that you are going on nice walks. Love, your family.

### Group #3 ###

1. Dear Dog, We have reached the family reunion.
2. You would like it here a lot, especially cousin Sally.
3. Dad's family is surprisingly normal considering how strange he is.
4. Pass on our love to Grandma and Grandpa. Love, your family.

## Postcard Activity ##

Divide the class into groups of three or four students and give each group one set of postcards.

Explain that a family wanted to send a message home while traveling, but the complete message was too long to fit on a single postcard. Instead, the message was divided across several postcards.

Ask each group to reconstruct what they think the original message was. As they work, students should also examine the communication system itself and take notes about what they observe. For example, they should observe things like:

- What information must appear on each postcard for it to reach the correct destination?
- How a long message can be divided into smaller chunks.
- What limits the amount of information that can be placed on one postcard?
- Could the message have been divided in a more efficient or logical way?
- What difficulties arise when trying to reconstruct the complete message?

Each group should agree on some answers and take notes. All this shouldn't take more than five or ten minutes.

## Wrap-Up Discussion ##

Discuss the results as a whole class. Ask one of the groups to summarize their experience. Ask the other groups to correct errors or fill in any missing information. Was this an easy task? What parts, if any, were difficult? There are a few details that should be covered during the discussion:

- Large messages can be divided into smaller pieces. On the internet, these pieces are called packets.
- Each packet needs addressing information so the network knows where to send it.
- There are different parts of an address, each one having a different level of detail. The state and city are at the highest level, then the street and house number. The first and last name are the most granular pieces of information.
- Communication systems often have size limits. A postcard has limited writing space; network packets also have maximum sizes.
- Humans can often infer missing order because we are intelligent and understand context, but computers need explicit rules and extra information.
- One of the postcards might be lost along the way, or the postcards could arrive at different times.
- People handling the postcards in the postal system could potentially read their contents.
- Mail usually includes a destination address and a source address, so the receiver knows where the packet came from and where replies should go. Internet packets are similar.

In this analogy, each postcard was like a small piece of data sent on the internet, called a packet. A packet is a small piece of data with delivery information attached. Packets are part of larger messages sent between computers. Instead of sending one large block of data, network communication divides information into manageable pieces that can be transmitted separately. The receiving computer ultimately needs to reconstruct the larger message from those individual pieces.

This activity intentionally leaves several problems unresolved: Why is the message divided into packets instead of being sent all at once? What happens if packets arrive out of order? What happens if one is lost? How does the sender know whether everything arrived successfully? Those questions lead naturally into future discussions about TCP, reliability, and routing.
