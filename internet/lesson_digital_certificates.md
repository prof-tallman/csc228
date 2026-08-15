# Digital Certificates and Certificate Authorities #

This lesson introduces digital certificates and certificate authorities through a physical wax-seal analogy. Students work in groups to create and verify signed messages, then discover that a valid signature does not necessarily prove the identity of the signer.

Students should already understand symmetric and public-key cryptography and basic digital signatures. However, the lesson works better if students do not have prior knowledge of certificate authorities.

The central question is:

> **How do I know that a public key really belongs to the person or organization it claims to represent?**

A planned visit from an impostor pretending to be the university president (or another well-known figure) exposes this weakness. The class then adds a trusted authority to verify the connection between an identity and its public key, providing a bridge to digital certificates, certificate authorities, root certificates, and HTTPS.

## Timing ##

This lesson is designed to take one hour. The wax sealing activity introduces a few minutes of variation. If time becomes tight, reduce the number of messages exchanged rather than cutting the certificate-authority portion. The identity problem and its solution are the central purpose of the activity.

| Section                        |           Time |
| ------------------------------ | -------------: |
| Introduction                   |      5 minutes |
| Original Wax-Seal Activity     |     15 minutes |
| The Identity/Imposter Problem  |     10 minutes |
| Certificate Authority Activity |     10 minutes |
| Connection to HTTPS            |     10 minutes |
| Conclusion                     |      5 minutes |
| **Total**                      | **55 minutes** |

## Learning Goals ##

By the end of the lesson, students should be able to:

- explain why a valid public key does not by itself establish identity;
- describe how a digital signature provides evidence of integrity and possession of a private key;
- explain how a digital certificate associates an identity with a public key;
- describe the role of a certificate authority;
- explain the purpose of trusted root certificates;
- distinguish between establishing a secure connection to a domain and determining whether that domain is the one the user intended to visit.

## Materials ##

For each group:

- One wax seal stamp (the stamps used by each group should have visibly distinct designs.)
- Sealing wax and supplies to melt the wax
- Message paper
- Notecards to sign the messages
- Pens or pencils

For the instructor:

- A different wax seal to represent the certificate authority (be sure to keep separate from the student seals)
- A reserved portion of the whiteboard for students to draw their seals
- Blank paper or cards for certificates
- Wax-sealing supplies
- An accomplice willing to impersonate the university president (coordinate this fake-president interruption the person)

The fake-president demonstration should occur after students have successfully used the peer directory but before the certificate-authority solution is introduced.

## Teacher Notes ##

The most important sentence in the lesson is:

> **The signature can be valid even though the identity is false.**

Do not spend too much time on the mechanical weaknesses of wax itself. Those are acknowledged limitations of the analogy. Likewise, avoid turning the lesson primarily into a discussion of certificate revocation or historical CA compromises. These are useful follow-up topics, but the central idea is the connection between identity and public key.

If the class is running long, shorten the first signing exercise. Do not omit the fake-president demonstration, CA certificate step, or final translation to HTTPS.

## Introduction

Begin with a brief review of digital signatures. Remind students that a signature can help establish that a message has not been altered and that it was signed using the expected private key.

Then pose the question:

> Suppose someone gives you a public key and says, "This belongs to the president of the university." How do you know?

Do not answer the question yet. Instead, tell students that they will build a simple signing system and see whether it solves the problem.

[**Link to Wax Seal Activity**](digital_certificate_activity/activity_who_do_you_trust.md)

## Transition

Once students have successfully exchanged and verified messages, shift the discussion from verifying a signature to verifying an identity.

Introduce the planned visit from an impostor claiming to be the university president. After students recognize the deception, connect it to the class's public directory: an impostor could publish their own seal under someone else's name and then produce signatures that verify correctly.

Emphasize the key distinction:

> **The cryptography can work perfectly while the identity information is wrong.**

Ask how the class could prevent someone from falsely claiming another person's identity. Use their responses to introduce the need for a trusted authority that verifies the connection between an identity and its public key.

The instructor then acts as the certificate authority by signing a record that connects each group's identity to its public seal information. This record represents a digital certificate.

## Conclusion

Bring the class back together by translating the wax-seal system into the real certificate system.

| Classroom Activity               | Internet System       |
| -------------------------------- | --------------------- |
| Metal wax stamp                  | Private key           |
| Public seal information          | Public key            |
| Simple message summary           | Cryptographic hash    |
| Sealed hash                      | Digital signature     |
| Record connecting group and seal | Digital certificate   |
| Instructor                       | Certificate authority |
| Instructor's seal                | CA digital signature  |
| Existing trust in instructor     | Trusted root          |

Explain that a public key alone does not prove who owns it. A digital certificate connects an identity, such as a domain name, to a public key, and a certificate authority signs that claim. But who verifies the certificate authority?

Explain that browsers and operating systems begin with a collection of trusted root certificates. These provide the starting point for the chain of trust. Organizations may also install their own trusted roots on systems they manage.

A computer can be securely connected to a website but that doesn't mean it is the website the user intended to visit. A phishing site may have a completely valid HTTPS certificate for a deceptive domain. The certificate system can therefore work exactly as intended even when the user has been tricked into visiting the wrong site.

## Limits of the Analogy ##

The wax-seal activity is intended to model the relationships among keys, signatures, identity, and trust. It does not reproduce the cryptographic mathematics.

### Public and Private Keys ###

A real public-key system has two mathematically related but distinct keys. The wax system has only one physical object. In this activity, the metal stamp was the private key and the public drawing of the stamp's recognizable design represents the public information used for verification. But the drawing is not literally equivalent to a public key. Students should imagine that anyone can use the public information to recognize a valid impression, but cannot use that information to work backwards to manufacture the private stamp.

### Duplicate Wax Seals ###

Real wax seals can be copied, purchased, or manufactured. Assume for the activity that every group's stamp is unique and impossible to duplicate. Properly generated cryptographic keys are drawn from such an enormous number of possibilities that accidental duplication is treated as effectively impossible. Public-key systems are also designed so that recovering the private key from the public key is computationally impractical.

### Classroom Hashes ###

Smmaries, word counts, and character counts are poor substitutes for cryptographic hashes. They were used because the students could calculate them quickly by hand. As learned previously, real cryptographic hash functions have much stronger properties.

## Attribution and Acknowledgements ##

The original wax-seal idea in this activity was inspired by a brief lesson summary from [Flip Educaiton](https://flipeducation.ai/curriculum/ca/computer-science/grade-12/digital-signatures-and-certificates/activities#activity-1). Their brief summary provided the initial spark for using physical seals to illustrate digital signatures; Prof. Tallman developed the lesson itself separately and then used GenAI to convert his activity into this lesson plan format.