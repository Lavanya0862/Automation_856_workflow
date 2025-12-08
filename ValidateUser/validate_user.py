import sqlite3
from ErrorHandler.error_handler import log_error

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
            access_level = result[0]
            if access_level == "Full":
                return access_level
            else:
                log_error(username_input, "User does not have 'Full' access. AccessLevel", "DB Connection")
                print(f"User does not have 'Full' access. AccessLevel: {access_level}")
                return None
        else:
            log_error(username_input, "Username not found.", "DB Connection") 
            return None
    except Exception as e:
        log_error(username_input, "Error validating user credentials", "DB Connection")
        print(f"Error validating user credentials: {e}")
        return None
