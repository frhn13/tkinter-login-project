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
            quiz_type TEXT NOT NULL);""")

    conn_scores.commit()

    conn_users.close()
    conn_scores.close()


def sql_commands():
    conn = sqlite3.connect("tables/users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    items = c.fetchall()
    print(items)
    c.execute("INSERT INTO users VALUES ('user1', '123245')")
