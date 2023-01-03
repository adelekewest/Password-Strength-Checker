import re

def check_password_strength(password):
  # Check if the password is at least 8 characters long
  if len(password) < 8:
    return "Weak"

  # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
  if not re.search(r'[A-Z]', password):
    return "Weak"
  if not re.search(r'[a-z]', password):
    return "Weak"
  if not re.search(r'\d', password):
    return "Weak"

  # Check if the password contains any common patterns or substrings
  if re.search(r'password', password, re.I):
    return "Weak"
  if re.search(r'abcdef', password):
    return "Weak"
  if re.search(r'qwerty', password):
    return "Weak"
  if re.search(r'12345', password):
    return "Weak"

  # If the password passes all checks, it is considered strong
  return "Strong"

# Test the password strength checker
password = input("Enter a password: ")
strength = check_password_strength(password)
print("Password strength:", strength)

