# Where’s the Secret? — Forensics Write-Up

Platform: Virginia Cyber Range  
Category: Forensics  
Points: 20  
Status: Solved  

---

Challenge Description

There is a secret hidden in the image. Can you decode it?

The challenge provides an image file named "cat.jpg".

---

Objective

Analyze the image to locate hidden data and recover the secret message.

---

Initial Analysis

The image opened normally, with no visible flag or message. This suggested the secret was hidden using steganography or metadata rather than being visually obvious.

---

Metadata Check

I first checked for hidden metadata:

exiftool cat.jpg

No useful or suspicious metadata was found, indicating the secret was likely embedded in the image data itself.

---

Steganography Analysis

Next, I analyzed the image using steganography techniques. By inspecting individual color channels and bit planes, hidden data became visible.

This revealed encoded information that was not present in the original image view.

---

Decoding the Secret

The extracted hidden data was decoded to reveal the flag.

---

Flag

flag{REDACTED}

---

Key Takeaways

- Images can hide data beyond what is visually observable
- Metadata inspection is a fast first step
- Steganography tools are effective for uncovering hidden image data
- Visual analysis is critical in forensic image challenges

---

Tools Used

- exiftool
- steganography analysis tools

