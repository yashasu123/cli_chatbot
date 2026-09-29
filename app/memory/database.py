import sqlite3

class Database:

    def __init__(self, db_name="chatbot.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)
    
    def create_tables(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """)

        connection.commit()
        connection.close()

    def save_message(self, role, content):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO messages (role, content)
            VALUES (?, ?)
            """,
            (role, content)
        )

        connection.commit()
        connection.close()

    def get_messages(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT role, content
            FROM messages
            ORDER BY id
            """
        )

        messages = cursor.fetchall()

        connection.close()

        return messages