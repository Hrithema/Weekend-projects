import tkinter as tk
from tkinter import messagebox

def checkWin():
    global winner
    winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in winning_combos:
        if buttons[combo[0]]['text'] == buttons[combo[1]]["text"] == buttons[combo[2]]['text'] != "":
            winner = True
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")   
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")   
            root.destroy()
            return
        # draw condition
    if all(button['text'] != "" for button in buttons):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        root.destroy()

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

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [tk.Button(root, text="", font=('normal', 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()