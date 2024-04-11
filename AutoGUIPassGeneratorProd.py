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
    root.title("Random Password Generator")
    root.geometry("650x400")
    root.config(bg="#000000")  # Black background color

    # Header label
    header_label = tk.Label(root, text="Random Password Generator", font=("Times New Roman", 30), fg="#00ff00", bg="#000000")
    header_label.pack(pady=(20, 10))

    # Input fields
    input_frame = tk.Frame(root, bg="#000000")
    input_frame.pack()

    tk.Label(input_frame, text="Enter letters:", font=("Times New Roman", 24), fg="#00ff00", bg="#000000").grid(row=0, column=0, padx=10, pady=5)
    letter_entry = tk.Entry(input_frame, font=("Times New Roman", 24))
    letter_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="Number of digits:", font=("Times New Roman", 24), fg="#00ff00", bg="#000000").grid(row=1, column=0, padx=10, pady=5)
    digits_entry = tk.Entry(input_frame, font=("Times New Roman", 24))
    digits_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="Password length:", font=("Times New Roman", 24), fg="#00ff00", bg="#000000").grid(row=2, column=0, padx=10, pady=5)
    length_entry = tk.Entry(input_frame, font=("Times New Roman", 24))
    length_entry.grid(row=2, column=1, padx=10, pady=5)

    # Generate and Stop buttons
    buttons_frame = tk.Frame(root, bg="#000000")
    buttons_frame.pack(pady=(10, 20))

    generate_button = tk.Button(buttons_frame, text="Generate Passwords", font=("Times New Roman", 24), bg="#00ff00", fg="#000000", command=start_generation)
    generate_button.grid(row=0, column=0, padx=10)

    stop_button = tk.Button(buttons_frame, text="Stop Generation", font=("Times New Roman", 24), bg="#ff0000", fg="#000000", command=stop_generation)
    stop_button.grid(row=0, column=1, padx=10)

    # Output label
    output_label = tk.Label(root, text="", font=("Times New Roman", 40), fg="#00ff00", bg="#000000")
    output_label.pack(pady=(0, 10))

    # Center the window
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
    root.geometry("+{}+{}".format(position_right, position_down))

    root.mainloop()

if __name__ == "__main__":
    generate_passwords_gui()
