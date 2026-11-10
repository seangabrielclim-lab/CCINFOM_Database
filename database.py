import mysql.connector


def init_database():
    password = input("password: ")
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd= password,
            database= 'pharmaflow',
            port=3306
        )

        if db.is_connected:
            print("Succesfully connected")
            return db
    except mysql.connector.Error as e:
        print(f"failed to connect. {e}")
    return None

def get_all_tables(db):
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    for table in cursor.fetchall():
        print(table)

    cursor.close()
