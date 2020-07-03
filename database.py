import sqlite3

db_name="database.db"

def create_connection(db_file):
    try:
        conn= sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
        return None

if __name__ == '__main__':
    create_connection(db_name)