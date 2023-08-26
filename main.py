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
    quiz_choice_label = Label(window, text="Choose Quiz Type", font=("Consolas", 30), fg="black")
    addition_button = Button(text="Addition",
                             command=lambda: addition_quiz(quiz_choice_label, addition_button,
                                                           subtraction_button, multiplication_button, division_button),
                             font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    subtraction_button = Button(text="Subtraction",
                                command=lambda: subtraction_quiz(quiz_choice_label, addition_button,
                                                                 subtraction_button, multiplication_button,
                                                                 division_button),
                                font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    multiplication_button = Button(text="Multiplication",
                                   command=lambda: multiplication_quiz(quiz_choice_label, addition_button,
                                                                       subtraction_button, multiplication_button,
                                                                       division_button),
                                   font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    division_button = Button(text="Division",
                             command=lambda: division_quiz(quiz_choice_label, addition_button,
                                                           subtraction_button, multiplication_button, division_button),
                             font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    quiz_choice_label.pack()
    addition_button.pack()
    subtraction_button.pack()
    multiplication_button.pack()
    division_button.pack()


def addition_quiz(quiz_choice_label, addition_button, subtraction_button, multiplication_button, division_button):
    global answer
    global score
    global question_number
    global quiz_type
    quiz_type = "add"
    question_label = Label(window, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    answer_entry = Entry(window, font=("Consolas", 30), fg="#00ff00", bg="black")
    submit_button = Button(text="Check Answer",
                           command=lambda: check_answer(answer_entry, question_label, submit_button, score_label,
                                                        quiz_choice_label, addition_button, subtraction_button,
                                                        multiplication_button, division_button),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    score_label = Label(window, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    if question_number <= QUIZ_QUESTIONS:
        if question_number == 1:
            quiz_choice_label.destroy()
            addition_button.destroy()
            subtraction_button.destroy()
            multiplication_button.destroy()
            division_button.destroy()
        num1 = random.randint(1, 200)
        num2 = random.randint(1, 200)
        answer = num1 + num2
        question_label.config(text=f"What is {num1} + {num2}?")
        question_label.pack()
        answer_entry.pack()
        submit_button.pack()
        score_label.config(text=f"Score: {score}/{question_number - 1}")
        score_label.pack()
    else:
        score = 0
        question_number = 1
        question_label.destroy()
        answer_entry.destroy()
        submit_button.destroy()
        score_label.destroy()
        choose_quiz_type()


def subtraction_quiz(quiz_choice_label, addition_button, subtraction_button, multiplication_button, division_button):
    global answer
    global score
    global question_number
    global quiz_type
    quiz_type = "sub"
    question_label = Label(window, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    answer_entry = Entry(window, font=("Consolas", 30), fg="#00ff00", bg="black")
    submit_button = Button(text="Check Answer",
                           command=lambda: check_answer(answer_entry, question_label, submit_button, score_label,
                                                        quiz_choice_label, addition_button, subtraction_button,
                                                        multiplication_button, division_button),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    score_label = Label(window, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    if question_number <= QUIZ_QUESTIONS:
        if question_number == 1:
            quiz_choice_label.destroy()
            addition_button.destroy()
            subtraction_button.destroy()
            multiplication_button.destroy()
            division_button.destroy()
        num1 = random.randint(1, 200)
        num2 = random.randint(1, 200)
        answer = num1 - num2
        question_label.config(text=f"What is {num1} - {num2}?")
        question_label.pack()
        answer_entry.pack()
        submit_button.pack()
        score_label.config(text=f"Score: {score}/{question_number - 1}")
        score_label.pack()
    else:
        score = 0
        question_number = 1
        question_label.destroy()
        answer_entry.destroy()
        submit_button.destroy()
        score_label.destroy()
        choose_quiz_type()


def multiplication_quiz(quiz_choice_label, addition_button, subtraction_button, multiplication_button, division_button):
    global answer
    global score
    global question_number
    global quiz_type
    quiz_type = "mul"
    question_label = Label(window, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    answer_entry = Entry(window, font=("Consolas", 30), fg="#00ff00", bg="black")
    submit_button = Button(text="Check Answer",
                           command=lambda: check_answer(answer_entry, question_label, submit_button, score_label,
                                                        quiz_choice_label, addition_button, subtraction_button,
                                                        multiplication_button, division_button),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    score_label = Label(window, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    if question_number <= QUIZ_QUESTIONS:
        if question_number == 1:
            quiz_choice_label.destroy()
            addition_button.destroy()
            subtraction_button.destroy()
            multiplication_button.destroy()
            division_button.destroy()
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        answer = num1 * num2
        question_label.config(text=f"What is {num1} * {num2}?")
        question_label.pack()
        answer_entry.pack()
        submit_button.pack()
        score_label.config(text=f"Score: {score}/{question_number - 1}")
        score_label.pack()
    else:
        score = 0
        question_number = 1
        question_label.destroy()
        answer_entry.destroy()
        submit_button.destroy()
        score_label.destroy()
        choose_quiz_type()


def division_quiz(quiz_choice_label, addition_button, subtraction_button, multiplication_button, division_button):
    global answer
    global score
    global question_number
    global quiz_type
    quiz_type = "div"
    question_label = Label(window, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    answer_entry = Entry(window, font=("Consolas", 30), fg="#00ff00", bg="black")
    submit_button = Button(text="Check Answer",
                           command=lambda: check_answer(answer_entry, question_label, submit_button, score_label,
                                                        quiz_choice_label, addition_button, subtraction_button,
                                                        multiplication_button, division_button),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    score_label = Label(window, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    if question_number <= QUIZ_QUESTIONS:
        if question_number == 1:
            quiz_choice_label.destroy()
            addition_button.destroy()
            subtraction_button.destroy()
            multiplication_button.destroy()
            division_button.destroy()
        num1 = random.randint(1, 200)
        num2 = random.randint(1, 200)
        answer = num1 / num2
        question_label.config(text=f"What is {num1} / {num2}?")
        question_label.pack()
        answer_entry.pack()
        submit_button.pack()
        score_label.config(text=f"Score: {score}/{question_number - 1}")
        score_label.pack()
    else:
        score = 0
        question_number = 1
        question_label.destroy()
        answer_entry.destroy()
        submit_button.destroy()
        score_label.destroy()
        choose_quiz_type()


def check_answer(answer_entry, question_label, submit_button, score_label, quiz_choice_label, addition_button,
                 subtraction_button, multiplication_button, division_button):
    global answer
    global score
    global question_number
    global quiz_type

    if answer == int(answer_entry.get()):
        score += 1
    question_number += 1
    question_label.destroy()
    answer_entry.destroy()
    submit_button.destroy()
    score_label.destroy()
    if quiz_type == "add":
        addition_quiz(quiz_choice_label, addition_button, subtraction_button, multiplication_button, division_button)
    elif quiz_type == "sub":
        subtraction_quiz(quiz_choice_label, addition_button, subtraction_button, multiplication_button, division_button)
    elif quiz_type == "mul":
        multiplication_quiz(quiz_choice_label, addition_button, subtraction_button, multiplication_button,
                            division_button)
    else:
        division_quiz(quiz_choice_label, addition_button, subtraction_button, multiplication_button, division_button)


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

# Entry boxes
username = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black")
password = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black", show="*")

# Labels
username_label = Label(window, text="Username: ", font=("Consolas", 30), fg="black")
password_label = Label(window, text="Password: ", font=("Consolas", 30), fg="black")

score = 0
answer = 0
question_number = 1
quiz_type = "add"

if __name__ == '__main__':
    window.mainloop()
