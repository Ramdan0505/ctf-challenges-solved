# hsabtA

**Platform:** Virginia Cyber Range – Cloud CTF  
**Category:** Cryptography  
**Difficulty:** Easy  
**Cipher:** Atbash  

## Objective
Decrypt the provided ciphertext to recover the flag in the format `CCT_CTF{...}`.

## Challenge Data

**Ciphertext:**
ZGYZHSRHHHRNKOVYFGVZHBGIYIVZP

## Initial Analysis
The challenge title is `hsabtA`, which is **“Atbash” reversed**—a strong indicator that the cipher is Atbash.  
The ciphertext is uppercase A–Z only, consistent with a monoalphabetic substitution cipher.

---

## Cipher Identified
**Atbash Cipher**

Atbash is a simple substitution cipher that maps each letter to its reverse:
- A ↔ Z  
- B ↔ Y  
- C ↔ X  
- …  

## Decryption Process (Python)

```python
import string

alphabet = string.ascii_uppercase
atbash = alphabet[::-1]
table = str.maketrans(alphabet, atbash)

ciphertext = "ZGYZHSRHHHRNKOVYFGVZHBGIYIVZP"
plaintext = ciphertext.translate(table)

print(plaintext)
