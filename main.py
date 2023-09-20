from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
from database_functions import tables_setup, add_user, compare_user, add_score, display_scores, display_user_scores, \
    display_quiz_id, add_question, add_quiz, display_quiz_questions, display_quizzes, update_question, \
    display_full_quiz_questions

SCREEN_HEIGHT = 900
SCREEN_WIDTH = 800
QUIZ_QUESTIONS = 10


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
                               command=lambda: choose_user(button_frame, "all"),
                               font=("Consolas", 30),
                               fg="#00ff00", bg="black", activebackground="lightgrey")
    all_add_scores_button = Button(button_frame, text="View Addition Scores",
                                   command=lambda: choose_user(button_frame, "addition"),
                                   font=("Consolas", 30),
                                   fg="#00ff00", bg="black", activebackground="lightgrey")
    all_sub_scores_button = Button(button_frame, text="View Subtraction Scores",
                                   command=lambda: choose_user(button_frame, "subtraction"),
                                   font=("Consolas", 30),
                                   fg="#00ff00", bg="black", activebackground="lightgrey")
    all_mul_scores_button = Button(button_frame, text="View Multiplication Scores",
                                   command=lambda: choose_user(button_frame, "multiplication"),
                                   font=("Consolas", 30),
                                   fg="#00ff00", bg="black", activebackground="lightgrey")
    all_div_scores_button = Button(button_frame, text="View Division Scores",
                                   command=lambda: choose_user(button_frame, "division"),
                                   font=("Consolas", 30),
                                   fg="#00ff00", bg="black", activebackground="lightgrey")
    button_frame.pack()
    all_scores_button.pack()
    all_add_scores_button.pack()
    all_sub_scores_button.pack()
    all_mul_scores_button.pack()
    all_div_scores_button.pack()


def choose_user(button_frame, quiz_type):
    button_frame.destroy()
    all_user_check = BooleanVar()
    users_frame = Frame(window, bd=20, relief=RAISED)
    all_users_button = Checkbutton(users_frame, text="View scores from all users?", font=("Consolas", 20),
                                   variable=all_user_check, fg="#00ff00", bg="black", activebackground="lightgrey")
    chosen_user_entry = Entry(users_frame, font=("Consolas", 20), fg="#00ff00", bg="black")
    chosen_user_label = Label(users_frame, text="Username to View: ", font=("Consolas", 30), fg="black")
    submit_user_button = Button(users_frame, text="View Scores",
                                command=lambda: find_scores(users_frame, chosen_user_entry, all_user_check,
                                                            quiz_type),
                                font=("Consolas", 30),
                                fg="#00ff00", bg="black", activebackground="lightgrey")

    users_frame.pack()
    all_users_button.pack()
    submit_user_button.pack()
    chosen_user_label.pack()
    chosen_user_entry.pack()


def find_scores(users_frame, chosen_user_entry, all_user_check, quiz_type):
    if all_user_check.get():
        scores = display_scores(quiz_type)
    else:
        scores = display_user_scores(chosen_user_entry.get(), quiz_type)
    users_frame.destroy()
    scores.sort(key=lambda i: i[4], reverse=True)  # Sorts list by 5th value (percentage)
    view_scores(scores)


def view_scores(scores):
    scores_frame = Frame(window,  # Frame added to window, widgets added to frames
                         bd=20,
                         relief=RAISED  # Border type is raised
                         )
    scores_frame.pack()
    title_label = Label(scores_frame,
                        text="Top 5 Scores\n" if len(scores) > 5 else f"Top {len(scores)} Scores\n",
                        font=("Consolas", 20), fg="black")
    title_label.grid(row=0, column=0, columnspan=2)
    counter = 0
    for i in range(0, len(scores)):
        if counter < 5:
            score_label = Label(scores_frame, text=f"{counter + 1}) User: {scores[i][0]},\n Score: {scores[i][1]}/"
                                                   f"{scores[i][2]},\n Quiz Type: {scores[i][3]}\n",
                                font=("Consolas", 18), fg="black")
            score_label.grid(row=i + 1, column=0, columnspan=2)
            counter += 1
        else:
            break
    quiz_label = Label(scores_frame, text="Enter Number of Quiz to make Report for", font=("Consolas", 20), fg="black")
    quiz_report_button = Button(scores_frame, text="View Quiz Report",
                                command=lambda: menu_quiz_validation(scores_frame, quiz_report_entry.get(), scores),
                                font=("Consolas", 20), fg="#00ff00", bg="black", activebackground="lightgrey")

    quiz_report_entry = Entry(scores_frame, font=("Consolas", 20), fg="#00ff00", bg="black")
    quiz_label.grid(row=6, column=0, columnspan=2)
    quiz_report_entry.grid(row=7, column=0)
    quiz_report_button.grid(row=7, column=1)
    return_button = Button(scores_frame, text="Return to Main Menu",
                           command=lambda: return_to_main(scores_frame),
                           font=("Consolas", 20), fg="#00ff00", bg="black", activebackground="lightgrey")
    return_button.grid(row=8, column=0, columnspan=2)


def menu_quiz_validation(scores_frame, score_number, scores):
    try:
        if int(score_number) > len(scores) or int(score_number) > 5 or int(score_number) < 1:
            messagebox.showerror(title="Input Invalid", message="Quiz Number entered is not valid")
        else:
            scores_frame.destroy()
            menu_quiz_report(scores[int(score_number) - 1], scores)
    except ValueError:
        messagebox.showerror(title="Input Invalid", message="Quiz Number entered is not an integer")


def menu_quiz_report(score, scores):
    report_frame = Frame(window, bd=20, relief=RAISED, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    report_frame.pack()
    report_frame.pack_propagate(0)
    report_canvas = Canvas(report_frame)
    report_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    scrollbar = ttk.Scrollbar(report_frame, orient=VERTICAL, command=report_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    report_canvas.configure(yscrollcommand=scrollbar.set)
    report_canvas.bind("<Configure>", lambda e: report_canvas.configure(scrollregion=report_canvas.bbox("all")))
    second_frame = Frame(report_canvas)
    report_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    quiz_questions = display_quiz_questions(score[5])
    quizzes_button = Button(second_frame, text="Return to Scores",
                            command=lambda: return_to_scores(report_frame, scores),
                            font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    return_button = Button(second_frame, text="Return to Main Menu", command=lambda: return_to_main(report_frame),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")

    for i in range(len(quiz_questions)):
        if quiz_questions[i][2] == "True":
            score_label = Label(second_frame, text=f"Question: {quiz_questions[i][0]},\n Correct?: "
                                                   f"{quiz_questions[i][2]}\n",
                                font=("Consolas", 18), fg="black")
        else:
            score_label = Label(second_frame, text=f"Question: {quiz_questions[i][0]},\n Correct?: "
                                                   f"{quiz_questions[i][2]}, Answer: {quiz_questions[i][1]}\n",
                                font=("Consolas", 18), fg="black")
        score_label.pack()
    quizzes_button.pack()
    return_button.pack()


def return_to_scores(frame, scores):
    frame.destroy()
    view_scores(scores)


def return_to_main(frame):
    frame.destroy()
    starting_page()


def login(window_frame):
    window_frame.destroy()
    login_frame = Frame(window, bd=20, relief=RAISED, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    username = Entry(login_frame, font=("Consolas", 20), fg="#00ff00", bg="black")
    password = Entry(login_frame, font=("Consolas", 20), fg="#00ff00", bg="black", show="*")
    username_label = Label(login_frame, text="Username: ", font=("Consolas", 30), fg="black")
    password_label = Label(login_frame, text="Password: ", font=("Consolas", 30), fg="black")
    submit_button = Button(login_frame, text="Login", command=lambda: submit_login(username, password, login_frame),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    return_button = Button(login_frame, text="Return to Main Menu",
                           command=lambda: return_to_main(login_frame),
                           font=("Consolas", 20), fg="#00ff00", bg="black", activebackground="lightgrey")

    login_frame.pack()
    login_frame.pack_propagate(0)
    username_label.place(x=10, y=10)
    username.place(x=250, y=20)
    password_label.place(x=10, y=100)
    password.place(x=250, y=110)
    submit_button.place(x=300, y=250)
    return_button.place(x=230, y=350)


def sign_up(window_frame):
    window_frame.destroy()
    signup_frame = Frame(window, bd=20, relief=RAISED, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    username = Entry(signup_frame, font=("Consolas", 20), fg="#00ff00", bg="black")
    password = Entry(signup_frame, font=("Consolas", 20), fg="#00ff00", bg="black", show="*")
    confirm_password = Entry(signup_frame, font=("Consolas", 20), fg="#00ff00", bg="black", show="*")
    username_label = Label(signup_frame, text="Username: ", font=("Consolas", 30), fg="black")
    password_label = Label(signup_frame, text="Password: ", font=("Consolas", 30), fg="black")
    confirm_password_label = Label(signup_frame, text="Confirm Password: ", font=("Consolas", 30), fg="black")
    submit_button = Button(signup_frame, text="Sign Up", command=lambda: submit_signup(username, password,
                                                                                       confirm_password, signup_frame),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    return_button = Button(signup_frame, text="Return to Main Menu",
                           command=lambda: return_to_main(signup_frame), font=("Consolas", 20), fg="#00ff00",
                           bg="black", activebackground="lightgrey")

    signup_frame.pack()
    signup_frame.pack_propagate(0)
    username_label.place(x=10, y=10)
    username.place(x=250, y=20)
    password_label.place(x=10, y=100)
    password.place(x=250, y=110)
    confirm_password_label.place(x=10, y=190)
    confirm_password.place(x=450, y=200)
    submit_button.place(x=300, y=350)
    return_button.place(x=230, y=450)


def submit_login(username, password, login_frame):
    global entered_user
    entered_username = username.get()
    entered_password = password.get()
    logged_in = compare_user(entered_username, entered_password)
    if logged_in:
        entered_user = entered_username
        login_frame.destroy()
        choose_quiz_type()
    else:
        messagebox.showerror(title="Login Failed", message="Username and/or password aren't recognised")


def submit_signup(username, password, confirm_password, signup_frame):
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
        user_added = add_user(username_str, password_str)
        if user_added:
            signup_frame.destroy()
            starting_page()
        else:
            messagebox.showerror(title="Sign Up Failed", message="That username has been taken")


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
    previous_quiz_button = Button(quiz_frame, text="Do Previous Quiz",
                                  command=lambda: previous_quizzes(quiz_frame),
                                  font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    no_questions_label = Label(quiz_frame, text="No of Questions", font=("Consolas", 30), fg="black")
    questions_entry = Entry(quiz_frame, font=("Consolas", 30), fg="#00ff00", bg="black")
    questions_entry.insert(0, 20)
    quiz_frame.pack()
    quiz_choice_label.pack()
    addition_button.pack()
    subtraction_button.pack()
    multiplication_button.pack()
    division_button.pack()
    no_questions_label.pack()
    questions_entry.pack()
    previous_quiz_button.pack()


def previous_quizzes(quiz_frame):
    quiz_frame.destroy()
    quizzes = display_quizzes()
    quizzes_frame = Frame(window, bd=20, relief=RAISED, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    quiz_canvas = Canvas(quizzes_frame)
    quiz_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    scrollbar = ttk.Scrollbar(quizzes_frame, orient=VERTICAL, command=quiz_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    quiz_canvas.configure(yscrollcommand=scrollbar.set)
    quiz_canvas.bind("<Configure>", lambda e: quiz_canvas.configure(scrollregion=quiz_canvas.bbox("all")))
    second_frame = Frame(quiz_canvas)
    quiz_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    for i in range(len(quizzes)):
        quiz_label = Label(second_frame, text=f"Quiz No: {i + 1},\n No. of Questions: {quizzes[i][1]}\n"
                                              f"Quiz Type: {quizzes[i][2]}\n", font=("Consolas", 18), fg="black")
        quiz_label.pack()
        # choose_quiz_button.grid(row=i, column=1)
    redo_quiz_label = Label(second_frame, text="Enter Number of Quiz to Redo", font=("Consolas", 20), fg="black")
    quiz_report_button = Button(second_frame, text="Redo Quiz",
                                command=lambda: create_quiz(second_frame, quiz_entry.get(), quizzes),
                                font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    return_button = Button(second_frame, text="Return to Quiz Selection", command=lambda: return_to_quiz(quizzes_frame),
                           font=("Consolas", 20), fg="#00ff00", bg="black", activebackground="lightgrey")

    quiz_entry = Entry(second_frame, font=("Consolas", 20), fg="#00ff00", bg="black")
    redo_quiz_label.pack()
    quiz_entry.pack()
    quiz_report_button.pack()
    return_button.pack()
    quizzes_frame.pack()
    quizzes_frame.pack_propagate(0)
    quiz_canvas.pack(side=LEFT, fill=BOTH, expand=1)


def return_to_quiz(frame):
    frame.destroy()
    choose_quiz_type()


def create_quiz(quiz_frame, quiz_number, quizzes):
    try:
        if int(quiz_number) > len(quizzes):
            messagebox.showerror(title="Invalid Entry", message="That Quiz Number doesn't exist")
        else:
            quiz_number = int(quiz_number) - 1
            quiz_frame.destroy()
            quiz_game(quizzes[quiz_number])
    except ValueError:
        messagebox.showerror(title="Invalid Entry", message="Quiz Number entered must be an Integer")


def quiz_game(quiz):
    global answer
    global score
    global question_number
    global no_of_questions
    quiz_questions = display_full_quiz_questions(quiz[0])
    quiz_game_frame = Frame(window, bd=20, relief=RAISED, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    question_number_label = Label(quiz_game_frame, text="Question {}".format(question_number), font=("Consolas", 30),
                                  fg="black")
    question_label = Label(quiz_game_frame, text="PLACEHOLDER", font=("Consolas", 30), fg="black")
    answer_entry = Entry(quiz_game_frame, font=("Consolas", 30), fg="#00ff00", bg="black")
    submit_button = Button(quiz_game_frame, text="Check Answer",
                           command=lambda: check_fixed_answer(answer_entry, quiz_game_frame, quiz,
                                                              quiz_questions[question_number - 1][0]),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    score_label = Label(quiz_game_frame, text="PLACEHOLDER", font=("Consolas", 30), fg="black")

    if question_number <= len(quiz_questions):
        answer = quiz_questions[question_number - 1][2]
        question_label.config(text=quiz_questions[question_number - 1][1])
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
        save_score(quiz[2], True, quiz[0], quiz[1])


def check_fixed_answer(answer_entry, quiz_game_frame, quiz, question_id):
    global answer
    global score
    global question_number
    try:
        if answer == int(answer_entry.get()):
            score += 1
            update_question(True, question_id)
        else:
            update_question(False, question_id)
        question_number += 1
        quiz_game_frame.destroy()
        quiz_game(quiz)
    except ValueError:
        messagebox.showerror(title="Answer Invalid", message="Answer can only be an integer")


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
            add_quiz(no_of_questions, quiz_type)
            random_quiz_game(quiz_type)

    except ValueError:
        messagebox.showerror(title="Answer Invalid", message="Number of Questions must be an Integer")


def random_quiz_game(quiz_type):
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
                           command=lambda: check_answer(answer_entry, question_label.cget("text"), quiz_game_frame,
                                                        quiz_type),
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
        save_score(quiz_type, False, 0, 0)


def check_answer(answer_entry, question, quiz_game_frame, quiz_type):
    global answer
    global score
    global question_number
    current_quiz = display_quiz_id()
    try:
        if answer == int(answer_entry.get()):
            score += 1
            add_question(question, answer, True, current_quiz)
        else:
            add_question(question, answer, False, current_quiz)
        question_number += 1
        quiz_game_frame.destroy()
        random_quiz_game(quiz_type)
    except ValueError:
        messagebox.showerror(title="Answer Invalid", message="Answer can only be an integer")


def save_score(quiz_type, previous_quiz, quiz_id, quiz_length):
    global score
    global question_number
    global entered_user
    global no_of_questions

    scores_frame = Frame(window, bd=20, relief=RAISED, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    results_label = Label(scores_frame, text="Well done, you got: {} / {}".format(score, question_number - 1),
                          font=("Consolas", 30), fg="black")
    logout_button = Button(scores_frame, text="Log out", command=lambda: endgame(scores_frame, "logout"),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    restart_button = Button(scores_frame, text="Do Another Quiz", command=lambda: endgame(scores_frame, "restart"),
                            font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    quiz_report_button = Button(scores_frame, text="View Quiz Report",
                                command=lambda: quiz_report(scores_frame),
                                font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    current_quiz = display_quiz_id()
    if previous_quiz:
        add_score(entered_user, score, no_of_questions, quiz_type, round(score / quiz_length, 2), quiz_id)
    else:
        add_score(entered_user, score, no_of_questions, quiz_type, round(score / no_of_questions, 2), current_quiz)
    scores_frame.pack()
    scores_frame.pack_propagate(0)
    results_label.pack()
    logout_button.pack()
    restart_button.pack()
    quiz_report_button.pack()


def quiz_report(scores_frame):
    scores_frame.destroy()
    report_frame = Frame(window, bd=20, relief=RAISED, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    report_frame.pack(fill=BOTH, expand=1)  # Can be used instead of pack_propagate(0)
    report_canvas = Canvas(report_frame)
    report_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    scrollbar = ttk.Scrollbar(report_frame, orient=VERTICAL, command=report_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    report_canvas.configure(yscrollcommand=scrollbar.set)
    report_canvas.bind("<Configure>", lambda e: report_canvas.configure(scrollregion=report_canvas.bbox("all")))
    second_frame = Frame(report_canvas)
    report_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    current_quiz = display_quiz_id()
    quiz_questions = display_quiz_questions(current_quiz)
    logout_button = Button(second_frame, text="Log out", command=lambda: endgame(report_frame, "logout"),
                           font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")
    restart_button = Button(second_frame, text="Do Another Quiz", command=lambda: endgame(report_frame, "restart"),
                            font=("Consolas", 30), fg="#00ff00", bg="black", activebackground="lightgrey")

    for i in range(len(quiz_questions)):
        if quiz_questions[i][2] == "True":
            score_label = Label(second_frame, text=f"Question: {quiz_questions[i][0]},\n Correct?: "
                                                   f"{quiz_questions[i][2]}\n",
                                font=("Consolas", 18), fg="black")
        else:
            score_label = Label(second_frame, text=f"Question: {quiz_questions[i][0]},\n Correct?: "
                                                   f"{quiz_questions[i][2]}, Answer: {quiz_questions[i][1]}\n",
                                font=("Consolas", 18), fg="black")
        score_label.pack()
    logout_button.pack()
    restart_button.pack()


def endgame(frame, end_game):
    global score
    global question_number
    frame.destroy()
    score = 0
    question_number = 1
    starting_page() if end_game == "logout" else choose_quiz_type()


window = Tk()
window.resizable(False, False)
window.title("Quiz Game")

monitor_width = window.winfo_screenwidth()
monitor_height = window.winfo_screenheight()

x = int((monitor_width / 2) - (SCREEN_HEIGHT / 2))  # Used to center the window
y = int((monitor_height / 2) - (SCREEN_WIDTH / 2))
window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}+{x}+{y}")

score = 0
answer = 0
question_number = 1
no_of_questions = 0
entered_user = ""

starting_page()

if __name__ == '__main__':
    tables_setup()
    window.mainloop()
