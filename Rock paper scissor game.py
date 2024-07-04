import tkinter as tk
import random

def play(choice):
    comp_choice = random.choice(["ROCK", "PAPER", "SCISSOR"])
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == "ROCK" and comp_choice == "SCISSOR") or (choice == "PAPER" and comp_choice == "ROCK") or (choice == "SCISSOR" and comp_choice == "PAPER"):
        result = "WIN"
    else:
        result = "LOSE"
    
    if result == "WIN":
        user_score.config(text=str(int(user_score.cget("text")) + 1))
    elif result == "LOSE":
        comp_score.config(text=str(int(comp_score.cget("text")) + 1))
    
    result_label.config(text=f"PLAYER: {choice}\nCOMPUTER: {comp_choice}\nRESULT: {result}")

root = tk.Tk()
root.configure(background="black")
root.title("Rock Paper Scissors Game")

label = tk.Label(root, text="rsp game", bg="black", fg="white")
label.grid(row=0, column=0)

user_name = tk.Label(root, text="PLAYER", bg="red")
user_name.grid(row=0, column=1)

comp_name = tk.Label(root, text="COMPUTER", bg="red")
comp_name.grid(row=0, column=3)

comp_score = tk.Label(root, text="0", width=15, height=3, bg="blue", fg="white")
comp_score.grid(row=1, column=3)

user_score = tk.Label(root, text="0", width=15, height=3, bg="blue", fg="white")
user_score.grid(row=1, column=1)

rock = tk.Button(root, width=20, height=4, text="ROCK", bg="yellow", command=lambda: play("ROCK"))
rock.grid(row=2, column=1)

paper = tk.Button(root, width=20, height=4, text="PAPER", bg="yellow", command=lambda: play("PAPER"))
paper.grid(row=2, column=2)

scissor = tk.Button(root, width=20, height=4, text="SCISSOR", bg="yellow", command=lambda: play("SCISSOR"))
scissor.grid(row=2, column=3)

result_label = tk.Label(root, text="", bg="black", fg="white")
result_label.grid(row=3, column=1, columnspan=3)

root.mainloop()