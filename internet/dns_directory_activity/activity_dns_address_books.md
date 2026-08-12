# DNS Address Book Activity #

Think about how the U.S. Postal System delivers a letter (or postcard). The sender usually cares most about the person who is supposed to receive the message, but the person's name alone is not enough for the Postal Service to deliver it. The postal system does not automatically know where every person lives, and even if it did, people move. A previous address may no longer be valid.

For a postcard to be delivered, it needs the recipient's name and a mailing address. Digital communication has a similar problem. We may know that we want to access a website such as `www.concordia.edu`, but the computer still needs an actual address it can use to find the server where that website is hosted. That machine-usable address is called an IP address. This system is called the Domain Name System (DNS).

## Materials ##

- One prepared IP address slip for each student--just a small slip of paper with an IP address printed on it.
- A second set of IP address slips for changing student addresses during the activity
- It's important that every student has a notebook to hand write their address book... if the students do not normally bring paper or notebooks, grab some paper and pens/pencils

## The Need for a Standard Lookup System ##

This quick learning activity helps students understand why DNS exists in the first place. The exercise itself can be done quickly, typically in about five minutes, before students begin to see the core challenge. If students start running away from you, that's a good sign that they have discovered what makes the activity difficult. Keep the exercise going long enough for students to become at least a little frustrated with all of the changing IP addresses.

### Starting the Exercise ###

When students enter the room, give each of them a slip of paper containing an IP address.

Explain:

> This is your IP address. In order to communicate with another computer on the internet, you need to know its IP address. Your goal is to create and maintain a written list of every one of your classmates' IP addresses. If your classmates represented computers on the internet, this list would allow you to communicate with each one of them.

The only rules are:

- Students may walk around the room.
- Students may share information with classmates.
- Students may talk or share information with only one classmate at a time.
- Students must write the IP address list on a piece of paper.

### During the Exercise ###

As the students work, circulate quietly through the room. Approach a student and silently take away that student's IP address slip. Give the student a new IP address slip, either a new address or one that has been reused. Reusing old address slips is especially useful because the same address may now refer to a different student, creating confusion about which information is current.

Repeat this process with as many students as possible while circulating around the room. The goal is to make it increasingly difficult for students to maintain an accurate list.

### After the Exercise ###

Before discussing the activity, consider holding a quick contest to see who maintained the most accurate address list. Have each student read aloud their current IP address. As the class goes around the room, students should check their own lists and count how many addresses they recorded correctly. Use the honor system and ask students to report their scores at the end. A small prize for the most accurate address list can make the activity more fun.

Ask your students to form small groups and discuss the following questions:

- Why do you think I was switching your IP addresses?
- What made the exercise difficult: the number of classmates, the changing IP addresses, or the fact that information spread person-to-person? Why?
- If this activity had 30 students, it would be annoying. If it had 30 million devices, what new problems would appear?
- What could go wrong if someone gave you the wrong IP address for a website?
- If IP addresses can change, is there a better way for everyone to know everyone else's IP address?

Bring the class back together and discuss their answers. Explain that computers need a standard system for requesting the IP address associated with a particular name. This system is called the **D**omain **N**ame **S**ystem, or DNS.

During the discussion, emphasize several observations:

- Devices are joining and leaving the internet all the time, and IP addresses do not always remain constant. If you go to a coffee shop or restart your router, your device might be assigned a new IP address. IP addresses can change for servers as well.
- If IP addresses can change, it is difficult for every computer to maintain its own accurate list of names and addresses.
- The internet therefore needs shared infrastructure that helps computers find one another at a massive scale.

## The Domain Name System ###

The Domain Name System (DNS) is an internet technology that translates human-readable names into machine-usable IP addresses.

- DNS is useful because people are better at remembering names such as `example.com` than numbers such as `93.184.216.34`.
- DNS also introduces trust. When your computer asks for the IP address associated with a website, it is relying on the DNS system to return the correct answer.
- If someone provides the wrong IP address for a website, a user could be sent to the wrong server. This could cause confusion, failed communication, or security problems.
- Control over names is powerful. Domain names can affect who is easy to find, who is difficult to find, and who gets to decide where a name points.
- DNS is technical infrastructure, but it also has social consequences. It affects communication, commerce, education, security, and even politics.

After establishing these basic ideas, transition the discussion toward the larger security and trust issues created by DNS.

DNS is a distributed system made up of many servers managed by different organizations. No single computer contains all DNS information. Instead, DNS servers follow common rules for answering name-resolution requests and cooperate to determine which IP address corresponds to a requested name. Information may also be stored temporarily so that the same lookup does not need to be repeated immediately.

A user's computer normally sends DNS requests to a DNS resolver selected by the operating system or network configuration. On many networks, this resolver is supplied automatically by the internet service provider or local network administrator. Users can also configure a different DNS resolver if they choose.

Some additional questions for class discussion might include:

- Domain names can be sold, seized, blocked, or redirected. Why does control over naming become a form of power?
- DNS is technical infrastructure, but it affects almost everything online. Who should be trusted to operate or regulate systems like this?

## Attribution and Acknowledgements

The core DNS activity was based on [Code.org's DNS Unplugged Activity](https://studio.code.org/courses/csp-2025/units/2/lessons/6#activity-section-51808796), which is licensed under [CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/). The lesson here has been adapted from Code.org and updated to fit my course; this does not imply endorsement by Code.org.
