# Password Strength Checker

A command-line Python tool that evaluates a password and reports whether it is **Weak**, **Medium**, or **Strong**, along with a tip for improving it.

## 📌 Overview

The script checks a password against:
- A list of common/known passwords (loaded from a text file)
- Character variety: uppercase, lowercase, digits, and symbols

Based on these checks, it returns a strength rating and a short improvement tip.

## 📂 Files

| File | Description |
|------|--------------|
| `password-strength-checker.py` | Main script |
| `common_passwords.txt` | Auto-generated on first run if missing, seeded with a few example common passwords |

## ▶️ How to Run

```bash
python3 password-strength-checker.py
```

You'll be prompted once to enter a password, then the script prints an evaluation report and exits.

### Example

```
Enter a password to check: Summer2024!

==============================================
        🔒 PASSWORD EVALUATION REPORT
==============================================
Strength : Strong
Tip      : Great password!
==============================================
```

## 🧠 Strength Logic

| Condition | Result |
|---|---|
| Password found in common password list | Weak |
| Length < 8 characters | Weak |
| Character variety score ≤ 2 (out of upper/lower/digit/symbol) | Weak |
| Variety score == 3 | Medium |
| Variety score == 4 and length < 12 | Medium |
| Variety score == 4 and length ≥ 12 | Strong |

## ⚠️ Known Issues

The script as uploaded has a couple of bugs that will prevent it from running correctly:

1. **`load_common_passwords` has an invalid path reference.**
   ```python
   if not os.path.exists(/home/mini/rockyou.txt):
   ```
   The path isn't quoted as a string, which is a syntax error in Python, and it also ignores the `file_path` argument passed into the function. It should read:
   ```python
   if not os.path.exists(file_path):
   ```

2. **The "print if missing" message has the same unquoted-path issue:**
   ```python
   print(f"Warning: '{/home/mini/rockyou.txt}' not found. ...")
   ```
   This should reference `file_path` instead.

3. **Hardcoded path mismatch.** The intent appears to be pointing at a local `rockyou.txt` wordlist (a large real-world leaked-password dataset commonly used for defensive password-strength checks), but the `main` block actually creates and loads a separate small `common_passwords.txt` file instead. Decide which source you want and make the function and the main block consistent.

Fixing points 1 and 2 (replacing the hardcoded path with the `file_path` parameter) is enough to make the script run as intended.

## 🚀 Ideas to Extend

- Point `common_passwords_file` at a full leaked-password dataset for stronger checks
- Add entropy-based scoring instead of a simple variety count
- Support checking multiple passwords in one run (loop until `quit`)
- Mask password input using `getpass` instead of plain `input()`