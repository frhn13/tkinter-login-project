import sqlite3


def tables_setup():
    conn_users = sqlite3.connect("tables/users.db")
    conn_scores = sqlite3.connect("tables/scores.db")

    c_users = conn_users.cursor()
    c_scores = conn_scores.cursor()

    c_users.execute("""CREATE TABLE if not exists users
             (username TEXT UNIQUE NOT NULL,
             password TEXT NOT NULL);""")

    conn_users.commit()

    c_scores.execute("""CREATE TABLE if not exists scores
            (username TEXT NOT NULL,
            score INTEGER NOT NULL,
            no_questions INTEGER NOT NULL,
            quiz_type TEXT NOT NULL,
            percentage REAL NOT NULL);""")

    conn_scores.commit()

    conn_users.close()
    conn_scores.close()


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


def add_score(username, score, no_questions, quiz_type, percentage):
    conn = sqlite3.connect("tables/scores.db")
    c = conn.cursor()
    c.execute(f"INSERT INTO scores VALUES ('{username}', '{score}', '{no_questions}', '{quiz_type}', '{percentage}')")
    conn.commit()
    conn.close()


def display_users():
    conn = sqlite3.connect("tables/users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    items = c.fetchall()
    print(items)
    conn.close()


def display_scores():
    conn = sqlite3.connect("tables/scores.db")
    c = conn.cursor()
    c.execute("SELECT * FROM scores")
    all_scores = c.fetchall()
    conn.close()
    return all_scores
