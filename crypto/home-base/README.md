# Home Base

**Platform:** Virginia Cyber Range – Cloud CTF  
**Category:** Cryptography  
**Difficulty:** Easy  
**Technique:** Base64 decoding  

---

## Objective
Decode the provided encoded string to recover the hidden flag.

---

## Initial Analysis
The challenge provided a string composed of alphanumeric characters ending with `==`.
The hint specifically referenced the equal sign, which is commonly used as padding in
Base64-encoded data.

---

## Encoding Identified
**Base64**

Base64 encoding often uses one or two `=` characters as padding to ensure the encoded
output length is a multiple of four.

---

## Exploitation Steps
The string was decoded using the Base64 utility:

```bash
echo "Q0NUX0NURntzMWlwbDNfY3J5cHQwX2NoNGxsfQ==" | base64 -d
