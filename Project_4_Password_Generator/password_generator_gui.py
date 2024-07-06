# password_generator_gui.py
import tkinter as tk
from tkinter import messagebox
import random
from utils import load_config, get_character_set
from password_strength import evaluate_password_strength
from password_generator import generate_password, save_passwords_to_file

def generate_passwords():
    try:
        length = int(length_entry.get())
        number = int(number_entry.get())
        config = load_config()
        characters = get_character_set(config)
        passwords = [generate_password(length, characters) for _ in range(number)]
        result_text.set('\n'.join(passwords))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for length and number of passwords")

def save_passwords():
    passwords = result_text.get().split('\n')
    save_passwords_to_file(passwords)

# GUI setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Length of password:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

tk.Label(root, text="Number of passwords:").pack()
number_entry = tk.Entry(root)
number_entry.pack()

tk.Button(root, text="Generate", command=generate_passwords).pack()
tk.Button(root, text="Save to file", command=save_passwords).pack()

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text).pack()

root.mainloop()
