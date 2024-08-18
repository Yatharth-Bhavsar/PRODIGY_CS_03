import re
import random
import string

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Check for special characters
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (e.g., @, #, $, etc.).")

    # Strength assessment
    if strength == 5:
        feedback.insert(0, "Strong password!")
    elif 3 <= strength < 5:
        feedback.insert(0, "Moderate password.")
    else:
        feedback.insert(0, "Weak password.")

    return feedback

def generate_random_password(length):
    if length < 8:
        print("Password length should be at least 8 characters for a strong password.")
        return None
    
    # Define character set: uppercase, lowercase, digits, and special characters
    char_set = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random password
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    return password

# Menu-driven interface
while True:
    print("\nPassword Tool Menu:")
    print("1. Check password strength")
    print("2. Generate a random password")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        password = input("Enter a password to check its strength: ")
        feedback = check_password_strength(password)
        print("\nPassword Strength Feedback:")
        for line in feedback:
            print("- " + line)
        print()
    elif choice == '2':
        try:
            length = int(input("Enter the desired length for the password (minimum 8 characters): ").strip())
            password = generate_random_password(length)
            if password:
                print("\nGenerated Password:", password)
                feedback = check_password_strength(password)
                print("\nPassword Strength Feedback:")
                for line in feedback:
                    print("- " + line)
        except ValueError:
            print("Please enter a valid integer for the length.")
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
