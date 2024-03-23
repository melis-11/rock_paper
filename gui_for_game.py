import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors Game")
        self.geometry("300x400")
        self.configure(background="#333333")  # Set background color to a darker shade

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.lbl_instruction = tk.Label(self, text="Select Rock, Paper, or Scissors:", bg="#333333", fg="white", font=("Arial", 14))
        self.lbl_instruction.pack(pady=10)

        self.btn_rock = tk.Button(self, text="Rock", command=lambda: self.play("rock"), bg="#90EE90", font=("Arial", 12))
        self.btn_rock.pack(fill=tk.X, padx=10, pady=5)

        self.btn_paper = tk.Button(self, text="Paper", command=lambda: self.play("paper"), bg="#ADD8E6", font=("Arial", 12))
        self.btn_paper.pack(fill=tk.X, padx=10, pady=5)

        self.btn_scissors = tk.Button(self, text="Scissors", command=lambda: self.play("scissors"), bg="#FFB6C1", font=("Arial", 12))
        self.btn_scissors.pack(fill=tk.X, padx=10, pady=5)

        self.lbl_score = tk.Label(self, text="Score: You 0 - 0 Computer", bg="#333333", fg="white", font=("Arial", 12, "bold"))
        self.lbl_score.pack(pady=20)

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)
        self.update_score(result)

        messagebox.showinfo("Result", f"Computer chose {computer_choice}. {result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "Computer wins!"

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

        self.lbl_score.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer", fg="white")

if __name__ == "__main__":
    app = RockPaperScissorsGame()
    app.mainloop()
