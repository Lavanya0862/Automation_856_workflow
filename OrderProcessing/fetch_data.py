def fetch_data_if_admin(conn, access_level):
    try:
        if access_level == 'Full':
            print("Access granted: Admin user.")
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Order_Data')
            rows = cursor.fetchall()

            if rows:
                print("Displaying data from Order_Data:")
                for row in rows:
                    print(row)
            else:
                print("No data found in Order_Data.")
        else:
            print("Access denied: You are not an admin.")
    except Exception as e:
        print(f"Error fetching data: {e}")
