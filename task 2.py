import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operation = operation_entry.get()

        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b != 0:
                result = a / b
            else:
                result = "Can't divide by zero"
        else:
            result = "Invalid operation"

        result_label.config(text="Result: " + str(result))
    except:
        messagebox.showerror("Error", "Enter valid numbers")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x250")

tk.Label(root, text="First Number:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root, font=("Arial", 12), width=20)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root, font=("Arial", 12), width=20)
entry2.grid(row=1, column=1)

tk.Label(root, text="Operation (+ - * /):", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
operation_entry = tk.Entry(root, font=("Arial", 12), width=20)
operation_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate).grid(row=3, column=0, columnspan=2, pady=15)

result_label = tk.Label(root, text="Result:", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
