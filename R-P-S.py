import tkinter as tk
import customtkinter
from PIL import Image
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle the game logic and update the result label
def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    if result == "You win!":
        result_label.configure(image=green_dot)
    elif result == "You lose!":
        result_label.configure(image=red_dot)
    elif result == "It's a tie!":
        result_label.configure(image=black_dot)

    # Update computer's choice image
    if computer_choice == "rock":
        cpu_result.configure(image=rock_imgi)
    elif computer_choice == "paper":
        cpu_result.configure(image=paper_imgi)
    elif computer_choice == "scissors":
        cpu_result.configure(image=scissors_imgi)

    global attempts
    attempts += 1
    if attempts >= 3:
        for button in buttons:
            button.configure(state=tk.DISABLED)
        try_again_button.configure(state=tk.NORMAL, image=retry_img)

# Function to reset the game
def try_again():
    global attempts
    attempts = 0
    result_label.configure(image=empty_dot)
    cpu_result.configure(image=hand)
    for button in buttons:
        button.configure(state=tk.NORMAL)
    try_again_button.configure(state=tk.DISABLED, image=retry_dis)

def show_frame(frame):
    frame.tkraise()

# Initialize the Tkinter window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.title("R-P-S")
root.geometry("350x300")
root.resizable(False, False)

attempts = 0

# Load images for the choices
rock_img = customtkinter.CTkImage(dark_image=Image.open("images/r.png"), size=(25, 25))
paper_img = customtkinter.CTkImage(dark_image=Image.open("images/p.png"), size=(25, 25))
scissors_img = customtkinter.CTkImage(dark_image=Image.open("images/s.png"), size=(25, 25))
rock_imgi = customtkinter.CTkImage(dark_image=Image.open("images/r(i).png"), size=(25, 25))
paper_imgi = customtkinter.CTkImage(dark_image=Image.open("images/p(i).png"), size=(25, 25))
scissors_imgi = customtkinter.CTkImage(dark_image=Image.open("images/s(i).png"), size=(25, 25))
red_dot = customtkinter.CTkImage(dark_image=Image.open("images/rd.png"), size=(25, 25))
green_dot = customtkinter.CTkImage(dark_image=Image.open("images/gd.png"), size=(25, 25))
black_dot = customtkinter.CTkImage(dark_image=Image.open("images/bd.png"), size=(25, 25))
empty_dot = customtkinter.CTkImage(dark_image=Image.open("images/ed.png"), size=(25, 25))
user = customtkinter.CTkImage(dark_image=Image.open("images/u.png"), size=(32, 32))
cpu = customtkinter.CTkImage(dark_image=Image.open("images/c.png"), size=(32, 32))
hand = customtkinter.CTkImage(dark_image=Image.open("images/hand.png"), size=(25, 25))
retry_img = customtkinter.CTkImage(dark_image=Image.open("images/rw.png"), size=(25, 25))
retry_dis = customtkinter.CTkImage(dark_image=Image.open("images/ww.png"), size=(25, 25))
back = customtkinter.CTkImage(dark_image=Image.open("images/b.png"), size=(25, 25))

# Create a container frame to hold all pages
container = customtkinter.CTkFrame(root)
container.pack(fill="both", expand=True)

# Create the first page frame
page1 = customtkinter.CTkFrame(container,fg_color="#1a1a1a")
page1.grid(row=0, column=0, sticky="nsew")

frame = customtkinter.CTkFrame(master=page1, width=150, height=45, corner_radius=7, fg_color="#1f1f1f")
frame.place(relx=0.5, rely=0.24, anchor=tk.CENTER)

# Create buttons for user choices
buttons = []
for i, (img, choice) in enumerate(zip([rock_img, paper_img, scissors_img], ["rock", "paper", "scissors"])):
    button = customtkinter.CTkButton(frame, image=img, text="", width=30, height=35, fg_color="#eaeaea", hover_color="#bbbbbb", command=lambda c=choice: play_game(c))
    button.place(x=5 + i * 50, y=5)  # Adjust x position by 50 for each subsequent button
    buttons.append(button)

frame3 = customtkinter.CTkFrame(page1,height=30,width=30)
frame3.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
# Create a label to display the result
result_label = customtkinter.CTkLabel(frame3, image=empty_dot, text="")
result_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
user1 = customtkinter.CTkLabel(page1, image=user, text="")
user1.place(relx=0.5, rely=0.11, anchor=tk.CENTER)

# Create a label to display the computer's choice image
frame2 = customtkinter.CTkFrame(master=page1, width=150, height=45, corner_radius=7, fg_color="#1f1f1f")
frame2.place(relx=0.5, rely=0.51, anchor=tk.CENTER)
cpu_result = customtkinter.CTkButton(frame2, image=hand, text="", fg_color="#eaeaea", hover_color="#eaeaea", state=tk.DISABLED)
cpu_result.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
cpu1 = customtkinter.CTkLabel(page1, image=cpu, text="")
cpu1.place(relx=0.5, rely=0.38, anchor=tk.CENTER)

# Create a "Try Again" button
try_again_button = customtkinter.CTkButton(page1, image=retry_dis, text="", fg_color="#eaeaea", hover_color="#eaeaea", command=try_again, state=tk.DISABLED)
try_again_button.place(relx=0.73, rely=0.9, anchor=tk.CENTER)

# Create a next button to navigate to the second page
next_button = customtkinter.CTkButton(page1, text="Rules",font=("Bahnschrift", 14),height=32,fg_color="#eaeaea", hover_color="#bbbbbb",text_color="#1a1a1a", command=lambda: show_frame(page2))
next_button.place(relx=0.27, rely=0.9, anchor=tk.CENTER)

# Create the second page frame
page2 = customtkinter.CTkFrame(container,fg_color="#1a1a1a")
page2.grid(row=0, column=0, sticky="nsew")

# Add content to the second page
label2 = customtkinter.CTkLabel(page2,font=("Bahnschrift", 20),text="1- Rock beats scissors\n2- Scissors beats paper\n3- Paper beats rock\n\n     means ( You win )\n     mean ( You lose )\n     mean ( It's a tie )")
label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
g = customtkinter.CTkLabel(page2,font=("Bahnschrift", 20),image=green_dot,text="")
g.place(relx=0.26, rely=0.49, anchor=tk.CENTER)
r = customtkinter.CTkLabel(page2,font=("Bahnschrift", 20),image=red_dot,text="")
r.place(relx=0.26, rely=0.572, anchor=tk.CENTER)
b = customtkinter.CTkLabel(page2,font=("Bahnschrift", 20),image=black_dot,text="")
b.place(relx=0.26, rely=0.653, anchor=tk.CENTER)

# Create a back button to navigate back to the first page
back_button = customtkinter.CTkButton(page2, text="",fg_color="#eaeaea", hover_color="#bbbbbb",image=back, command=lambda: show_frame(page1))
back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Configure the container to expand and fill the entire window
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Show the first page initially
show_frame(page1)

# Run the Tkinter event loop
root.mainloop()
