#Password Generator source code made by Cedric Arts

"""
import random
import sys
import tkinter


def GeneratePassword():

    answer = input("Do you want a password?:" )

    if answer.lower() == 'yes':
        # Allowing user to change length of password
        length = input("How long should the password be: ")

        # Declaring list of characters, digits to be used in password
        pass1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        password = ""

        # Generating password
        for x in range(int(length)):
            password = password + random.choices(pass1)[0]
        #Displaying password to user
        print("Your new password is\n: ", password)
    else:
        print("Goodbye, have a great day!!")

GeneratePassword()
"""
# Password Generator with the assistance of ChatGPT

"""import random
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def GeneratePassword():
    try:
        # Get the length from the entry widget
        length = int(length_entry.get())

        # List of characters to be used in the password
        pass1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        password = ""

        # Generate the password
        for x in range(length):
            password += random.choice(pass1)

        # Display the password in the label
        password_label.config(text=f"Your password is: {password}")
    except ValueError:
        # Show an error if the length entry is not a valid number
        messagebox.showerror("Invalid Input", "Please enter a valid number for the length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Label and Entry for password length input
length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Button to trigger password generation
generate_button = tk.Button(root, text="Generate Password", command=GeneratePassword)
generate_button.pack(pady=10)

# Label to display the generated password
password_label = tk.Label(root, text="")
password_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
"""
# Assistance from ChatGPT

import random
import tkinter as tk
from tkinter import ttk, messagebox

# Function to generate password
def GeneratePassword():
    try:
        # Get the length from the entry widget
        length = int(length_entry.get())

        # Character sets based on user selections
        digits = '0123456789'
        symbols = '!@#$%^&*()'
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # Build the pool of characters based on selected options
        character_pool = ""
        if digits_var.get():
            character_pool += digits
        if symbols_var.get():
            character_pool += symbols
        if letters_var.get():
            character_pool += lowercase + uppercase

        # If no options are selected, show an error
        if not character_pool:
            messagebox.showerror("Input Error", "Please select at least one option (letters, digits, or symbols).")
            return
        
        # Generate the password
        password = "".join(random.choice(character_pool) for _ in range(length))

        # Display the password in the label
        password_label.config(text=f"Your password is: {password}")
    except ValueError:
        # Show an error if the length entry is not a valid number
        messagebox.showerror("Invalid Input", "Please enter a valid number for the length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Apply modern style using ttk widgets
style = ttk.Style(root)
style.theme_use('clam')  # Change this to 'clam', 'alt', 'default', or 'classic' for different looks

# Frame for the length and options
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Length input label and entry
length_label = ttk.Label(main_frame, text="Enter password length:")
length_label.pack(pady=5)

length_entry = ttk.Entry(main_frame)
length_entry.pack(pady=5)

# Options for password content
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()
letters_var = tk.BooleanVar()

# Checkbuttons for password options
digits_check = ttk.Checkbutton(main_frame, text="Include Digits (0-9)", variable=digits_var)
digits_check.pack(pady=5)

symbols_check = ttk.Checkbutton(main_frame, text="Include Symbols (!@#$%^&*)", variable=symbols_var)
symbols_check.pack(pady=5)

letters_check = ttk.Checkbutton(main_frame, text="Include Letters (a-z, A-Z)", variable=letters_var)
letters_check.pack(pady=5)

# Button to generate the password
generate_button = ttk.Button(main_frame, text="Generate Password", command=GeneratePassword)
generate_button.pack(pady=20)

# Label to display the generated password
password_label = ttk.Label(main_frame, text="")
password_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

    
