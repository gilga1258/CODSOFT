import tkinter as tk
from tkinter import messagebox
import random
import string

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")

title_label = tk.Label(window, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry_label = tk.Label(window, text="Enter Password Length:", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(window, font=("Arial", 12), width=10, justify='center')
entry.pack(pady=5)

def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password:\n{password}")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer.")

generate_button = tk.Button(window, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), wraplength=350, justify="center")
result_label.pack(pady=10)

window.mainloop()