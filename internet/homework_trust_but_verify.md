# Trust But Verify #

When you visit an HTTPS website, your browser does more than encrypt the connection. It also attempts to determine whether the server at the other end of that connection really belongs to the domain that you intended to visit. Digital certificates and Certificate Authorities help make that possible.

For this assignment, you will investigate a real website's digital certificate and follow its chain of trust from the website itself back to a trusted Root Certificate Authority. Choose a website that uses HTTPS. Try to choose something more interesting than Google or another site that everyone else is likely to investigate.

The goal of this assignment is not merely to locate a collection of certificate fields. By the end, you should be able to look at a secure website and answer a more important question:

> **Why does my computer believe that this public key really belongs to this website?**

## Part 1: Meet the Certificate ##

Open the digital certificate associated with your website. Depending on your browser and operating system, you may need to click through the browser's security information or use another certificate-viewing tool. Record the following information:

1. Website: What website are you investigating?

2. Subject: What information appears in the certificate's Subject field?

3. Subject Alternative Names: What hostnames, domains, or wildcard domains does the certificate identify as valid for this certificate?

4. Issuer: Who issued this certificate?

5. Validity: When did the certificate become valid, and when does it expire?

6. Serial Number: What is the certificate's serial number?

Include a screenshot showing the website certificate and however much of this information can fit on the screen.

## A Quick Guide to Modern Cryptography ##

You have already worked with RSA and AES in this course. When examining a real certificate, however, you may encounter several other cryptographic algorithms. Do not worry if your certificate contains an algorithm that we did not study in detail. Your job is to determine its general purpose: symmetric encryption, public-key cryptography, digital signatures, key agreement, or hashing.

You are not expected to understand the mathematics behind any of these algorithms. Instead, use the table below to help identify what you find and what role it plays.

| Algorithm | Type | What You Should Know |
| --------- | ---- | -------------------- |
| **AES** | Symmetric Cryptography | A widely used modern encryption algorithm. The same secret key is used for encryption and decryption. AES commonly uses 128-, 192-, or 256-bit keys. |
| **ChaCha20** | Symmetric Cryptography | A modern alternative to AES. It also uses a shared secret key, although its internal design is very different from AES. You may encounter ChaCha20 as part of a TLS connection, but it is not normally the public-key algorithm stored in a certificate. |
| **RSA** | Public-Key Cryptography | The public-key system studied in class. Its security is related to the difficulty of factoring very large numbers that are the product of large primes. RSA keys are commonly 2048 bits or larger. |
| **RSA-PSS** | Digital Signature | A modern method of creating digital signatures using RSA. The underlying public-key mathematics is still RSA; PSS describes how RSA is used to create and verify the signature. |
| **ECDSA** | Digital Signature | The Elliptic Curve Digital Signature Algorithm. It uses elliptic-curve cryptography to create digital signatures and can provide strong security with much smaller keys than RSA. |
| **Ed25519 / EdDSA** | Digital Signature | A newer family of elliptic-curve signature algorithms designed to provide strong security and efficient digital signatures. |
| **ECDH / ECDHE** | Key Agreement | Elliptic-curve versions of Diffie-Hellman. They allow two parties to establish a shared secret over an insecure network. These are key-agreement algorithms, not symmetric encryption algorithms or certificate signatures. |
| **SHA-256 / SHA-384 / SHA-512** | Hash Function | These algorithms create fixed-length digests from data. Hash functions are used as part of digital signatures and to create certificate fingerprints. They do not encrypt data and do not use an encryption key. |

## Part 2: The Cryptography Inside ##

A digital certificate contains a public key and is itself protected by a digital signature from a Certificate Authority. Investigate the cryptographic information in your certificate.

7. What algorithm is used for the website's public key?

8. If the algorithm has a meaningful key size, how large is the key? If the certificate instead identifies a named elliptic curve, record the name of the curve.

9. Find the actual public key or encoded public-key information. You do not need to copy the entire key into your report. Include a screenshot or copy a small portion that demonstrates that you found it.

10. What algorithm was used by the Certificate Authority to digitally sign the certificate?

11. What hash algorithm is associated with that signature, if one is listed?

12. Find a fingerprint calculated for the certificate, such as a SHA-256 fingerprint. What hash algorithm is used, and what is the fingerprint?

13. Explain the difference between (a) the website's public key, (b) the CA's digital signature on the certificate, and (c) the certificate's fingerprint. Your explanation does not need to be long, but it should make clear that these are three different things with three different purposes.

## Part 3: Who Says We Should Trust Them? ##

Your website did not simply create a certificate that your browser decided to trust. Its certificate is part of a certificate chain.

14. Find the certificate chain for your website. For each certificate in the chain, identify:
   - the subject or owner of the certificate (who is it for),
   - the issuer (on whose authority),
   - and whether it is the website certificate, an Intermediate CA certificate, or a Root CA certificate.

You may organize this information as a short list or simple diagram. For example: `Website → Intermediate CA → Root CA` (although your actual chain may contain more certificates). Include a screenshot showing the certificate chain if your software provides one.

## Part 4: Find the Root ##

Follow the certificate chain until you identify the Root Certificate Authority that serves as the trust anchor.

15. What is the name of the Root Certificate Authority?

16. Who issued the Root CA's certificate?

17. How is that different from the website certificate you examined earlier?

18. When does the Root CA certificate expire?

19. Find this Root CA in the trusted certificate store on your own computer, if possible. Include a screenshot showing it there.

On Windows, you may be able to find trusted roots through the Windows certificate-management tools. On macOS, you can investigate trusted certificates through Keychain Access. Your browser may also provide access to certificate or trust information.

## Part 5: Why Does Your Computer Believe It? ##

Now put the pieces together. Suppose an attacker creates a fake certificate claiming to belong to the website you investigated. The fake certificate contains the correct website name and the attacker's own public key.

20. In a short paragraph, explain why your browser would not normally accept that certificate simply because the name looks correct. Your explanation should use what you discovered in this assignment. In particular, consider:
   - the website's public key,
   - digital signatures,
   - the certificate chain,
   - and the trusted root certificates already installed on your computer.

The goal is to explain how your browser moves from:

> **"This certificate claims to belong to this website."**

to:

> **"I have a cryptographic reason to trust that claim."**