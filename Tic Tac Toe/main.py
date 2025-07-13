import tkinter as tk
import customtkinter as ctk
import random
from PIL import Image
from customtkinter import CTkImage

# Window Creation
window = ctk.CTk()
window.title("Tic-Tac-Toe")
window.geometry("500x570")
window.configure(fg_color="#343434")
window.resizable(False, False)

# BG Image for starting interface
img = CTkImage(Image.open("intro.png"), size=(500, 570))

bg_label = ctk.CTkLabel(window, image=img, text="")
bg_label.place(relx=0.5, rely=0.5, anchor="center")

# Variables
button = []
winning_combos = [ [0, 1, 2], [3, 4, 5], [6, 7, 8] ,[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8] ,[2, 4, 6] ]
is_multiplayer = False
current_turn = "X"

# Functions
def create_button():
    for i in range(9):
        btn = ctk.CTkButton(canvas, width=160 , height=160 ,text="", font=("Arial", 70, "bold"), fg_color="#343434", hover_color="#3c3c3c", corner_radius=0, border_width=1, border_color="white", command=lambda i=i: user_move(i))
        btn.grid(row=i//3, column=i%3)
        button.append(btn)

def singleplayer():
    global is_multiplayer, current_turn
    is_multiplayer = False
    current_turn = "X"

    tic_tac_toe_label.place_forget()
    singleplayer_button.place_forget()
    multiplayer_button.place_forget()
    turn_label.place(relx=0.5, rely=0.06, anchor="center")
    canvas.place(relx=0.5, rely=0.56, anchor="center")
    create_button()

def multiplayer():
    global is_multiplayer, current_turn
    is_multiplayer = True
    current_turn = "X"

    tic_tac_toe_label.place_forget()
    singleplayer_button.place_forget()
    multiplayer_button.place_forget()
    turn_label.place(relx=0.5, rely=0.06, anchor="center")
    canvas.place(relx=0.5, rely=0.56, anchor="center")
    create_button()

def user_move(index):
    global current_turn

    btn = button[index]
    if btn.cget("text") == "":
        btn.configure(text=current_turn, text_color="#FFD43B" if current_turn == "X" else "#306998" )
        btn._state = "disabled"
        evaluate_game_result()

        if is_multiplayer:
            if current_turn == "X":
                current_turn = "O"
            else:
                current_turn ="X"
            turn_label.configure(text=f"{current_turn}'s Turn")
        else:
            turn_label.configure(text="Computer's Turn")
            window.after(500, computer_move)

def computer_move():
    empty_button = [btn for btn in button if btn.cget("text") == ""]
    if empty_button:
        btn = random.choice(empty_button)
        btn.configure(text="O", text_color="#306998")
        btn._state = "disabled"
    turn_label.configure(text="Your Turn")
    evaluate_game_result()

def winner_checker():
    for combo in winning_combos:
        a, b, c = combo
        if (button[a].cget("text") == button[b].cget("text") == button[c].cget("text") and button[a].cget("text") != ""):
            return button[a].cget("text"), combo
    return None, None

def evaluate_game_result():
    winner, combo = winner_checker()
    if winner == "X":
        for index in combo:
            button[index].configure(fg_color="#4CAF50")
        window.after(2000, lambda: display_end_screen("win"))
    elif winner == "O":
        for index in combo:
            button[index].configure(fg_color="#4CAF50")
        window.after(2000,lambda: display_end_screen("lose"))

    elif all(btn.cget("text") != "" for btn in button):
        window.after(2000, lambda: display_end_screen("draw"))

def display_end_screen(result):

    canvas.place_forget()
    turn_label.place_forget()
    if is_multiplayer:
        if result == "win":
            x_won_label.place(relx=0.5, rely=0.25, anchor="center")
        elif result == "lose":
            o_won_label.place(relx=0.5, rely=0.25, anchor="center")
        elif result == "draw":
            draw_label.place(relx=0.5, rely=0.2, anchor="center")
    else:
        if result == "win":
            win_label.place(relx=0.5, rely=0.25, anchor="center")
        elif result == "lose":
            lose_label.place(relx=0.5, rely=0.2, anchor="center")
        elif result == "draw":
            draw_label.place(relx=0.5, rely=0.2, anchor="center")

    restart_button.place(relx=0.5, rely=0.45, anchor="center")
    main_menu_button.place(relx=0.5, rely=0.6, anchor="center")
    quit_button.place(relx=0.5, rely=0.75, anchor="center")


def main_menu():
    for btn in button:
        btn.destroy()
    button.clear()

    win_label.place_forget()
    lose_label.place_forget()
    draw_label.place_forget()
    x_won_label.place_forget()
    o_won_label.place_forget()
    restart_button.place_forget()
    main_menu_button.place_forget()
    quit_button.place_forget()

    tic_tac_toe_label.place(relx=0.5, rely=0.3, anchor="center")
    singleplayer_button.place(relx=0.5, rely=0.5, anchor="center")
    multiplayer_button.place(relx=0.5, rely=0.65, anchor="center")

def restart():
    for btn in button:
        btn.destroy()
    button.clear()

    win_label.place_forget()
    lose_label.place_forget()
    draw_label.place_forget()
    restart_button.place_forget()
    main_menu_button.place_forget()
    quit_button.place_forget()

    if is_multiplayer:
        multiplayer()
    else:
        singleplayer()

# Ui Elements
tic_tac_toe_label = ctk.CTkLabel(window, text= "Tic-Tac-Toe", font= ("Arial", 50, "bold"), text_color="#FFEA00")
tic_tac_toe_label.place(relx=0.5, rely=0.3, anchor="center")

turn_label = ctk.CTkLabel(window, text= "Your Turn", font= ("Segoe UI", 30, "bold"), text_color="white")

win_label = ctk.CTkLabel(window, text= "You Won", font= ("Arial", 60, "bold"), text_color="#39FF14")

lose_label= ctk.CTkLabel(window, text= "You Lose", font= ("Arial", 60, "bold"), text_color="#FF3030")

draw_label = ctk.CTkLabel(window, text= "Draw", font= ("Arial", 60, "bold"), text_color="white")

x_won_label = ctk.CTkLabel(window, text= "X Won", font= ("Arial", 60, "bold"), text_color="#39FF14")

o_won_label = ctk.CTkLabel(window, text= "O Won", font= ("Arial", 60, "bold"), text_color="#39FF14")

singleplayer_button = ctk.CTkButton(window, width=140, height=60, fg_color="white", corner_radius=15, text="Singleplayer", font=("Arial", 25, "bold",), text_color="black", hover_color= "#FFD43B", command=singleplayer)
singleplayer_button.place(relx=0.5, rely=0.5, anchor="center")

multiplayer_button = ctk.CTkButton(window, width=140, height=60, fg_color="white", corner_radius=15, text=" Multiplayer ", font=("Arial", 25, "bold",), text_color="black", hover_color= "#FFD43B", command= multiplayer)
multiplayer_button.place(relx=0.5, rely=0.65, anchor="center")

restart_button = ctk.CTkButton(window, width=140, height=60, fg_color="white", corner_radius=15, text="Restart", font=("Arial", 25, "bold",), text_color="black", hover_color= "#FFD43B", command= restart)

main_menu_button = ctk.CTkButton(window, width=140, height=60, fg_color="white", corner_radius=15, text="Main Menu", font=("Arial", 25, "bold",), text_color="black", hover_color= "#FFD43B", command= main_menu)

quit_button = ctk.CTkButton(window, width=140, height=60, fg_color="white", corner_radius=15, text="Quit", font=("Arial", 25, "bold",), text_color="black", hover_color= "#FFD43B", command = window.destroy)

# Canvas
canvas = tk.Canvas(window, width=500, height=500, bg="#343434", highlightthickness=0)

window.mainloop()