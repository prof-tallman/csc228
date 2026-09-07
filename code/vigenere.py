#!/usr/bin/env python
# encoding: utf-8

"""
   @author: Joshua Tallman
  @license: MIT Licence
  @contact: joshua.tallman@cui.edu
     @file: vigenere.py
     @time: 2020-05-19 09:15
"""

# For encrypting and decrypting text with the Vigenere Cipher. Also includes
# several functions to assist with cryptanalysis.


import caesar as _caesar
import queue as _queue


def _get_space_positions(text):
    """ Returns a list containing the index of every space ' ' in a string.
    """
    space_positions = {}
    for pos in range(len(text)):
        if not text[pos].isalpha():
            space_positions[pos] = text[pos]
    return space_positions


def _insert_spaces(text, space_positions):
    """ Inserts spaces ' ' into a string at each index given in the list.
    """
    for pos, value in space_positions.items():
        text = text[:pos] + value + text[pos:]
    return text


def _get_shift_factor(ch):
    """ Returns the base-0 ordinal of a letter (A->0, B->1, C->2, ...).
    """
    return ord(ch.lower()) - ord('a')



def encrypt(plaintext, keyword):
    """ Encrypts a text with the Vigenere Cipher using the given keyword. By
        defualt, spaces in the plaintext are preserved. """
    
    # Repeat the keyword over and over again so that we have a key that is the
    # same length as the text itself.
    # "key" ==> [k, e, y, k, e, y, k...]
    key = [keyword[i%len(keyword)] for i in range(len(plaintext))]

    # Convert the key into a series of shift amounts; e.g.,
    # [k, e, y, k, e, y, k...] ==> [-11, -5, -25, -11, -5, -25, -11, ...]
    shifts = [-_get_shift_factor(k) for k in key]

    # We encrypt the plaintext by using the shift amounts as a series of keys
    # to the the basic Caesar Shift Cipher.
    shift_index = 0
    ciphertext = []
    for ch in plaintext:
        if ch.isalpha():
            ciphertext += _caesar.encrypt(ch, shifts[shift_index])
            shift_index += 1
        else:
            ciphertext += ch
    ciphertext = ''.join(ciphertext).upper()

    return ciphertext


def decrypt(ciphertext, keyword):
    """ Decrypts a text with the Vigenere Cipher using the given keyword.
    """

    # Repeat the keyword over and over again so that we have a key that is the
    # same length as the text itself.
    # "key" ==> [k, e, y, k, e, y, k...]    
    key = [keyword[i%len(keyword)] for i in range(len(ciphertext))]

    # Convert the key into a series of shift amounts; e.g.,
    # [k, e, y, k, e, y, k...] ==> [11, 5, 25, 11, 5, 25, 11, ...]
    shifts = [-_get_shift_factor(k) for k in key]

    # We decrypt the ciphertext using the shift amounts as a series of keys
    # to the the basic Caesar Shift Cipher.
    shift_index = 0
    plaintext = []
    for ch in ciphertext:
        if ch.isalpha():
            plaintext += _caesar.decrypt(ch, shifts[shift_index])
            shift_index += 1
        else:
            plaintext += ch    
    plaintext = ''.join(plaintext).lower()

    return plaintext


def show_encrypt(plaintext, keyword):
    print(f"\n   {_caesar.english_alphabet.lower()}")
    for letter in keyword.upper():
        index = _caesar.english_alphabet.upper().index(letter)
        alphabet = _caesar.encrypt(_caesar.english_alphabet.upper(), -index)
        print(f"{letter}: {alphabet}")

    ciphertext = encrypt(plaintext, keyword)
    print(f"\n{plaintext}\n")
    print(f"{ciphertext}\n")


def show_decrypt(ciphertext, keyword):
    print(f"\n   {_caesar.english_alphabet.lower()}")
    for letter in keyword.upper():
        index = _caesar.english_alphabet.upper().index(letter)
        alphabet = _caesar.encrypt(_caesar.english_alphabet.upper(), -index)
        print(f"{letter}: {alphabet}")

    plaintext = decrypt(ciphertext, keyword)
    print(f"\n{ciphertext}\n")
    print(f"{plaintext}\n")


def sequence_lists(text, count):
    """ Finds the index of all count-length sequences in the ciphertext and
        returns them in a dictionary. Used for cryptanalysis. All sequences are
        returned, but only repeated sequences have value.
        For a text of "ABCDABCD" and sequence length of 3, the function returns
          { "ABC":[0,4], "BCD":[1,5], "CDA":[2], "DAB":[3] }
    """
    sequences = {}
    lastIndex = len(text)-count
    for i in range(lastIndex+1):
        s = text[i:i+count]
        sequences[s] = sequences.get(s, [])
        sequences[s].append(i)
    return sequences


def sequence_span_lengths(sequences):
    """ Finds the space between each repeated sequence. Input is a dictionary
        of all sequences, as obtained from the `sequence_lists` function.
        Returns a dictionary with the sequence as the key and each span length
        as an element in a list. Used for cryptanalysis.
        For input { "ABC":[0,4], "BCD":[1,5], "CDA":[2], "DAB":[3] }, it returns
          { "ABC":[4], "BCD":[4] }
    """
    # Filter sequences that only appear once
    sequences = { seq:idx for seq, idx in sequences.items() if len(idx) > 1}
    # Calculate the spans between each sequence
    spans = {}
    for s, indices in sequences.items():
        last = len(indices)-1 # to account for forward looking calculation
        spans[s]  = [(indices[i+1]-indices[i]) for i in range(last)]
    return spans


def _get_factor_list(n):
    """ Returns a list of all the factors for a number
    """
    return [i for i in range(2, n//2+1) if n % i == 0] + [n]


def sequence_length_factors(span):
    """ Calculates the factors for each provided sequence span length. Input is
        a dictionary of all sequences and their span length, as obtained from
        the `sequence_span_lengths` function. Returns a dictionary with them
        sequence as the key and a list of the factors. Note that 1 is omitted
        as a factor). Used for cryptanalysis.
        For input { "ABC":[4], "BCD":[4] }, it returns
          { "ABC":[2,4], "BCD":[2,4] }
    """
    factorLists = {}
    for spanSequence, spanLengthList in span.items():
        for spanLength in spanLengthList:
            if spanSequence not in factorLists:
                factorLists[spanSequence] = set(_get_factor_list(spanLength))
            else:
                factorLists[spanSequence].update(_get_factor_list(spanLength))
        factorLists[spanSequence] = sorted(list(factorLists[spanSequence]))
    return factorLists


def find_common_factors(factors):
    """ Finds the common factors within multiple groups of factors. Input is a
        dictionary of sequences and all the factors of their span length.
        Returns a list of any factors that are common to all sequences. Used for
        cryptanalysis.
        For input { "ABC":[2,4], "BCD":[4] }, it returns [4]
    """
    commonFactors = []
    allFactors = {f for factorList in factors.values() for f in factorList}
    for factor in allFactors:
        if all(factor in factorList for factorList in factors.values()):
            commonFactors.append(factor)
    return commonFactors


def split_ciphertext_by_key_length(ciphertext, key_length):
    """ Divides a Vigenere ciphertext into separate sub-ciphertexts, one for
        each letter of the key. Returns a list of sub-ciphertexts. There will
        be `key_length` number of sub-texts. Each sub-text corresponds to a
        different letter in the key. Used for cryptanalysis.
        For input "ABCDABCD" key_length=3, it returns [ "ADC", "BAD", "CB" ]
    """
    textList = [""] * key_length
    for startIndex in range(key_length):
        for idx in range(startIndex, len(ciphertext), key_length):
            textList[startIndex] += ciphertext[idx]
    return textList


def top3(subtext):
    """ Calculates the three most likely Vigenere shift factors for a group of
        subtext. Returns the shift facts as a list of tuples, each tuple having
        a score and the letter that corresponds to the shift factor.
        For example: [(48.5, 'P'), (459.6, 'E'), (468.6, 'A')]
    """
    q = _queue.PriorityQueue()
    scores = _caesar.score_all_keys(subtext)
    for i, score in scores.items():
        keyLetter = chr(i + ord('A'))
        q.put((round(score, 1), keyLetter))
    if q.qsize() != 26:
        err = "Error: Expected 26 scores but got {0}"
        raise IndexError(err.format(q.qsize()))
    return [q.get(), q.get(), q.get()]
