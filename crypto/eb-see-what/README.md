# Eb-see-what?!?

**Platform:** Virginia Cyber Range – Cloud CTF  
**Category:** Cryptography  
**Difficulty:** Medium  
**Encoding:** EBCDIC (IBM cp037)

## Objective
Decode the provided hexadecimal data to recover the hidden flag.

## Challenge Data

**Hex-encoded bytes:**
C1 A2 83 89 89 A2 C3 96 A4 A2 89 95

**Flavor Text:**
> “Old school is the best school”  
> — Quote by retired IBM engineer

## Initial Analysis
The challenge title phonetically resembles “EBCDIC,” an IBM-developed character encoding.
The reference to an IBM engineer strongly reinforces this hint.

The provided data consists of hexadecimal byte values that do not map cleanly to ASCII,
suggesting an alternate encoding rather than encryption.

## Encoding Identified
**EBCDIC (Extended Binary Coded Decimal Interchange Code)**

EBCDIC was historically used on IBM mainframe systems and differs significantly from ASCII.

## Decoding Process (Python)

```python
hex_data = "C1A2838989A2C396A4A28995"
bytes_data = bytes.fromhex(hex_data)

decoded = bytes_data.decode("cp037")
print(decoded)
