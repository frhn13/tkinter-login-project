from tkinter import *
import pandas as pd

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800


def login():
    login_button.destroy()
    signup_button.destroy()
    username_label = Label(window, text="Username: ", font=("Consolas", 30), fg="black")
    username_label.place(x=10, y=10)
    username.place(x=250, y=20)
    password_label = Label(window, text="Password: ", font=("Consolas", 30), fg="black")
    password_label.place(x=10, y=100)
    password.place(x=250, y=110)
    submit_button = Button(text="Login", command=submit_login, font=("Consolas", 30),
                           fg="#00ff00", bg="black", activebackground="lightgrey")
    submit_button.place(x=300, y=250)


def sign_up():
    pass


def submit_login():
    login_details = {"user1": "12345",
                     "user2": "54321"}
    entered_username = username.get()
    entered_password = password.get()

    if entered_username in login_details and entered_password == login_details[entered_username]:
        print("Yay")
    else:
        print("Login failed")


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

# Entry boxes
username = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black")
password = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black", show="*")

if __name__ == '__main__':
    window.mainloop()
