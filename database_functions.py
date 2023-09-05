import sqlite3


def tables_setup():
    conn_users = sqlite3.connect("tables/users.db")
    conn_scores = sqlite3.connect("tables/scores.db")
    conn_quizzes = sqlite3.connect("tables/quizzes.db")
    conn_questions = sqlite3.connect("tables/questions.db")

    c_users = conn_users.cursor()
    c_scores = conn_scores.cursor()
    c_quizzes = conn_quizzes.cursor()
    c_questions = conn_questions.cursor()

    c_users.execute("""CREATE TABLE if not exists users
             (username TEXT UNIQUE NOT NULL,
             password TEXT NOT NULL);""")

    conn_users.commit()

    c_scores.execute("""CREATE TABLE if not exists scores
            (username TEXT NOT NULL,
            score INTEGER NOT NULL,
            no_questions INTEGER NOT NULL,
            quiz_type TEXT NOT NULL,
            percentage REAL NOT NULL,
            quiz_id INTEGER NOT NULL);""")

    conn_scores.commit()

    c_quizzes.execute("""CREATE TABLE if not exists quizzes
                (no_questions TEXT NOT NULL,
                quiz_type TEXT NOT NULL);""")

    conn_quizzes.commit()

    c_questions.execute("""CREATE TABLE if not exists questions
                    (question TEXT NOT NULL,
                    answer INTEGER NOT NULL,
                    correct BOOLEAN,
                    question_quiz INTEGER NOT NULL);""")

    conn_questions.commit()

    conn_users.close()
    conn_scores.close()
    conn_quizzes.close()
    conn_questions.close()


def add_user(username, password):
    try:
        conn = sqlite3.connect("tables/users.db")
        c = conn.cursor()
        c.execute(f"INSERT INTO users VALUES ('{username}', '{password}')")
        conn.commit()
        conn.close()
        return True
    except sqlite3.OperationalError:
        return False


def compare_user(username, password):
    conn = sqlite3.connect("tables/users.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE username = '{username}'")
    user_details = c.fetchone()
    if user_details and user_details[1] == password:
        return True
    else:
        return False


def add_score(username, score, no_questions, quiz_type, percentage, current_quiz):
    conn = sqlite3.connect("tables/scores.db")
    c = conn.cursor()
    c.execute(f"INSERT INTO scores VALUES ('{username}', '{score}', '{no_questions}', '{quiz_type}', '{percentage}', '{current_quiz}')")
    conn.commit()
    conn.close()


def display_users():
    conn = sqlite3.connect("tables/users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    items = c.fetchall()
    conn.close()


def display_scores(quiz_type):
    conn = sqlite3.connect("tables/scores.db")
    c = conn.cursor()
    if quiz_type == "all":
        c.execute("SELECT * FROM scores")
    else:
        c.execute(f"SELECT * FROM scores WHERE quiz_type = '{quiz_type}'")
    all_scores = c.fetchall()
    conn.close()
    return all_scores


def display_user_scores(username, quiz_type):
    conn = sqlite3.connect("tables/scores.db")
    c = conn.cursor()
    if quiz_type == "all":
        c.execute(f"SELECT * FROM scores WHERE username = '{username}'")
    else:
        c.execute(f"SELECT * FROM scores WHERE username = '{username}' AND quiz_type = '{quiz_type}'")
    all_scores = c.fetchall()
    conn.close()
    return all_scores


def add_quiz(no_questions, quiz_type):
    conn = sqlite3.connect("tables/quizzes.db")
    c = conn.cursor()
    c.execute(f"INSERT INTO quizzes VALUES ('{no_questions}', '{quiz_type}')")
    conn.commit()
    conn.close()


def add_question(question, answer, correct, question_quiz):
    conn = sqlite3.connect("tables/questions.db")
    c = conn.cursor()
    c.execute(f"INSERT INTO questions VALUES ('{question}', '{answer}', '{correct}', '{question_quiz}')")
    conn.commit()
    conn.close()


def display_quiz_id():
    conn = sqlite3.connect("tables/quizzes.db")
    c = conn.cursor()
    c.execute(f"SELECT MAX(rowid) FROM quizzes")
    quiz_id = c.fetchone()
    conn.close()
    return quiz_id[0]


def display_quiz_questions(quiz_id):
    conn = sqlite3.connect("tables/questions.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM questions WHERE question_quiz = '{quiz_id}'")
    quiz_questions = c.fetchall()
    conn.close()
    return quiz_questions
