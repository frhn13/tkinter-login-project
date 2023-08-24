from tkinter import *
import pandas as pd
import random

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
QUIZ_QUESTIONS = 10


def login():
    login_button.destroy()
    signup_button.destroy()
    username_label.place(x=10, y=10)
    username.place(x=250, y=20)
    password_label.place(x=10, y=100)
    password.place(x=250, y=110)
    submit_login_button.place(x=300, y=250)


def sign_up():
    pass


def submit_login():
    login_details = {"user1": "12345",
                     "user2": "54321"}
    entered_username = username.get()
    entered_password = password.get()

    if entered_username in login_details and entered_password == login_details[entered_username]:
        username_label.destroy()
        username.destroy()
        password_label.destroy()
        password.destroy()
        submit_login_button.destroy()
        choose_quiz_type()
    else:
        print("Login failed")


def choose_quiz_type():
    quiz_choice_label.pack()
    addition_button.pack()
    subtraction_button.pack()
    multiplication_button.pack()
    division_button.pack()


def addition_quiz():
    pass


def subtraction_quiz():
    pass


def multiplication_quiz():
    pass


def division_quiz():
    pass


window = Tk()
window.resizable(False, False)

monitor_width = window.winfo_screenwidth()
monitor_height = window.winfo_screenheight()

x = int((monitor_width / 2) - (SCREEN_HEIGHT / 2))  # Used to center the window
y = int((monitor_height / 2) - (SCREEN_WIDTH / 2))
window.geometry(f"{SCREEN_HEIGHT}x{SCREEN_WIDTH}+{x}+{y}")

# Buttons
login_button = Button(text="Login", command=login, font=("Consolas", 30),
                      fg="#00ff00", bg="black", activebackground="lightgrey")
login_button.pack(side=LEFT)

signup_button = Button(text="Sign Up", command=sign_up, font=("Consolas", 30),
                       fg="#00ff00", bg="black", activebackground="lightgrey")
signup_button.pack(side=RIGHT)
submit_login_button = Button(text="Login", command=submit_login, font=("Consolas", 30),
                             fg="#00ff00", bg="black", activebackground="lightgrey")

addition_button = Button(text="Addition", command=addition_quiz, font=("Consolas", 30),
                         fg="#00ff00", bg="black", activebackground="lightgrey")
subtraction_button = Button(text="Subtraction", command=subtraction_quiz, font=("Consolas", 30),
                            fg="#00ff00", bg="black", activebackground="lightgrey")
multiplication_button = Button(text="Multiplication", command=multiplication_quiz, font=("Consolas", 30),
                               fg="#00ff00", bg="black", activebackground="lightgrey")
division_button = Button(text="Division", command=division_quiz, font=("Consolas", 30),
                         fg="#00ff00", bg="black", activebackground="lightgrey")

# Entry boxes
username = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black")
password = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black", show="*")

# Labels
username_label = Label(window, text="Username: ", font=("Consolas", 30), fg="black")
password_label = Label(window, text="Password: ", font=("Consolas", 30), fg="black")
quiz_choice_label = Label(window, text="Choose Quiz Type", font=("Consolas", 30), fg="black")

score = 0

if __name__ == '__main__':
    window.mainloop()
