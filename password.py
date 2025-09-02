"""
Create a Python script to check the strength of the password with password score
"""

def check_password_strength(password):
    """
        Checks if the password meets the following criteria:
        - Minimum length of 8 characters
        - Contains both uppercase and lowercase letters
        - Contains at least one digit (0-9)
        - Contains at least one special character (!, @, #, $, %, etc.)
        - Does not contain spaces
    """
    errors = []  # List to store validation errors
    strength_score = 0  # Score to determine password strength
    password = password.strip() # Strip the before and after spaces
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    
    if " " in password:
        errors.append("Spaces are not allowed inside the password")
    if len(password) < 8:
        errors.append("Minimum 8 characters are needed")
    if not any(char.isupper() for char in password):
        errors.append("Password should contain at least 1 uppercase letter")
    if not any(char.islower() for char in password):
        errors.append("Password should contain at least 1 lowercase letter")
    if not any(char.isdigit() for char in password):  
        errors.append("Password should contain at least 1 digit")
    if not any(char in special_characters for char in password):
        errors.append("Password should contain at least 1 special character")
    
    # If there are errors, return them
    if errors:
        return {"error_count": len(errors), "errors": errors, "strength": "Weak"}

    # **Password Strength Calculation**
    if len(password) >= 12:
        strength_score += 2  # Stronger if length is >= 12
    elif len(password) >= 10:
        strength_score += 1  # Medium strength for length >= 10

    special_count = sum(1 for char in password if char in special_characters)
    if special_count >= 2:
        strength_score += 2  # More than 2 special characters increases strength
    elif special_count == 1:
        strength_score += 1  

    if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        strength_score += 1  # Having both letters and numbers adds strength

    # **Categorizing Password Strength**
    if strength_score >= 4:
        strength = "Strong"
    elif strength_score >= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    return {"error_count": 0, "message": "Password is valid", "strength": strength}

input_password = input("Enter Password: ")

if input_password:
    validate = check_password_strength(input_password)
    print(validate)
else:
    print("Oops! Password cannot be Empty!")