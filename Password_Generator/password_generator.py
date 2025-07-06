import random
import string
import secrets

def generate_secure_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """Generate a cryptographically secure random password"""
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = '!@#$%^&*()_+-=[]{}|;:,.<>?' if use_special else ''
    
    # Combine all allowed characters
    all_chars = lowercase + uppercase + digits + special
    
    # Ensure password contains at least one character from each selected set
    password = []
    if use_uppercase:
        password.append(secrets.choice(uppercase))
    if use_digits:
        password.append(secrets.choice(digits))
    if use_special:
        password.append(secrets.choice(special))
    
    # Fill the rest with random characters
    remaining_length = length - len(password)
    password.extend(secrets.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Advanced Password Generator")
    print("--------------------------")
    
    try:
        # Get user preferences
        count = int(input("Number of passwords to generate (1-20): "))
        count = max(1, min(20, count))  # Clamp between 1 and 20
        
        length = int(input("Password length (8-64): "))
        length = max(8, min(64, length))  # Clamp between 8 and 64
        
        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate and display passwords
        print("\nGenerated Passwords:")
        for i in range(count):
            password = generate_secure_password(length, uppercase, digits, special)
            print(f"{i+1}. {password}")
        
    except ValueError:
        print("Please enter valid numerical inputs.")

if __name__ == "__main__":
    main()