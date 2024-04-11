import re
import random
import string
import tkinter as tk
from tkinter import messagebox

# Global variables
stop_generation = False

def generate_passwords(letters, num_digits, length):
    regex = re.compile('[%s]' % re.escape(''.join(letters)))
    digits = string.digits
    
    while not stop_generation:
        password = ''.join(random.choice(letters) for _ in range(length - num_digits))
        password += ''.join(random.choice(digits) for _ in range(num_digits))
        
        # Shuffle the password characters
        password = ''.join(random.sample(password, len(password)))
        
        if regex.search(password):
            yield password

def generate_and_display_passwords(letters, num_digits, length, output_label):
    global stop_generation
    stop_generation = False
    generator = generate_passwords(letters, num_digits, length)
    for password in generator:
        if not stop_generation:
            output_label.config(text=password)
            root.update()  # Update the Tkinter window
            root.after(1000)  # Wait for 1 second
        else:
            break

def start_generation():
    letters = letter_entry.get()
    num_digits = int(digits_entry.get())
    length = int(length_entry.get())
    
    output_label.config(text="Generating...")
    generate_and_display_passwords(letters, num_digits, length, output_label)

def stop_generation():
    global stop_generation
    stop_generation = True

def generate_passwords_gui():
    global root, letter_entry, digits_entry, length_entry, output_label
    root = tk.Tk()
    root.title("Password Generator")

    # Input fields
    tk.Label(root, text="Enter letters:").grid(row=0, column=0)
    letter_entry = tk.Entry(root)
    letter_entry.grid(row=0, column=1)

    tk.Label(root, text="Number of digits:").grid(row=1, column=0)
    digits_entry = tk.Entry(root)
    digits_entry.grid(row=1, column=1)

    tk.Label(root, text="Password length:").grid(row=2, column=0)
    length_entry = tk.Entry(root)
    length_entry.grid(row=2, column=1)

    # Generate button
    generate_button = tk.Button(root, text="Generate Passwords", command=start_generation)
    generate_button.grid(row=3, column=0)

    # Stop button
    stop_button = tk.Button(root, text="Stop Generation", command=stop_generation)
    stop_button.grid(row=3, column=1)

    # Output label
    output_label = tk.Label(root, text="", font=("Helvetica", 20))
    output_label.grid(row=4, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    generate_passwords_gui()
