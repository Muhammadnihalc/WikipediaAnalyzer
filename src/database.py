import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('search_history.db')
        c = conn.cursor()

        # Creating the search history table
        c.execute('''CREATE TABLE IF NOT EXISTS search_history
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     topic TEXT,
                     word TEXT,
                     count INTEGER,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        # Commit changes and close connection
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_database()


