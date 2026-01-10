import os
import math

COMMON_PASSWORDS_FILE = "claves.txt"

SPECIAL_CHARACTERS = [
    "!", "@", "#", "$", "%", "^", "&", "*",
    "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", ";", ":",
    "'", '"', ",", ".", "<", ">",
    "/", "?", "\\", "|", "`", "~"
]


def load_common_passwords(path):
    passwords = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            passwords.append(line.strip())
    return passwords


def detect_char_sets(password):
    sets_size = 0

    if any(c.islower() for c in password):
        sets_size += 26
    if any(c.isupper() for c in password):
        sets_size += 26
    if any(c.isdigit() for c in password):
        sets_size += 10
    if any(c in SPECIAL_CHARACTERS for c in password):
        sets_size += len(SPECIAL_CHARACTERS)

    return sets_size


def calculate_entropy(password):
    length = len(password)
    charset_size = detect_char_sets(password)

    if charset_size == 0:
        return 0

    combinations = charset_size ** length
    entropy = math.log2(combinations)
    return entropy


def audit_password(password, common_passwords):
    if password in common_passwords:
        return "Insecure password (very common)"

    if len(password) < 8:
        return "Insecure password (too short)"

    entropy = calculate_entropy(password)

    if entropy < 40:
        return "Weak password"
    elif entropy < 60:
        return "Acceptable password"
    else:
        return "Strong password"


def main():
    if not os.path.exists(COMMON_PASSWORDS_FILE):
        print("Common passwords file not found")
        return

    common_passwords = load_common_passwords(COMMON_PASSWORDS_FILE)
    user_password = input("Enter your password: ").strip()

    result = audit_password(user_password, common_passwords)
    entropy = calculate_entropy(user_password)

    print(result)
    print(f"Estimated entropy: {entropy:.2f} bits")


if __name__ == "__main__":
    main()
