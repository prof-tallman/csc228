# Towards Modern Cryptography #

## Symmetric Cryptography ##

Modern cryptographic systems are more sophisticated than historic systems like the Caesar Shift Cipher, Vigenère Cipher, and the Enigma Machine. These historic systems were all examples of *symmetric cryptography* (also called *secret-key cryptography*) because the same secret was used for both encryption and decryption. Most modern encryption algorithms are still symmetric systems, although they have been improved to operate on binary data instead of letters and perform many rounds of substitution, transposition, and similar mathematical mixing operations. One of the most widely used modern symmetric algorithms is called the Advanced Encryption Standard (AES). In the future, we will explore *asymmetric cryptography* (or *public-key cryptography*), which uses one key for encryption and a different key for decryption.

Modern cryptography is extremely difficult to break mathematically and at the same time, it is generally easy to use correctly. Cryptography software is standardized and freely available. The tools are built directly into modern web browsers and can also be downloaded as separate programs. As a result, modern attacks often focus less on breaking the algorithm itself and more on malware, weak passwords, poor key management, and vulnerable aspects of human behavior. One particular free tool is called the GNU Privacy Guard. "GNU" is a collection of Unix-like software tools named with the clever recursive acronym "GNU’s Not Unix."

## GNU Privacy Guard (GPG) ##

GNU Privacy Guard (GPG) is a freely available cryptography toolkit that supports many modern encryption algorithms, including AES. You are not expected to become a GPG expert for this assignment. The goal is simply to use modern cryptographic tools and observe their behavior.

Install GPG on your computer using a trustworthy source appropriate for your operating system. Windows users may wish to install Gpg4win and macOS users probably want to install the GPG Suite (sometimes called "Mac GPG" on the [main website](https://www.gnupg.org/download/)). The main GPG website has links to the installation files. If you encounter difficulties, try troubleshooting with GenAI tools. Students are also encouraged to chat with classmates or schedule an appointment with the instructor.

### AES Encryption with GPG ###

Encrypt a simple text file with AES. Start by creating a plaintext text file named message.txt that contains a short message. Avoid using word processors like Microsoft Word and Apple's Pages because they will add extra formatting and might change the file name. Instead, create the plaintext file with a text editor like Notepad (Windows) or TextEdit (macOS). Then, use GPG to encrypt the file using AES. GPG will convert your password into an encryption key. Note that the following examples work with GPG version 2.5.x and are expected to continue with future versions of the tool.

```
gpg --armor --symmetric --cipher-algo AES256 --output ciphertext.txt message.txt
```

In GPG, "armor" means the output file will be formatted in a way that keeps it easy to read.

Next, to make sure that everything works, decrypt the encrypted file.

```
gpg --decrypt --output plaintext.txt ciphertext.txt
```

The final output file, `plaintext.txt`, should be exactly the same as the original message.

1. Did the encrypted text appear random or structured?
2. How difficult was this process compared to historical systems such as Enigma or Vigenère? Consider the tools available at each time period.
3. What happened when you entered the wrong password?
4. Why do modern cryptographic systems depend so heavily on password quality and password management?
5. What would be the full command to give the final output file a different name?
6. Why was it important to download GPG from a trustworthy source?

### AES Decryption with GPG ###

Decrypt the file provided by Prof. Tallman using the password that was distributed to the class.

7. What was the plaintext message?
8. How does sharing a password securely become a challenge in real-world cryptography?
9. Why is strong encryption not enough if passwords or keys are handled poorly?

## Cryptographic Hashing ##

Another important cryptographic tool is the hash function. Encryption is designed to provide privacy (confidentiality) by transforming plaintext into ciphertext that can later be reversed with the correct password or key. Hashing serves a different purpose. A cryptographic hash function is intentionally designed as a one-way operation that should not be reversible.

Instead of hiding information, cryptographic hashes are primarily used to verify data integrity. If two files, passwords, or messages produce the exact same hash value, the underlying data is almost certainly identical. Good hash functions also demonstrate the avalanche effect, meaning that even a tiny change to the original data should produce a dramatically different hash value. This makes cryptographic hashes extremely useful for tamper detection and file verification.

A cryptographic hash function converts data into a short, fixed-length value called a hash or digest. Good hash functions are deterministic, difficult to reverse, and highly sensitive to small input changes. There are many different hashing functions and some algorithms are better than others. One of the most common modern hash functions is called SHA-256, which stands for Secure Hash Algorithm 256.

To calculate a cryptographic hash, Windows users may use GPG or the built-in CertUtil program; macOS users may use GPG or the built-in shasum tool. For example:

```
gpg --print-md SHA256 message.txt
```

```
certutil -hashfile message.txt SHA256
```

```
shasum -a 256 message.txt
```

Use the SHA-256 cryptographic hash algorithm to compute the digest of a file. First, create a small text document using a text editor and compute its SHA-256 hash. Then modify exactly one character in the file, recompute the hash, and compare the results. What happens if you add a single character? What if you delete one?

10. What was the SHA-256 hash of your original file?
11. What was the SHA-256 hash after you made a minor change?
12. How similar were the resulting hashes?
13. What does this suggest about the avalanche effect?
14. Why is the avalanche effect useful in cybersecurity?
15. How would somebody use a cryptographic hash to help protect against somebody tampering with a file?

Remember that cryptographic hashes are extremely sensitive to tiny changes, including spaces, punctuation, capitalization, and hidden formatting characters. Even adding an extra blank line at the end of a file will completely change the hash.

## Modern Cryptography ##

Modern encryption algorithms such as AES and SHA-256 are considered extremely secure when used properly. However, attackers often target weak passwords, password reuse, phishing attacks, or careless human behavior instead of attacking the mathematics directly.

## Reflection Question ##

16. Briefly describe a modern technology or security system that appears secure mathematically or technically, but still depends heavily on human responsibility to function safely. What kinds of human behaviors weaken the system, and why do people continue making these mistakes even when they understand the risks?

Avoid broad or shallow answers. Focus on specific examples and explain your reasoning carefully. Assume that your readers will not have access to this assignment. Your writing should include enough background and explanation to stand on its own.
