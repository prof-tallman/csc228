# How the Internet Works: Teacher Outline #

This lesson gives students a concrete introduction to how the internet moves information and helps computers find one another. Two short, hands-on activities use familiar analogies to make otherwise invisible network processes easier to understand. The emphasis is on building an intuitive foundation that can support later lessons on routing, reliability, security, and other internet technologies.

It has been organized into two topics:
1. [**Data Packetization:**](#Introduction)
2. [**The Domain Name System:**](#Transition)

## Timing ##

My intention is to complete the entire lesson within one hour, but such timing requires focus. Any remaining time in the class period can focus on the readings and discussion of the larger class themes.

| Section                     | Estimated Time |
| --------------------------- | -------------: |
| Introduction to Postcards   |          5 min |
| Postcard Packet Activity    |         20 min |
| Transition to DNS Problem   |          5 min |
| Name Translation Activity   |         15 min |
| Conclusion                  |          5 min |

## Learning Goals ##

By the end of the lesson, students should be able to:

- Explain why internet data is divided into smaller pieces called packets
- Explain the need to address every packet with both source and destination
- Describe a way to reconstruct the original message from its parts
- Explain the challenge of mapping human-readable names to machine addresses
- Trace the basic steps that occur when a user browses a website
- Recognize that the internet depends on technology and trust

## Materials ##

Supplies for the two activities:

- Enough postcards for the class; at least one **set** for every 3-4 students
- IP address slips; two per student should be more than enough
- For the second activity, it's very important that every student has a notebook and a pen/pencil... if the students do not normally bring these, you may need to provide them (or a few extras)

## Teacher Notes ##

- **Keep the first activity focused on packetization and addressing.**
   Students may naturally suggest sequence numbers, acknowledgements, routing, or other solutions to problems they encounter. Those ideas are worth acknowledging, but deeper discussion can be saved for later lessons.
- **Frustration is an important part of learning.**
   The DNS activity works best if students experience at least a little frustration trying to keep track of changing IP addresses. Avoid explaining the purpose of DNS too early; let the problem emerge from the activity first.

## Introduction ##

This lesson introduces students to two basic problems that the internet must solve: how to move large amounts of data between computers and how to locate the computer that should receive that data.

The first activity uses postcards as a simple analogy for data packetization. Students will see how a longer message can be divided into smaller pieces, how each piece needs addressing information, and what limitations arise when messages are sent in this way. The activity is intentionally simplified so that later lessons can build on it with topics such as packet ordering, reliability, and routing.

[**Link to Postcard Packet Activity**](tcpip_postcard_activity/activity_postcard_packets.md)

## Transition ##

The postcard activity establishes that each packet needs a destination address before it can be delivered. This provides a natural transition to the second activity: How does the sender know the correct address?

In everyday life, we usually think about the person or organization we want to reach rather than memorizing their physical address. When necessary, we look up the address in a contact list or ask someone for it. Internet users behave similarly. They remember names such as www.concordia.edu, while computers ultimately need IP addresses to communicate.

Use this distinction to transition into the DNS activity, which demonstrates why maintaining mappings between human-readable names and changing machine addresses becomes difficult as a network grows.

[**Link to DNS Address Book Activity**](dns_directory_activity/activity_dns_address_books.md)

## Conclusion ##

Bring the class back together by connecting the two problems explored in the lesson. First, data must be divided into packets and each packet must contain enough addressing information to reach the correct destination. Second, users usually know the name of the website they want rather than its IP address, so the computer needs a system for finding that address.

Walk through a simple web request from beginning to end:

1. User enters a URL like `http://www.concordia.edu`.
2. Client sends a DNS request to find the corresponding IP address for `www.concordia.edu`.
3. Client sends an HTTP request to the matching IP address.
4. Server responds with the webpage data in small packets.
5. Client receives the data and reconstructs the webpage; browser uses it to display the webpage.

Emphasize that these two systems solve different problems but work together. DNS helps the computer determine where to send the request, while packetization helps the internet move the actual data between computers.

Close by reminding students that these systems also depend on trust. Computers must trust addressing and naming information well enough to communicate with the intended destination. Later lessons can build on this foundation by examining what happens when packets are lost, arrive out of order, take different routes, or when addressing and naming information cannot be trusted.

## Attribution and Acknowledgements ##

The DNS activity is based on [Code.org's DNS Unplugged Activity](https://studio.code.org/courses/csp-2025/units/2/lessons/6#activity-section-51808796), which is licensed under [CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/). It has been adapted and updated slightly; this does not imply endorsement by Code.org.

Prof. Tallman used ChatGPT to help convert his step-by-step activity plans into this lesson-plan overview.
