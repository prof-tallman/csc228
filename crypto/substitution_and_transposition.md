# Substitution and Transposition #

## Cryptographic Operations ##

Cryptographic algorithms are based on two simple mathematical operations: substitution and transposition. Historic algorithms used simple techniques with letters that can easily be traced on paper or in somebody's head.

Two examples of substitution and transposition are the Caesar Shift Cipher and Rail Fence cipher. Information about these two operations and the corresponding ciphers can be found on Wikipedia and cryptography websites such as Crypto Corner ([Caesar Shift](https://crypto.interactive-maths.com/caesar-shift-cipher.html) and [Rail Fence](https://crypto.interactive-maths.com/rail-fence-cipher.html)).

1. Define *substitution* in your own words.
2. Define *transposition* in your own words.

For the following questions, assume that the following plaintext:

```
The quick brown fox jumps over the lazy dog.
```

For all encryption exercises:

* Preserve spaces and punctuation.
* Use the standard convention of converting all ciphertexts to uppercase and all plaintexts to lowercase.

## Caesar Shift Cipher ##

The Caesar Shift Cipher is based on shifting the entire alphabet by a set amount. It is often shown with a decoder wheel made with an inner and outer ring. The outer ring can spin, allowing the letters at the end of the alphabet to rotate back around to the beginning letters.

3. Use the Caesar Shift Cipher to encrypt the plaintext using a key of 7 shifts.
4. Take the resulting ciphertext and decrypt it.
5. Did the Caesar Shift Cipher use substitution or transposition?

## Rail Fence Cipher ##

The Rail Fence Cipher begins by splitting the plaintext into a series of rails by zig-zagging diagonally from the top to bottom. If the key is two, there will be two rails; if the key is three, there will be three rails; and so on. After the rails have been filled out, the cipher concatenates the letters from the top rail and then moves downward until reaching the last rail.

6. Use the Rail Fence Cipher to encrypt the plaintext using a key of 3 rails.
7. Take the resulting ciphertext and decrypt it.
8. Did the Rail Fence Cipher use substitution or transposition?

## Cryptanalysis ##

Two secret messages have been intercepted. One was encrypted with the Caesar Shift Cipher and the other Rail Fence Cipher, however it is not clear which is which.

9. Determine which ciphertext corresponds to which cipher and then crack both messages by decrypting them without knowing the key.

```
TI SM OMN-ESRN N ORGOS ONTB FADO ICUAE.FRTELR ORGDI IHYUWEEE O OHSI YCMADB TOGADCUAEU!D O EARI RDSORGD O H ODYU O SWT O HRVRYUG.
```

```
JSV KSH LEW RSX KMZIR YW E WTMVMX SJ JIEV ERH XMQMHMXC, FYX SJ TSAIV, PSZI, ERH WIPJ-HMWGMTPMRI.
```

## Modern Algorithms ##

Most modern algorithms are still based on substitution and transposition, but they apply these operations to binary data. Each operation on its own remains reasonably straightforward, but together the overarching algorithm can become quite complex and difficult to understand.

## Reflection Question ##

Briefly describe (a) how you determined which algorithm corresponded to which ciphertext; (b) the technique that you used to crack the Caesar Shift Cipher; and (c) crack the Rail Fence Cipher. Each portion of the answer (A-C) should be a well-formed paragraph. Assume that your readers will not have access to this assignment, so your writing should include a brief introduction and enough explanation to stand on its own.
