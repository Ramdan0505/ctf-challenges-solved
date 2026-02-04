# appleappleapple

**Platform:** Virginia Cyber Range – Cloud CTF  
**Category:** Cryptography  
**Difficulty:** Easy–Medium  
**Cipher:** Vigenère  


## Objective
Decrypt the provided ciphertext to recover the hidden flag in the format `CCT_CTF{...}`.



## Challenge Data

**Ciphertext:**
AcPatItPOeyZtptsIWpHorizvsPllc

markdown
Copy code

**Hint / Flavor Text:**
> “Mmmm I like apples in my vinegar”

**Challenge Title:**
appleappleapple



## Initial Analysis
The ciphertext consists solely of alphabetic characters with mixed casing, which suggests a classical substitution cipher rather than an encoding scheme (e.g., Base64 or hex).

The flavor text references **“vinegar”**, which strongly hints at the **Vigenère cipher**. This is a common CTF clue, as “vinegar” is a phonetic play on *Vigenère*.

Additionally, the challenge title repeats the word **“apple”**, indicating that it is likely the encryption key.



## Cipher Identified
**Vigenère Cipher**

- Polyalphabetic substitution cipher
- Uses a repeating keyword to shift characters
- Commonly appears in introductory cryptography challenges



## Key Identification
Based on the challenge title:

appleappleapple

The repeating nature implies the key is simply:

apple

## Decryption Process

The ciphertext was decrypted using a Vigenère cipher with the key `apple`.

### Python Decryption Script

def vigenere_decrypt(ciphertext, key):
    result = ""
    key = key.lower()
    key_index = 0

   for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = (
                (ord(char) - offset - (ord(key[key_index % len(key)]) - ord('a'))) % 26
            ) + offset
            result += chr(decrypted_char)
            key_index += 1
        else:
            result += char

  return result

ciphertext = "AcPatItPOeyZtptsIWpHorizvsPllc"
print(vigenere_decrypt(ciphertext, "apple"))
