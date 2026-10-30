# Vajaran Nall

REQUIRED_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REQUIRED_LOWER = 'abcdefghijklmnopqrstuvwxyz'
REQUIRED_DIGIT = '0123456789'


def main():
    """Main function to run the password validator."""
    try:
        password, result = validation_check(get_password())
        if result:
            print(result)
        else:
            print(f"Password: {password}")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_password():

    # Ask the user to enter a password and validate it
    while True:
        password = input("Enter your password: ")
        
        if not password.strip():
            print("Please enter a password")
        else:
            return password
        
        

def validation_check(password):
    
    # Does the password meet the specified criteria
    if len(password) < 8:
        return False, f"Password must be at least 8 characters long."

    has_upper = any(c in REQUIRED_UPPER for c in password)
    has_lower = any(c in REQUIRED_LOWER for c in password)
    has_digit = any(c in REQUIRED_DIGIT for c in password)

    if not has_upper or not has_lower or not has_digit:
        reasons = []
        if not has_upper:
            reasons.append("Does not contain uppercase letters.")
        if not has_lower:
            reasons.append("Does not contain lowercase letters.")
        if not has_digit:
            reasons.append("Does not contain digits.")
        return False, f"Password is invalid. Requirements not met: {', '.join(reasons)}"

    for c in password:
        if c not in (REQUIRED_UPPER + REQUIRED_LOWER + REQUIRED_DIGIT):
            return False, "Password may only contain letters and digits."
    
    return True, "Password is valid."

if __name__ == "__main__":
    main()