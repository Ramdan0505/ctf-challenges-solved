# Diffie-Hellman

**Platform:** Virginia Cyber Range – Cloud CTF  
**Category:** Cryptography  
**Difficulty:** Medium  
**Topic:** Diffie–Hellman key exchange  

## Objective
Compute the Diffie–Hellman shared secret using the provided parameters.

## Challenge Data
- (p, g) = (799, 876)
- Alice: 14
- Bob: 99

## Initial Analysis
This challenge uses small integers, indicating a simplified Diffie–Hellman setup.
The values shown for Alice and Bob are treated as the private exponents `a` and `b`.

In Diffie–Hellman, the shared secret is:

s = g^(a*b) mod p

## Computation (Python)

```python
p = 799
g = 876
a = 14
b = 99

s = pow(g, a*b, p)
print(s)
