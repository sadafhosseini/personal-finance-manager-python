import sqlite3


DATABASE_NAME = "finance.db"


def connect_database():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        transaction_type TEXT NOT NULL,
        date TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def add_transaction(title, amount, category, transaction_type, date):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO transactions 
    (title, amount, category, transaction_type, date)
    VALUES (?, ?, ?, ?, ?)
    """,
    (title, amount, category, transaction_type, date))

    connection.commit()
    connection.close()


def get_transactions():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM transactions
    """)

    data = cursor.fetchall()

    connection.close()

    return data


def delete_transaction(transaction_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM transactions
    WHERE id = ?
    """,
    (transaction_id,))

    connection.commit()
    connection.close()
