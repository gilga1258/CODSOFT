import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x350")

title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

instruction = tk.Label(window, text="Choose your move:", font=("Arial", 12))
instruction.pack()

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=f"You chose {user_choice}\nComputer chose {computer_choice}\n\n{result}")
    score_label.config(text=f"Your Score: {user_score}   Computer Score: {computer_score}")

result_label = tk.Label(window, text="", font=("Arial", 12), pady=10)
result_label.pack()

score_label = tk.Label(window, text="Your Score: 0   Computer Score: 0", font=("Arial", 12))
score_label.pack()

window.mainloop()
