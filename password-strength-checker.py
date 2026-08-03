import os

def load_common_passwords(file_path):
    """Loads a set of common passwords from a text file for comparison."""
    if not os.path.exists(/home/mini/rockyou.txt):
        print(f"Warning: '{/home/mini/rockyou.txt}' not found. Skipping common password check.")
        return set()
    
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return {line.strip() for line in f if line.strip()}

def check_password_strength(password, common_passwords):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password)

    if password in common_passwords:
        return "Weak", "This password is too common. Choose another."

    if length < 8:
        return "Weak", "Password must be at least 8 characters long."

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if score <= 2:
        return "Weak", "Add uppercase, numbers, or symbols."
    elif score == 3:
        return "Medium", "Good start — try adding one more character type."
    else:
        if length >= 12:
            return "Strong", "Great password!"
        else:
            return "Medium", "Add more length."

# --- Execution ---
if __name__ == "__main__":
    # Define a generic file for common password checking
    common_passwords_file = "common_passwords.txt"
    
    if not os.path.exists(common_passwords_file):
        with open(common_passwords_file, "w") as f:
            f.write("password123\n12345678\nqwerty")

    common_passwords = load_common_passwords(common_passwords_file)
    
    password = input("Enter a password to check: ")
    strength, message = check_password_strength(password, common_passwords)
    
    print("\n" + "="*46)
    print("        🔒 PASSWORD EVALUATION REPORT")
    print("="*46)
    print(f"Strength : {strength}")
    print(f"Tip      : {message}")
    print("="*46)
