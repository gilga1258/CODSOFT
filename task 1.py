import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?"):
        tasks.clear()
        update_listbox()

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30, font=("Arial", 14))
entry.grid(row=0, column=0, padx=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=1)

listbox = tk.Listbox(root, width=45, height=15, font=("Arial", 12))
listbox.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack()

remove_btn = tk.Button(btn_frame, text="Remove Task", command=remove_task)
remove_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear All", command=clear_tasks)
clear_btn.grid(row=0, column=1, padx=10)

root.mainloop()
 