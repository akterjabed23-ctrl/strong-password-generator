import random
import string

def generate_password(length=12):
    """Generate a random strong password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars)
                   for _ in range(length))

def main():
    print("=== Random Password Generator ===")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        print("Invalid input! Using default length 12.")
        length = 12
    password = generate_password(length)
    print(f"\nGenerated password: {password}\n")

if __name__ == "__main__":
    main()
