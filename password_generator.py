import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on user preferences."""
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters  # a-z, A-Z
    if use_numbers:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # !@#$%^&* etc.
    
    if not characters:
        return "Error: No character types selected!"
    
    # Randomly choose characters for the password
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("=== Password Generator ===")
    
    try:
        # Get password length
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Error: Length must be a positive number.")
            return
        
        # Get character type preferences
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        # Generate password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        print(f"\nGenerated Password: {password}")
    
    except ValueError:
        print("Error: Please enter a valid number for length.")

if __name__ == "__main__":
    main()
