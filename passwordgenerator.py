import random
import string

def get_password_length():
    """Get the password length from the user and validate the input."""
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_character_set():
    """Get the character set preferences from the user."""
    print("Select character sets to include in the password:")
    print("1. Letters (a-z, A-Z)")
    print("2. Numbers (0-9)")
    print("3. Symbols (!, @, #, $, etc.)")

    character_set = ""

    while True:
        choice = input("Enter the numbers of the character sets to include (comma-separated): ")
        choices = [x.strip() for x in choice.split(",")]
        valid_choices = ["1", "2", "3"]

        if all(x in valid_choices for x in choices):
            for x in choices:
                if x == "1":
                    character_set += string.ascii_letters
                elif x == "2":
                    character_set += string.digits
                elif x == "3":
                    character_set += string.punctuation
            if character_set:
                return character_set
            else:
                print("Please select at least one character set.")
        else:
            print("Invalid input. Please enter the numbers of the character sets.")

def generate_password(length, character_set):
    """Generate a random password based on the given length and character set."""
    return ''.join(random.choice(character_set) for _ in range(length))

def main():
    print("Password Generator")
    print("------------------")
    length = get_password_length()
    character_set = get_character_set()
    password = generate_password(length, character_set)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

