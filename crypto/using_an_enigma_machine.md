# Using an Enigma Machine #

## Enigma Components ##

The German Enigma machine looks and operates something like a typewriter. It has a keyboard with a mechanical and electrical system underneath each key. But unlike a typewriter, Enigma does not press ink onto paper, instead each key press turns on a light that is hidden behind a letter. The glowing letter would then be written down or transmitted by radio or telegram.

Every time a key was pressed, the gears in the Enigma machine rotated so that the next key, even if it was the exact same key, would light up a different lamp. There was no backspace. If a major error was made, the operator would start all over again at the beginning of the message.

The cryptographic innards of an Enigma machine were a collection of rotating scramblers, a single stationary reflector disc, and a plugboard. The original machines used three scramblers but later versions required four. The plugboard swapped any two letters with patch cables.

When a key was pressed, the electrical signal travelled through the system such that it passed through the scramblers from right to left, "bounced" off the reflector, went back through the scramblers (this time from left to right), and then passed through the plugboard. It was truly an ingenious system and one that took Allied Forces years of effort to defeat. But cracking the system gave the Allies a significant advantage and likely shortened the war by several years.

## Encrypting With Enigma ##

The Nazis had a very specific way to use Enigma machines. Headquarters would send a code book every month that would contain a code for each day. This daily code provided the order of the scramblers. It gave the orientation of the rings that covered each scrambler and which letter should be facing on top. It also identified the reflector and the settings for plugboard cables.

Once the Enigma machine was configured with the daily settings, the cryptographer would choose a random, three-letter key for each individual message. He would type the three letters twice in a row, recording the six letters that lit up on the lamp board. These six letters formed the beginning of his message (for the four-rotor version of Enigma, he would choose a four-letter random message key, type it twice, and there would be eight letters formed).

Next, he would reset the scramblers by rotating them so that the letters on top were the three (or four) letters that he had chosen for the random message key. At this point, the Enigma machine was fully configured and the cryptographer would type out the true secret message, one letter at a time, transmitting the ciphertext letters that appeared on the lamp board.

1. Encrypt a message with an Enigma machine simulator and send it to a partner. Set the daily key to the settings in your daily code book. Choose your own random message key. Send the six-letter encrypted message key and the full ciphertext to your partner.

## Decrypting With Enigma ##

One remarkable property of Enigma was that the same machine configuration would encrypt and decrypt messages. The only difference involved the first six letters of the ciphertext. Upon receiving a secret message, the Enigma operator would set the scramblers, reflector, and the plugboard to the daily key settings (the same configuration used by the message sender). He would type in the first six letters, taking special note of the plaintext. If the received message was authentic, the first three letters should match the next three letters, something like ABC ABC, since these letters formed the "random" and repeated message key chosen by the sender.

Armed with the random message key, the recipient would rotate the scramblers until the random letters were on top. Once this was done, Enigma was ready to decrypt the rest of the plaintext. The operator would type each key of the ciphertext and read the plaintext from each lamp.

2. Decrypt a message with an Enigma machine simulator as received from a partner. Use the daily encryption key to configure the machine. Decrypt the first six letters, verify that the three letters repeat, and then reset the machine for the rest of the message.

## Enigma Machines Today ##

Although a working mechanical Enigma machine might not be readily available to students, there are several freely available online simulators. Consider any of these websites:

* [GCHQ's Cyber Chef](https://gchq.github.io/CyberChef/#recipe=Enigma('3-rotor','LEYJVCNIXWPBQMDRTAKZGFUHOS','A','A','EKMFLGDQVZNTOWYHXUSPAIBRCJ%3CR','A','A','AJDKSIRUXBLHWTMCQGZNPYFVOE%3CF','A','A','BDFHJLCPRTXVZNYEIWGAKMUSQO%3CW','A','A','AY%20BR%20CU%20DH%20EQ%20FS%20GL%20IP%20JX%20KN%20MO%20TZ%20VW','',true)) (probably the most authoritative source)
* [101 Computing's Simulator](https://www.101computing.net/enigma-machine-emulator/) (definitely the most fancy looking)
* [Daniel Pallok's Enigma Website](https://people.physik.hu-berlin.de/~palloks/js/enigma/enigma-u_v262_en.html) (a well done hobbyist website)

There are a handful of Enigma machines in museums that still work and are sometimes even available for visitors to use. Prof. Tallman had the privilege of typing on a working machine at the National Cryptologic Museum in Maryland. Enigmas are occasionally available for auction, although a working machine often costs tens of thousands of dollars.

## Reflection Question ##

During World War II, the Enigma machine gave governments powerful new ways to communicate securely and coordinate warfare. Modern technologies similarly give ordinary people abilities that previous generations could barely imagine.

Describe a modern technology that you believe people have adopted without fully understanding its consequences. What makes it difficult to use this technology wisely?

Avoid broad or shallow answers. Focus on examples and explain how the technology affects human behavior, relationships, institutions, or moral decision making. Consider both the opportunities and the risks created by the technology.
