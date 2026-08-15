# Digital Certificates and Wax Seals Activity #

Public-key cryptography allows a sender to create a digital signature that others can verify. A valid signature can help show that a message has not been changed and that it was signed using the expected private key.

But there is still an important question:

> **How do you know that the public key really belongs to the person or organization it claims to represent?**

This activity uses wax seals as a simplified analogy for digital signatures, public keys, and certificates. The analogy is not perfect, but it helps demonstrate the difference between verifying a signature and verifying an identity.

## Materials ##

For each group:

- One wax seal stamp
- Sealing wax and supplies to melt the wax
- Message paper
- Small notecards or slips of paper
- Pens or pencils

For the class:

- Whiteboard space for a public directory
- One separate instructor wax seal
- Blank cards or paper for certificates

## Publish Your Seal ##

Divide into groups of three or four students and collect your wax stamp. This stamp will represent your group's private key. No other group should have the same stamp.

Make a test wax impression with your stamp and examine the design. Once you feel comfortable with the kit, go to the whiteboard and write your group name next to a simple drawing of the seal's recognizable pattern.

The whiteboard acts as a common place to store public keys. The drawing of the seal serves as a rough classroom stand-in for your public key, or more precisely, public information that other groups can use to recognize signatures created with your private stamp.

For the purposes of this activity, assume:
- every group's metal seal is unique;
- no duplicate copy exists;
- seeing the pattern does not allow someone to manufacture your private seal.

Real public-key cryptography achieves these properties mathematically rather than with physical objects.

## Seal a Message ##

Select a message and a blank notecard from Prof. Tallman's collection. Read the message and then create a simple classroom "hash" of the message on the blank notecard. The hash should include the message's word count and total character count (letters, numbers, punctuation, etc). You may also include a one-sentence description of the message for reference.

After creating the hash, fold the two sides of the notecard inward to the center and then seal it with your group's wax stamp. Send the original message and the sealed hash to another group.

The activity now represents the following pieces of a digital-signature system:

| Wax-Seal Activity                    | Cryptography                 |
| ------------------------------------ | ---------------------------: |
| Metal wax stamp                      | Private key                  |
| Public seal drawing                  | Public key                   |
| Classroom hash                       | Cryptographic hash           |
| Sealing the folded hash              | Creating a digital signature |
| Sealed hash accompanying the message | Digital signature            |

## Verify a Sealed Message ##

When your group receives a sealed message, identify the claimed sender. Look at that group's entry on the whiteboard and compare the wax impression on the sealed slip with the published seal drawing. Then open the slip and recalculate the hash from the received message. Ask yourselves:

- Does the wax impression match the sender's published information?
- Does the recalculated hash match the value inside the sealed slip?
- What would happen if someone changed the original message after it had been signed?

At this point, the signing system should seem reasonably successful. But there is still a problem.

## The Identity Problem ##

Look again at the public directory on the whiteboard. Who verified that the name next to each seal is correct? Suppose someone writes:

```
University President → [their own seal drawing]
```

and they actually possess the matching private seal. They could now create messages whose signatures verify perfectly. Would our wax-seal signing system detect that the person had lied about their identity?

Discuss:

- What does a valid signature actually prove?
- What does it not prove?
- How could someone falsely associate their own public key with another person's identity?
- What additional information or authority would you need before trusting the identity written next to a public key?

The important idea is:

> The signature can be valid even though the identity is false.

## Add a Trusted Authority ##

The class now needs a way to verify the connection between an identity and its public information. The instructor will act as a trusted authority. Each group should create a simple record containing the group's name, the group's public seal drawing, and a brief statement connecting the two. For example:

> The public seal shown below belongs to Group Falcon.

The instructor will verify the information and then sign the record using a separate instructor wax seal. This signed record represents a digital certificate. The instructor is acting as a certificate authority (CA). The certificate now makes a trusted claim:

> This public information belongs to this identity.

## Use the Certificate ##

Suppose you receive a signed message from a group you have never communicated with before. You now have the original message, the sealed hash that verifies against the signer's public information, and the group's certificate to map the public key to a CA-verified identity. You can work through the chain:

1. Do you trust the instructor's seal?
2. Does the instructor-signed certificate connect the group name to a particular public seal?
3. Does the signature on the message match that certified public seal?
4. Does the hash match the message?

If all of these checks succeed, you have stronger evidence that (1) the message was not changed; (2) the expected private key was used; (3) the public key really belongs to the claimed identity. The chain of trust now looks like this:

> Trusted Authority → Certificate → Public Key → Signature → Message

## The Internet Connection ##

Websites use the same general idea of using a trusted authority to connect public keys to identities. A web server has a public/private key pair. The server can present a public key, but simply providing the key does not prove who owns it. A digital certificate connects an identity, usually a domain name, with a public key.

For example, a digital certificate, at its core, provides the following information:

```
www.example.com → Public Key
```

A certificate authority digitally signs that certificate. A browser can then verify that signature and determine whether it trusts the authority that issued the certificate. The analogy looks roughly like this:

| Classroom Activity               | Internet System       |
| -------------------------------- | --------------------- |
| Group                            | Website/server        |
| Metal wax stamp                  | Private key           |
| Public seal information          | Public key            |
| Message summary                  | Cryptographic hash    |
| Sealed hash                      | Digital signature     |
| Record connecting group and seal | Digital certificate   |
| Instructor                       | Certificate authority |
| Instructor's seal                | CA digital signature  |

## Where Does the Trust Begin? ##

Think back to the classroom activity. Why did you trust your professor's seal? You did not need another wax certificate proving that Prof. Tallman was really your professor. You already had an independent reason to trust his identity. That prior trust served as the starting point for the entire certificate system you built in class.

Real certificate systems also need a starting point. Browsers and operating systems therefore contain collections of trusted root certificates. These identify certificate authorities that the system has already been configured to trust.

In other words, the chain does not continue forever. Eventually it reaches a root certificate that is trusted because the operating system or browser has chosen to trust it. We trust software vendors such as Microsoft, Apple, Google, and Mozilla to decide which certificate authorities should be included in their trust stores--although organizations such as Concordia can install new trusted roots on systems they manage.

## One Important Limitation ##

A valid digital certificate does not mean that a website is necessarily safe or honest. Suppose you receive an email or text containing a link to:

```
concordia-account-security.example
```

The site might use HTTPS and have a valid certificate. But the certificate would only prove you are securely connected to `concordia-account-security.example`. It does not prove that this domain belongs to Concordia University.

An attacker may not need to break encryption or compromise a certificate authority. Sometimes it is much easier to convince someone to visit the wrong domain.

## Wrap-Up Discussion ##

In your group first, and then--if there's time--with the entire class, discuss the following questions:

- Why wasn't the original whiteboard directory enough to establish identity?
- What problem did the certificate authority solve?
- Why must browsers and operating systems begin by trusting some root certificates?
- How can a phishing website have a valid HTTPS certificate and still be dangerous?

The central distinction is that a digital signature helps verify a message and the key that signed it. A digital certificate helps verify whose key it is. The certificate authority is who we trust to verify the connection between the public key and the identity of the owner.

## Limits of the Analogy ##

The wax-seal activity is intended to model the relationships among keys, signatures, identity, and trust. It does not reproduce the cryptographic mathematics exactly.

A real public-key system has two mathematically related but distinct keys. The wax system has only one physical object. In this activity, the metal stamp represents the private key, while the public drawing of its recognizable pattern represents information that can be used for verification.

Real wax seals can also be copied, purchased, or manufactured. For this activity, assume that every seal is unique and impossible to duplicate. Properly generated cryptographic keys are drawn from such an enormous number of possibilities that accidental duplication is treated as effectively impossible, and public-key systems are designed so that recovering the private key from the public key is computationally impractical.

Finally, summaries, word counts, and character counts are very poor substitutes for real cryptographic hashes. They are used only because students can calculate them quickly by hand.

## Attribution and Acknowledgements ##

The original wax-seal idea in this activity was inspired by a brief lesson summary from [Flip Education](https://flipeducation.ai/curriculum/ca/computer-science/grade-12/digital-signatures-and-certificates/activities#activity-1). Their summary provided the initial spark for using physical seals to illustrate digital signatures; Prof. Tallman developed the lesson itself separately and then used GenAI to convert his raw activity into a polished lesson-plan format that he then edited and revised.
