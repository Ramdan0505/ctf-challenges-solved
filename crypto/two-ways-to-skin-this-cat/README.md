# Two ways to skin this cat

**Platform:** Virginia Cyber Range – Cloud CTF  
**Category:** Cryptography / Passwords  
**Difficulty:** Medium  
**Artifacts:** `shadow`, `password-clean.lst`  
**Technique:** SHA-512 crypt ($6$) hash cracking + concatenation

## Objective
Recover plaintext passwords from a Linux `shadow` file using the provided wordlist, then concatenate the recovered passwords and submit the result as the key.

## Challenge Data
Files provided:
- `shadow` (Linux password hash database)
- `password-clean.lst` (candidate password list)

## Initial Analysis
The `shadow` file stores password hashes in the format:

`username:$id$salt$hash:...`

All entries begin with `$6$`, indicating **SHA-512 crypt**. Since a wordlist is provided, the intended solution is dictionary cracking rather than brute force.

Users listed (in file order):
1. masked
2. yellow
3. jester
4. catty

## Cracking Method
For each user:
1. Extract the `$6$salt$` component
2. Hash each candidate with the same salt using `crypt.crypt()`
3. Compare against the stored hash

## Reproducible Solution (Python)
(See `solve.py` in this folder.)

## Result
Cracked passwords:
- masked → granny
- yellow → pinkie
- jester → minute
- catty → cornered

Concatenated key (same order as `shadow`):
`grannypinkieminutecornered`

## Lessons Learned
- `$6$` in `/etc/shadow` indicates SHA-512 crypt
- Salt must match exactly when verifying candidate passwords
- Many “password” challenges are solved by dictionary cracking, not brute force
- When a prompt specifies “concatenate,” preserve the original file order
