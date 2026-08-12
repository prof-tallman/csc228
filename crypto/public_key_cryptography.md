# Public Key Cryptography #

## Asymmetric Cryptography ##

Modern symmetric cryptography is extraordinarily powerful, but it creates an important practical difficulty: two people must somehow share a secret password or key before they can exchange encrypted messages. For instance, in a previous assignment, you used GNU Privacy Guard (GPG) to encrypt and decrypt files using AES and a password. Anyone who knew the password could decrypt the message. But what if two people wanted to communicate securely but did not share a common password?

Public key cryptography provides a different approach. Rather than using one shared secret, each person creates two related keys:

- A public key, which may be given to other people.
- A private key, which must remain secret.

Other people use your public key to encrypt messages intended for you. You use your private key to decrypt those messages. To send an encrypted message to another person, you need a copy of that person's public key. A public key can be distributed to other people without giving them the ability to read messages encrypted for you.

In this assignment, you will use GPG to generate your own public/private key pair. You will send your public key to Prof. Tallman, receive and decrypt a message encrypted for you, import Prof. Tallman's public key, and send him an encrypted message in return.

## GNU Privacy Guard ##

GNU Privacy Guard is a freely available cryptography toolkit that you previously used to perform AES encryption and cryptographic hashing. Reuse it for public key cryptography. Install GPG on your computer using a trustworthy source appropriate for your operating system. If you already installed GPG for the previous assignment, continue using that installation. Focus on the command-line version of GPG, as shown below.

### Generating Your Public and Private Keys ###

Open a terminal or command prompt and generate a new public/private key pair:

```
gpg --full-generate-key
```

Follow the prompts carefully:

- You may accept the recommended default key type and size.
- Set the key to expire after a reasonable amount of time, such as one year.
- Enter your real name and Eagles email address.
- Create a passphrase that you can remember for the duration of this assignment. Your passphrase protects your private key on your computer. Do not forget it.

After generating your key pair, list the public keys stored in your GPG keyring. You should see an entry containing your name and email address.

```
gpg --list-keys
```

### Protecting Your Private Key ###

Your public key is intended to be shared. Your private key is not. Do not send your private key to anyone, including Prof. Tallman. Do not upload your private key to Canvas. Do not share the passphrase protecting your private key with anyone.

For this assignment, you will submit only an exported copy of your public key. An exported public key file begins with text similar to this:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
```

In contrast, a private key file would contain text similar to this:

```
-----BEGIN PGP PRIVATE KEY BLOCK-----
```

If you see the words `PRIVATE KEY BLOCK`, do not submit or send that file.

### Sharing Your Public Key ###

Export your public key in a text-based format that Prof. Tallman can import. Replace the email address in the following command with the email address associated with your GPG key:

```
gpg --armor --output name_public_key.asc --export your.email@eagles.cui.edu
```

Open the exported file in a text editor and verify that it begins with:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
```

1. Submit your exported public key file to Prof. Tallman and he will use it to encrypt a short message for you.

### Decrypting a Message from Prof. Tallman ###

After you submit your public key, Prof. Tallman will send you an encrypted file. This file has been encrypted using your public key. Save the encrypted file to a folder and decrypt it using GPG. GPG may ask for the passphrase that protects your private key.

```
gpg --decrypt --output plaintext.txt ciphertext.txt
```

Open the resulting plaintext file and record the message that you recovered. You will include it in your encrypted response to Prof. Tallman.

2. What key did Prof. Tallman use to encrypt the message sent to you?
3. What key did you use to decrypt the message?
4. Why would another student be unable to decrypt the message sent to you merely by obtaining a copy of your public key?
5. What would happen if you lost your private key or forgot the passphrase protecting it?

### Importing Prof. Tallman's Public Key ###

To send an encrypted message to Prof. Tallman, you must first obtain his public key. Download the public key file provided by Prof. Tallman and import it into your GPG keyring:

```
gpg --import tallman_public_key.txt
```

You can confirm the import worked correctly using the following command:

```
gpg --list-keys his.email@cui.edu
```

You now have a public key that allows you to encrypt a message intended for Prof. Tallman.

### Sending an Encrypted Message to Prof. Tallman ###

Encrypt a message to Prof. Tallman using his public key. Start by creating a plain text file using a simple editor such as Notepad (Windows) or TextEdit (macOS). Your message should contain your name and a short message to Prof. Tallman. Also copy-paste the plaintext message that reveals you received and decrypted the message from Prof. Tallman.
GPG may warn you that it cannot confirm whether this public key actually belongs to Prof. Tallman. For this assignment, proceed using the public key file that was provided to you. You will consider the significance of this warning in the reflection section.

```
gpg --encrypt --recipient his.email@cui.edu --armor --output to_tallman.txt my_message.txt
```

To verify that the encryption worked correctly, open the output file in a text editor. Submit the encrypted file to Prof. Tallman. He will use his private key to decrypt your message.

## Understanding Public Key Cryptography ##

After completing the public key encryption assignment, think about the overall security of the system.

6. In the previous AES assignment, you needed a shared password to encrypt and decrypt a file. How is the communication process different in this assignment?
7. Why is it safer to send your public key than a password, even though Prof. Tallman could use either to encrypt a confidential message?
8. Why would it be dangerous to send your private key to Prof. Tallman or upload it as part of your assignment submission?
9. Suppose Prof. Tallman sends you a second encrypted message using the same public key that you provided. Would you need a new private key to decrypt the second message? Explain your answer.
10. Your private key is protected by a passphrase. Why does the quality of this passphrase matter even though the encryption system itself is strong?

This assignment allowed you and Prof. Tallman to exchange confidential messages without first sharing a secret password. Assume, however, that another person wanted to interfere and exchange confidential messages with you in place of Prof. Tallman.

## Reflection Question ##

11. Describe one or more ways that the exchange could still go wrong even if the cryptographic algorithms themselves are strong and GPG works correctly. What could an attacker do? Do not limit your answer to protecting your private key or choosing a good passphrase. Think carefully about the entire communication process: creating keys, sending keys, receiving keys, encrypting messages, and deciding whom you are actually communicating with.

Avoid broad or shallow answers. Explain a specific possible weakness and reason carefully about what could happen. Assume that your readers will not have access to this assignment; your writing should include enough background and explanation to stand on its own.
