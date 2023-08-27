import csv
from tkinter import *
import pandas as pd
import random

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
QUIZ_QUESTIONS = 10
SCORES_FILE = "scores.csv"
USER_DETAILS_FILE = "users.csv"


def starting_page():
    login_button = Button(text="Login", command=lambda: login(login_button, signup_button, view_scores_button),
                          font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    login_button.pack(side=LEFT)

    signup_button = Button(text="Sign Up", command=lambda: sign_up(login_button, signup_button, view_scores_button),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    signup_button.pack(side=RIGHT)
    view_scores_button = Button(text="View Scores", command=lambda: choose_scores(login_button, signup_button,
                                                                                  view_scores_button),
                                font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    view_scores_button.pack(side=TOP)


def choose_scores(login_button, signup_button, view_scores_button):
    login_button.destroy()
    signup_button.destroy()
    view_scores_button.destroy()

    all_scores_button = Button(text="View All Scores", command=lambda: view_all_scores(all_scores_button),
                               font=("Consolas", 30),
                               fg="#00ff00", bg="black", activebackground="lightgrey")
    all_scores_button.pack()


def view_all_scores(all_scores_button):
    all_scores_button.destroy()
    all_scores = pd.read_csv(SCORES_FILE, header=None)
    rows, cols = (len(all_scores.index), 5)
    all_scores_arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(0, len(all_scores.index)):
        for j in range(0, 4):
            all_scores_arr[i][j] = all_scores.loc[i][j]
        all_scores_arr[i][4] = all_scores.loc[i][1] / all_scores.loc[i][2]
    all_scores_arr.sort(key=lambda x: x[4], reverse=True)  # Sorts list by second value
    if len(all_scores_arr) > 5:
        top_scores = 5
    else:
        top_scores = len(all_scores_arr)
    scores_frame = Frame(window,  # Frame added to window, widgets added to frames
                         bd=20,
                         relief=RAISED  # Border type is raised
                         )
    scores_frame.pack()
    title_label = Label(scores_frame, text="Top 5 Scores", font=("Consolas", 20), fg="black")
    title_label.pack()
    for i in range(0, top_scores):
        score_label = Label(scores_frame, text=f"User: {all_scores_arr[i][0]},\n Score: {all_scores_arr[i][1]}/"
                                               f"{all_scores_arr[i][2]},\n Quiz Type: {all_scores_arr[i][3]}\n",
                            font=("Consolas", 18), fg="black")
        score_label.pack()
    return_button = Button(scores_frame, text="Return to Main Menu",
                           command=lambda: return_to_main(scores_frame),
                           font=("Consolas", 20), fg="#00ff00", bg="black", activebackground="lightgrey")
    return_button.pack()


def return_to_main(scores_frame):
    scores_frame.destroy()
    starting_page()


def login(login_button, signup_button, view_scores_button):
    login_button.destroy()
    signup_button.destroy()
    view_scores_button.destroy()

    username = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black")
    password = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black", show="*")
    username_label = Label(window, text="Username: ", font=("Consolas", 30), fg="black")
    password_label = Label(window, text="Password: ", font=("Consolas", 30), fg="black")
    submit_button = Button(text="Login", command=lambda: submit_login(username, password, username_label,
                                                                      password_label, submit_button),
                           font=("Consolas", 30),
                           fg="#00ff00", bg="black", activebackground="lightgrey")

    username_label.place(x=10, y=10)
    username.place(x=250, y=20)
    password_label.place(x=10, y=100)
    password.place(x=250, y=110)
    submit_button.place(x=300, y=250)


def sign_up(login_button, signup_button, view_scores_button):
    login_button.destroy()
    signup_button.destroy()
    view_scores_button.destroy()

    username = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black")
    password = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black", show="*")
    confirm_password = Entry(window, font=("Consolas", 20), fg="#00ff00", bg="black", show="*")
    username_label = Label(window, text="Username: ", font=("Consolas", 30), fg="black")
    password_label = Label(window, text="Password: ", font=("Consolas", 30), fg="black")
    confirm_password_label = Label(window, text="Confirm Password: ", font=("Consolas", 30), fg="black")
    submit_button = Button(text="Sign Up", command=lambda: submit_signup(username, password, confirm_password,
                                                                         username_label, password_label,
                                                                         confirm_password_label, submit_button),
                           font=("Consolas", 30),
                           fg="#00ff00", bg="black", activebackground="lightgrey")
    username_label.place(x=10, y=10)
    username.place(x=250, y=20)
    password_label.place(x=10, y=100)
    password.place(x=250, y=110)
    confirm_password_label.place(x=10, y=190)
    confirm_password.place(x=450, y=200)
    submit_button.place(x=300, y=350)


def submit_login(username, password, username_label, password_label, submit_button):
    global entered_user
    user_details = pd.read_csv(USER_DETAILS_FILE, header=None)  # Gets all the details from the users file
    entered_username = username.get()
    entered_password = password.get()
    for i in range(0, len(user_details.index)):
        # In .loc[x][y], x is the row no and y is the column no
        if entered_username == user_details.loc[i][0] and entered_password == str(user_details.loc[i][1]):
            entered_user = entered_username
            username_label.destroy()
            username.destroy()
            password_label.destroy()
            password.destroy()
            submit_button.destroy()
            choose_quiz_type()
    print("Login failed")


def submit_signup(username, password, confirm_password, username_label, password_label, confirm_password_label,
                  submit_button):
    username_str = str(username.get())
    password_str = str(password.get())
    confirm_password_str = str(confirm_password.get())
    if 5 <= len(username_str) <= 15 and 5 <= len(password_str) <= 15 and password_str == confirm_password_str:
        with open(USER_DETAILS_FILE, "a") as users_file:
            csv_writer = csv.writer(users_file)
            csv_writer.writerow([username_str, password_str])
        remove_white_lines = pd.read_csv(USER_DETAILS_FILE)  # Removes whitespace in the file
        remove_white_lines.to_csv(USER_DETAILS_FILE, index=False)
        username_label.destroy()
        username.destroy()
        password_label.destroy()
        password.destroy()
        confirm_password_label.destroy()
        confirm_password.destroy()
        submit_button.destroy()
        starting_page()
    else:
        print("Sign up failed")


def choose_quiz_type():
    quiz_choice_label = Label(window, text="Choose Quiz Type", font=("Consolas", 30), fg="black")
    addition_button = Button(text="Addition",
                             command=lambda: quiz_game(quiz_choice_label, addition_button,
                                                       subtraction_button, multiplication_button, division_button,
                                                       "addition"),
                             font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    subtraction_button = Button(text="Subtraction",
                                command=lambda: quiz_game(quiz_choice_label, addition_button,
                                                          subtraction_button, multiplication_button,
                                                          division_button, "subtraction"),
                                font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    multiplication_button = Button(text="Multiplication",
                                   command=lambda: quiz_game(quiz_choice_label, addition_button,
                                                             subtraction_button, multiplication_button,
                                                             division_button, "multiplication"),
                                   font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    division_button = Button(text="Division",
                             command=lambda: quiz_game(quiz_choice_label, addition_button,
                                                       subtraction_button, multiplication_button, division_button,
                                                       "division"),
                             font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    quiz_choice_label.pack()
    addition_button.pack()
    subtraction_button.pack()
    multiplication_button.pack()
    division_button.pack()


def quiz_game(quiz_choice_label, addition_button, subtraction_button, multiplication_button, division_button,
              quiz_type):
    global answer
    global score
    global question_number
    question_number_label = Label(window, text="Question {}".format(question_number), font=("Consolas", 30), fg="black")
    question_label = Label(window, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    answer_entry = Entry(window, font=("Consolas", 30), fg="#00ff00", bg="black")
    submit_button = Button(text="Check Answer",
                           command=lambda: check_answer(answer_entry, question_number_label, question_label,
                                                        submit_button, score_label, quiz_choice_label, addition_button,
                                                        subtraction_button, multiplication_button, division_button,
                                                        quiz_type),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    score_label = Label(window, text="PLACEHOLDER", font=("Consolas", 30), fg="black")

    if question_number <= QUIZ_QUESTIONS:
        if question_number == 1:
            quiz_choice_label.destroy()
            addition_button.destroy()
            subtraction_button.destroy()
            multiplication_button.destroy()
            division_button.destroy()
        match quiz_type:
            case "addition":
                num1 = random.randint(1, 200)
                num2 = random.randint(1, 200)
                answer = num1 + num2
                question_label.config(text=f"What is {num1} + {num2}?")
            case "subtraction":
                num1 = random.randint(1, 200)
                num2 = random.randint(1, 200)
                answer = num1 - num2
                question_label.config(text=f"What is {num1} - {num2}?")
            case "multiplication":
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)
                answer = num1 * num2
                question_label.config(text=f"What is {num1} * {num2}?")
            case "division":
                num1 = random.randint(1, 200)
                num2 = random.randint(1, 200)
                answer = num1 / num2
                question_label.config(text=f"What is {num1} / {num2}?")
        question_number_label.pack()
        question_label.pack()
        answer_entry.pack()
        submit_button.pack()
        score_label.config(text=f"Score: {score}/{question_number - 1}")
        score_label.pack()
    else:
        question_number_label.destroy()
        question_label.destroy()
        answer_entry.destroy()
        submit_button.destroy()
        score_label.destroy()
        save_score(quiz_type)


def check_answer(answer_entry, question_number_label, question_label, submit_button, score_label, quiz_choice_label,
                 addition_button, subtraction_button, multiplication_button, division_button, quiz_type):
    global answer
    global score
    global question_number
    try:
        if answer == int(answer_entry.get()):
            score += 1
        question_number += 1
        question_number_label.destroy()
        question_label.destroy()
        answer_entry.destroy()
        submit_button.destroy()
        score_label.destroy()
        quiz_game(quiz_choice_label, addition_button, subtraction_button, multiplication_button, division_button,
                  quiz_type)
    except ValueError:
        pass


def save_score(quiz_type):
    global score
    global question_number
    global entered_user
    results_label = Label(window, text="Well done, you got: {} / {}".format(score, question_number - 1),
                          font=("Consolas", 30), fg="black")
    logout_button = Button(text="Log out", command=lambda: endgame(results_label, logout_button, restart_button,
                                                                   "logout"),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    restart_button = Button(text="Do Another Quiz", command=lambda: endgame(results_label, logout_button, restart_button
                                                                            , "restart"),
                            font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    with open(SCORES_FILE, "a") as scores_file:
        csv_writer = csv.writer(scores_file)
        csv_writer.writerow([entered_user, score, QUIZ_QUESTIONS, quiz_type])
    remove_white_lines = pd.read_csv(SCORES_FILE)  # Removes whitespace in the file
    remove_white_lines.to_csv(SCORES_FILE, index=False)
    results_label.pack()
    logout_button.pack()
    restart_button.pack()


def endgame(results_label, logout_button, restart_button, end_game):
    global score
    global question_number
    score = 0
    question_number = 1
    results_label.destroy()
    logout_button.destroy()
    restart_button.destroy()
    starting_page() if end_game == "logout" else choose_quiz_type()


window = Tk()
window.resizable(False, False)

monitor_width = window.winfo_screenwidth()
monitor_height = window.winfo_screenheight()

x = int((monitor_width / 2) - (SCREEN_HEIGHT / 2))  # Used to center the window
y = int((monitor_height / 2) - (SCREEN_WIDTH / 2))
window.geometry(f"{SCREEN_HEIGHT}x{SCREEN_WIDTH}+{x}+{y}")

score = 0
answer = 0
question_number = 1
entered_user = ""

starting_page()

if __name__ == '__main__':
    window.mainloop()
