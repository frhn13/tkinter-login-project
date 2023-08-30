import csv
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
from database_functions import tables_setup


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
QUIZ_QUESTIONS = 10
SCORES_FILE = "scores.csv"
USER_DETAILS_FILE = "users.csv"


def starting_page():
    window_frame = Frame(window, bd=20, relief=RAISED, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    login_button = Button(window_frame, text="Login",
                          command=lambda: login(window_frame),
                          font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    login_button.pack(side=LEFT)

    signup_button = Button(window_frame, text="Sign Up",
                           command=lambda: sign_up(window_frame),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    signup_button.pack(side=RIGHT)
    view_scores_button = Button(window_frame, text="View Scores",
                                command=lambda: choose_scores(window_frame),
                                font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    view_scores_button.pack(side=TOP)
    window_frame.pack()
    # Adapted from https://www.tutorialkart.com/python/tkinter/tkinter-frame-width-height-not-working/#gsc.tab=0
    window_frame.pack_propagate(0)  # Needed to make frame take up specified width and height


def choose_scores(window_frame):
    window_frame.destroy()
    button_frame = Frame(window, bd=20, relief=RAISED)
    all_scores_button = Button(button_frame, text="View All Scores",
                               command=lambda: view_scores(button_frame, "all"),
                               font=("Consolas", 30),
                               fg="#00ff00", bg="black", activebackground="lightgrey")
    all_add_scores_button = Button(button_frame, text="View Addition Scores",
                                   command=lambda: view_scores(button_frame, "addition"),
                                   font=("Consolas", 30),
                                   fg="#00ff00", bg="black", activebackground="lightgrey")
    all_sub_scores_button = Button(button_frame, text="View Subtraction Scores",
                                   command=lambda: view_scores(button_frame, "subtraction"),
                                   font=("Consolas", 30),
                                   fg="#00ff00", bg="black", activebackground="lightgrey")
    all_mul_scores_button = Button(button_frame, text="View Multiplication Scores",
                                   command=lambda: view_scores(button_frame, "multiplication"),
                                   font=("Consolas", 30),
                                   fg="#00ff00", bg="black", activebackground="lightgrey")
    all_div_scores_button = Button(button_frame, text="View Division Scores",
                                   command=lambda: view_scores(button_frame, "division"),
                                   font=("Consolas", 30),
                                   fg="#00ff00", bg="black", activebackground="lightgrey")
    button_frame.pack()
    all_scores_button.pack()
    all_add_scores_button.pack()
    all_sub_scores_button.pack()
    all_mul_scores_button.pack()
    all_div_scores_button.pack()


def view_scores(button_frame, quiz_type):
    button_frame.destroy()
    all_scores = pd.read_csv(SCORES_FILE, header=None)
    rows, cols = (len(all_scores.index), 5)
    all_scores_arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(0, len(all_scores.index)):
        for j in range(0, 4):
            all_scores_arr[i][j] = all_scores.loc[i][j]
        all_scores_arr[i][1] = round(all_scores.loc[i][1], 0)
        all_scores_arr[i][2] = round(all_scores.loc[i][2], 0)
        all_scores_arr[i][4] = all_scores.loc[i][1] / all_scores.loc[i][2]
    all_scores_arr.sort(key=lambda i: i[4], reverse=True)  # Sorts list by second value
    scores_frame = Frame(window,  # Frame added to window, widgets added to frames
                         bd=20,
                         relief=RAISED  # Border type is raised
                         )
    scores_frame.pack()
    title_label = Label(scores_frame, text="Up To Top 5 Scores\n", font=("Consolas", 20), fg="black")
    title_label.pack()
    counter = 0
    for i in range(0, len(all_scores_arr)):
        if counter < 5 and (quiz_type == "all" or quiz_type == all_scores_arr[i][3]):
            score_label = Label(scores_frame, text=f"User: {all_scores_arr[i][0]},\n Score: {all_scores_arr[i][1]}/"
                                                   f"{all_scores_arr[i][2]},\n Quiz Type: {all_scores_arr[i][3]}\n",
                                font=("Consolas", 18), fg="black")
            score_label.pack()
            counter += 1
    return_button = Button(scores_frame, text="Return to Main Menu",
                           command=lambda: return_to_main(scores_frame),
                           font=("Consolas", 20), fg="#00ff00", bg="black", activebackground="lightgrey")
    return_button.pack()


def return_to_main(scores_frame):
    scores_frame.destroy()
    starting_page()


def login(window_frame):
    window_frame.destroy()

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


def sign_up(window_frame):
    window_frame.destroy()

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
    logged_in = False
    user_details = pd.read_csv(USER_DETAILS_FILE, header=None)  # Gets all the details from the users file
    entered_username = username.get()
    entered_password = password.get()
    for i in range(0, len(user_details.index)):
        # In .loc[x][y], x is the row no and y is the column no
        if entered_username == user_details.loc[i][0] and entered_password == str(user_details.loc[i][1]):
            logged_in = True
            entered_user = entered_username
            username_label.destroy()
            username.destroy()
            password_label.destroy()
            password.destroy()
            submit_button.destroy()
            choose_quiz_type()
    if not logged_in:
        messagebox.showerror(title="Login Failed", message="Username and password aren't recognised")


def submit_signup(username, password, confirm_password, username_label, password_label, confirm_password_label,
                  submit_button):
    username_str = str(username.get())
    password_str = str(password.get())
    confirm_password_str = str(confirm_password.get())
    has_digit = False
    has_upper = False
    has_lower = False
    for i in password_str:
        if i.isdigit():
            has_digit = True
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True
    if len(username_str) > 15 or len(username_str) < 5:
        messagebox.showerror(title="Sign Up Failed", message="Username should be between 5 and 15 characters")
    elif len(username_str) > 15 or len(username_str) < 5:
        messagebox.showerror(title="Sign Up Failed", message="Password should be between 5 and 15 characters")
    elif password_str != confirm_password_str:
        messagebox.showerror(title="Sign Up Failed", message="Passwords don't match")
    elif not has_digit:
        messagebox.showerror(title="Sign Up Failed", message="Password must include a digit")
    elif not has_lower or not has_upper:
        messagebox.showerror(title="Sign Up Failed", message="Password must include an upper and lowercase letter")
    else:
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


def choose_quiz_type():
    quiz_frame = Frame(window, bd=20, relief=RAISED, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    quiz_choice_label = Label(quiz_frame, text="Choose Quiz Type", font=("Consolas", 30), fg="black")
    addition_button = Button(quiz_frame, text="Addition",
                             command=lambda: quiz_setup(quiz_frame, questions_entry, "addition"),
                             font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    subtraction_button = Button(quiz_frame, text="Subtraction",
                                command=lambda: quiz_setup(quiz_frame, questions_entry, "subtraction"),
                                font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    multiplication_button = Button(quiz_frame, text="Multiplication",
                                   command=lambda: quiz_setup(quiz_frame, questions_entry, "multiplication"),
                                   font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    division_button = Button(quiz_frame, text="Division",
                             command=lambda: quiz_setup(quiz_frame, questions_entry, "division"),
                             font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    no_questions_label = Label(quiz_frame, text="No of Questions", font=("Consolas", 30), fg="black")
    questions_entry = Entry(quiz_frame, font=("Consolas", 30), fg="#00ff00", bg="black")
    questions_entry.insert(0, 20)
    quiz_frame.pack()
    quiz_frame.pack_propagate(0)
    quiz_choice_label.pack()
    addition_button.pack()
    subtraction_button.pack()
    multiplication_button.pack()
    division_button.pack()
    no_questions_label.pack()
    questions_entry.pack()


def quiz_setup(quiz_frame, questions_entry, quiz_type):
    global no_of_questions
    try:
        no_of_questions = int(questions_entry.get())
        if no_of_questions < 5:
            messagebox.showerror(title="Answer Invalid", message="Number of Questions must be more than 5")
        elif no_of_questions > 50:
            messagebox.showerror(title="Answer Invalid", message="Number of Questions must be less than 50")
        else:
            quiz_frame.destroy()
            quiz_game(quiz_type)
    except ValueError:
        messagebox.showerror(title="Answer Invalid", message="Number of Questions must be an Integer")


def quiz_game(quiz_type):
    global answer
    global score
    global question_number
    global no_of_questions
    quiz_game_frame = Frame(window, bd=20, relief=RAISED, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    question_number_label = Label(quiz_game_frame, text="Question {}".format(question_number), font=("Consolas", 30),
                                  fg="black")
    question_label = Label(quiz_game_frame, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    answer_entry = Entry(quiz_game_frame, font=("Consolas", 30), fg="#00ff00", bg="black")
    submit_button = Button(quiz_game_frame, text="Check Answer",
                           command=lambda: check_answer(answer_entry, quiz_game_frame, quiz_type),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    score_label = Label(quiz_game_frame, text="PLACEHOLDER", font=("Consolas", 30), fg="black")

    if question_number <= no_of_questions:
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
                num1 = random.randint(1, 400)
                num2 = random.randint(1, 50)
                while num1 % num2 != 0:
                    num1 = random.randint(1, 200)
                    num2 = random.randint(1, 50)
                    answer = num1 / num2
                question_label.config(text=f"What is {num1} / {num2}?")
        question_number_label.pack()
        question_label.pack()
        answer_entry.pack()
        submit_button.pack()
        score_label.config(text=f"Score: {score}/{question_number - 1}")
        score_label.pack()
        quiz_game_frame.pack()
        quiz_game_frame.pack_propagate(0)
    else:
        quiz_game_frame.destroy()
        save_score(quiz_type)


def check_answer(answer_entry, quiz_game_frame, quiz_type):
    global answer
    global score
    global question_number
    try:
        if answer == int(answer_entry.get()):
            score += 1
        question_number += 1
        quiz_game_frame.destroy()
        quiz_game(quiz_type)
    except ValueError:
        messagebox.showerror(title="Answer Invalid", message="Answer can only be an integer")


def save_score(quiz_type):
    global score
    global question_number
    global entered_user
    global no_of_questions
    results_label = Label(window, text="Well done, you got: {} / {}".format(score, question_number - 1),
                          font=("Consolas", 30), fg="black")
    logout_button = Button(text="Log out", command=lambda: endgame(results_label, logout_button, restart_button,
                                                                   "logout"),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    restart_button = Button(text="Do Another Quiz", command=lambda: endgame(results_label, logout_button,
                                                                            restart_button, "restart"),
                            font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    with open(SCORES_FILE, "a") as scores_file:
        csv_writer = csv.writer(scores_file)
        csv_writer.writerow([entered_user, score, no_of_questions, quiz_type])
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
window.title("Quiz Game")

monitor_width = window.winfo_screenwidth()
monitor_height = window.winfo_screenheight()

x = int((monitor_width / 2) - (SCREEN_HEIGHT / 2))  # Used to center the window
y = int((monitor_height / 2) - (SCREEN_WIDTH / 2))
window.geometry(f"{SCREEN_HEIGHT}x{SCREEN_WIDTH}+{x}+{y}")

score = 0
answer = 0
question_number = 1
no_of_questions = 0
entered_user = ""

starting_page()

if __name__ == '__main__':
    tables_setup()
    window.mainloop()
