import pandas as pd
from db_connection import create_db_connection

db_path = 'Database/automation_data.db'
excel_file_path = 'Database/Automation_856_Workflow_Data.xlsx'

conn = create_db_connection(db_path)

try:
    xls = pd.ExcelFile(excel_file_path)
    cursor = conn.cursor()

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)

        columns = ", ".join([f'"{col}" TEXT' for col in df.columns])
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS "{sheet_name}" (
            {columns}
        )
        ''')

        for index, row in df.iterrows():
            values = tuple(row)
            placeholders = ', '.join(['?'] * len(values))
            cursor.execute(f'''
            INSERT OR REPLACE INTO "{sheet_name}" ({', '.join(df.columns)})
            VALUES ({placeholders})
            ''', values)

        conn.commit()

    print("Excel data imported successfully.")

except Exception as e:
    print(f"Error importing data from Excel: {e}")

finally:
    if conn:
        conn.close()
