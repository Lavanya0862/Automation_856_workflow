from Database.db_connection import create_db_connection
# from Database.import_excel import import_excel_data_to_db
from ValidateUser.validate_user import validate_user_credentials
from OrderProcessing.fetch_data import fetch_data_if_admin


def main():
    db_path = 'Database/automation_data.db'
    conn = create_db_connection(db_path)
    if not conn:
        return

    # excel_file_path = 'Database/Automation_856_Workflow_Data.xlsx'
    # if not import_excel_data_to_db(conn, excel_file_path):
    #     conn.close()
    #     return

    username_input = input("Enter your username: ")
    access_level = validate_user_credentials(conn, username_input)
    if not access_level:
        conn.close()
        return

    fetch_data_if_admin(conn, access_level)

    conn.close()

if __name__ == "__main__":
    main()
