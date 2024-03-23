from flask import Flask, render_template
import tkinter as tk
from tkinter import messagebox
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play/<choice>")
def play(choice):
    result = play_game(choice)
    return result

def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    return f"Computer chose {computer_choice}. {result}"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == "__main__":
    app.run(debug=True)
