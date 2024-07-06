# password_strength.py
def evaluate_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for c in password)

    strength = "Weak"
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif length >= 8 and ((has_upper and has_lower) or (has_digit and has_special)):
        strength = "Moderate"

    return strength
