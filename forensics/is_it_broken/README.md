# Is It Broken? — Forensics Write-Up

Platform: Virginia Cyber Range  
Category: Forensics  
Points: 20  
Status: Solved  

---

Challenge Description

We intercepted an image, but we can’t open it?

The challenge provides a file named "isitbroken". Although it is supposed to be an image, it does not open in standard image viewers.

---

Objective

Identify why the image cannot be opened, fix the issue, and recover the hidden flag.

---

Initial Analysis

First, I checked the file type:

file isitbroken

The result did not clearly identify the file as a valid image format, which suggested the file header might be corrupted.

---

Forensic Examination

Next, I examined the file header using a hex dump:

xxd isitbroken | head

Most image files start with specific magic bytes that identify the file type. For example:

PNG files start with: 89 50 4E 47 0D 0A 1A 0A  
JPEG files start with: FF D8 FF  

The bytes at the beginning of the file did not match any valid image format.

---

Repairing the File

Based on the file structure, it appeared the image was a PNG with an incorrect header.

I repaired the header by replacing the first 8 bytes with the correct PNG signature:

printf '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' | dd of=isitbroken bs=1 count=8 conv=notrunc

This fixed the corrupted header without changing the rest of the file.

---

Verification

After repairing the header, the file opened successfully as an image. The image revealed the flag.

---

Flag

Key Takeaways

- File extensions cannot be trusted
- Magic bytes are critical for identifying file types
- Hex inspection can quickly reveal corrupted headers
- Simple fixes can recover damaged forensic evidence


Tools Used

- file
- xxd
- hex-level byte editing
