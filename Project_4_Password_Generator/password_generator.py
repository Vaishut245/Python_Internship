# password_generator.py
import random
import string
import json
from utils import load_config, get_character_set
from password_strength import evaluate_password_strength

def generate_password(length, characters):
    return ''.join(random.choice(characters) for i in range(length))

def save_passwords_to_file(passwords, file_path='passwords.txt'):
    with open(file_path, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

def main():
    config = load_config()
    characters = get_character_set(config)
    
    length = int(input("Enter the length of the password (default {}): ".format(config['default_length'])) or config['default_length'])
    number = int(input("Enter the number of passwords to generate: "))

    passwords = [generate_password(length, characters) for _ in range(number)]

    for password in passwords:
        strength = evaluate_password_strength(password)
        print(f"Password: {password} - Strength: {strength}")

    save_to_file = input("Do you want to save the passwords to a file? (yes/no): ").lower() == 'yes'
    if save_to_file:
        save_passwords_to_file(passwords)

if __name__ == "__main__":
    main()
