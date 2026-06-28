import tkinter as tk
from tkinter import messagebox
import random

def checkWin():
    global winner, x_score, o_score, draw_score
    winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in winning_combos:
        if buttons[combo[0]]['text'] == buttons[combo[1]]["text"] == buttons[combo[2]]['text'] != "":
            winner = True
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green") 
            if buttons[combo[0]]['text'] == "X":
                x_score += 1
            else:
                o_score += 1
            score_label.config(
                text=f"X: {x_score}    O: {o_score}    Draws: {draw_score}")  
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")   
            for button in buttons:
                button.config(state="disabled")
            return
        
        # draw condition
    if all(button['text'] != "" for button in buttons):
        draw_score += 1
        score_label.config(
            text=f"X: {x_score}    O: {o_score}    Draws: {draw_score}")    
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        for button in buttons:
            button.config(state="disabled")

def button_click(i):
    if buttons[i]['text'] == "" and not winner:
        buttons[i]['text'] = current_player
        
        checkWin()
        
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text = f"Player {current_player}'s turn")

def restart_game():
    global current_player, winner

    current_player = random.choice(["X", "O"])
    winner = False

    label.config(
    text=f"Current Turn: {'❌' if current_player=='X' else '⭕'}")

    for button in buttons:
        button.config(text="", bg="SystemButtonFace", state="normal")

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [tk.Button(root, text="", font=('normal', 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)
x_score = 0
o_score = 0
draw_score = 0
current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 16))
label.grid(row=3, column=0, columnspan=3)
score_label = tk.Label(
    root,
    text="X: 0    O: 0    Draws: 0",
    font=("Arial", 14)
)
score_label.grid(row=4, column=0, columnspan=3)
restart_button = tk.Button(root, text="Restart", font=('normal', 16), command=restart_game)
restart_button.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()