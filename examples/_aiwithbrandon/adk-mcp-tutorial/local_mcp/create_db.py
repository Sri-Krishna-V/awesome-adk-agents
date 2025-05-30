import os
import sqlite3

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "database.db")


def create_database():
    # Check if the database already exists
    db_exists = os.path.exists(DATABASE_PATH)

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    if not db_exists:
        print(f"Creating new database at {DATABASE_PATH}...")
        # Create users table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL
            )
        """
        )
        print("Created 'users' table.")

        # Create todos table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                task TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """
        )
        print("Created 'todos' table.")

        # Insert dummy users
        dummy_users = [
            ("alice", "alice@example.com"),
            ("bob", "bob@example.com"),
            ("charlie", "charlie@example.com"),
        ]
        cursor.executemany(
            "INSERT INTO users (username, email) VALUES (?, ?)", dummy_users
        )
        print(f"Inserted {len(dummy_users)} dummy users.")

        # Insert dummy todos
        dummy_todos = [
            (1, "Buy groceries", 0),
            (1, "Read a book", 1),
            (2, "Finish project report", 0),
            (2, "Go for a run", 0),
            (3, "Plan weekend trip", 1),
        ]
        cursor.executemany(
            "INSERT INTO todos (user_id, task, completed) VALUES (?, ?, ?)", dummy_todos
        )
        print(f"Inserted {len(dummy_todos)} dummy todos.")

        conn.commit()
        print("Database created and populated successfully.")
    else:
        print(f"Database already exists at {DATABASE_PATH}. No changes made.")

    conn.close()


if __name__ == "__main__":
    create_database()
