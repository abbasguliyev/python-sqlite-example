import sqlite3

DB_NAME = "rentacar.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def migrate():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT NOT NULL,
            color TEXT NOT NULL,
            rental_price INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    migrate()

