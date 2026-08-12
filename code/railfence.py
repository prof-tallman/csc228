#!/usr/bin/env python
# encoding: utf-8

"""
   @author: Joshua Tallman
  @license: MIT Licence
  @contact: joshua.tallman@cui.edu
     @file: railfence.py
     @time: 2026-08-12 10:00
"""

# For encrypting and decrypting text with the Railfence Cipher. The purpose of
# this code is to help students understand the transposition process.


def encrypt(plaintext, key=2):
    """ Encrypts using the Railfence Cipher with the given key
    """  
    rails = [ '' ] * key
    direction = 1         # takes values +/-1 to move up and down the fence
    curr = 0              # keep track of the current rail

    # Step through each letter in the plaintext one at a time
    for letter in plaintext:

        # Adds the next letter to the current rail
        rails[curr] += letter

        # Moves on to the next rail
        if curr == 0:
            direction = 1
        elif curr == key - 1:
            direction = -1
        curr += direction

    return ''.join(rails)


def encrypt_show_rails(plaintext, key=2):
  """ Returns an list of the rails that would be used in encryption. The rails
      are constructed with spaces to make them line up visually. Underscores
      replace the spaces to make it easier to see.
  """
  visual_rails = [ '' ] * key
  direction = 1
  curr = 0

  # Step through each letter in the plaintext one at a time
  for letter in plaintext.replace(' ', '_'):
  
    # Adds the next letter to the current rail. This extra step with the spaces
    # creates the visual zig-zag rails by adding spaces to the unused rails.
    for i in range(key):
      if i == curr:
        visual_rails[i] += letter
      else:
        visual_rails[i] += ' '

    # Moves on to the next rail
    if curr == 0:
      direction = 1
    elif curr == key - 1:
      direction = -1
    curr += direction

  return visual_rails


def _rail_counts(text, key=2):
  """ Returns the number characters on each rail as a list.
  """
  rail_counts = [ 0 ] * key
  direction = 1
  curr = 0

  # Step through each letter in the plaintext one at a time
  for _ in text:
    rail_counts[curr] += 1

    # Moves on to the next rail
    if curr == 0:
      direction = 1
    elif curr == key - 1:
      direction = -1
    curr += direction

  return rail_counts


def show_rail_lengths(text, key=2):
    """ Returns the number characters on each rail as a list.
    """
    visual_counts = [ '' ] * key
    direction = 1
    curr = 0

    # Step through each letter in the plaintext one at a time
    for _ in text:

        # Adds the next letter to the current rail. This extra step with the spaces
        # creates the visual zig-zag rails by adding spaces to the unused rails.
        for i in range(key):
            if i == curr:
                visual_counts[i] += '*'
            else:
                visual_counts[i] += ' '        

        # Moves on to the next rail
        if curr == 0:
            direction = 1
        elif curr == key - 1:
            direction = -1
        curr += direction

    return visual_counts
   


def ciphertext_to_rails(ciphertext, key=2):
    """ Divides the ciphertext into rails for the given key
    """
    rails = [ '' ] * key

    # Determines how many characters belong to each rail
    counts = _rail_counts(ciphertext, key)

    # Extract the substrings for each rail
    start_idx = 0
    for i in range(key):
        end_idx = start_idx + counts[i]
        rails[i] = ciphertext[start_idx:end_idx]
        start_idx += counts[i]

    return rails


def decrypt(ciphertext, key=2):
    """ Decrypts using the Railfence Cipher with the given key
    """
    steps = [ 0 ] * key
    direction = 1
    rail_idx = 0

    # Divide the ciphertext up into the different rails
    raw_rails = ciphertext_to_rails(ciphertext, key)

    # Create the plaintext one letter at a time
    plaintext = ''
    for _ in ciphertext:

        # Get the next plaintext letter, moving zig-zag along the rails. The
        # inner rails are longer and move faster than outer rails
        letter_idx = steps[rail_idx]
        plaintext += raw_rails[rail_idx][letter_idx]

        # Moves on to the next rail
        if rail_idx == 0:
            direction = 1
        elif rail_idx == key - 1:
            direction = -1

        # Handle the wierd stepping due to zig-zag nature of rails...            
        steps[rail_idx] += 1
        rail_idx += direction
    return plaintext


def decrypt_show_rails(ciphertext, key=2):
    """ Returns an list of the rails that would be used in decryption. The rails
        are constructed with spaces to make them line up visually. Underscores
        replace the spaces to make it easier to see.
    """
    steps = [ 0 ] * key
    direction = 1
    rail_idx = 0

    # Divide the ciphertext up into the different rails
    raw_rails = ciphertext_to_rails(ciphertext, key)
    visual_rails = [ '' ] * key

    # Create the visual rails one letter at a time
    for _ in ciphertext:

        # Adds the next letter to the current rail. This extra step with the spaces
        # creates the visual zig-zag rails by adding spaces to the unused rails.
        for i in range(key):
            if i == rail_idx:
                letter_idx = steps[rail_idx]
                letter = raw_rails[rail_idx][letter_idx]
                visual_rails[i] += letter
            else:
                visual_rails[i] += ' '

        # Moves on to the next rail
        if rail_idx == 0:
            direction = 1
        elif rail_idx == key - 1:
            direction = -1

        # Handle the wierd stepping due to zig-zag nature of rails...            
        steps[rail_idx] += 1
        rail_idx += direction

    return visual_rails
