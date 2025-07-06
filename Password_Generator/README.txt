🔐 Advanced Password Generator

A secure and customizable command-line password generator written in Python.  
It uses the `secrets` module for cryptographic strength and allows users to define the structure and length of their passwords.

---

✨ Features

- Generate 1 to 20 passwords at once
- Choose password length (8 to 64 characters)
- Optional inclusion of:
  - ✅ Uppercase letters
  - 🔢 Digits
  - 🔐 Special characters
- Ensures cryptographic randomness using the `secrets` module
- Avoids predictable patterns by shuffling characters

---
📦 Requirements

- Python 3.x
- No external libraries required

---

🚀 How to Run

1. Save the file as `password_generator.py`
2. Open a terminal or command prompt
3. Run:

```bash
python password_generator.py


Advanced Password Generator
--------------------------
Number of passwords to generate (1-20): 3
Password length (8-64): 12
Include uppercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): y

Generated Passwords:
1. K&9x@d2gY!r#
2. fW^7zp#V!2s+
3. M3@apw$Lt%r9
