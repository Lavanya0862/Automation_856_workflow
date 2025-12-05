import sqlite3

def create_db_connection(db_path):
    try:
        conn = sqlite3.connect(db_path)
        print("Database connection established.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def validate_user_credentials(conn, username_input):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT AccessLevel FROM User_Credentials WHERE username = ?
        ''', (username_input,))

        result = cursor.fetchone()

        if result:
            AccessLevel = result[0]
            return AccessLevel
        else:
            print("Username not found.")
            return None
    except Exception as e:
        print(f"Error validating user credentials: {e}")
        return None
