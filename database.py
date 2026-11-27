import mysql.connector
import getpass

def init_database(password):
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd= password,
            database= 'pharmaflow',
            port=3306
        )

        if db.is_connected:
            return db, "success"
    except mysql.connector.Error as e:
        print(f"failed to connect. {e}")
        return None, str(e)

def get_all_tables(db):
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    for table in cursor.fetchall():
        print(table)

    cursor.close()