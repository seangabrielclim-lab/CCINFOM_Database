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
        if (str(e) == "1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)"):
            msg = "Wrong Password"
        elif (str(e) == "1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)"):
            msg = "Enter a password"
        else:
            msg = f"Error : {e}"
        return None, msg

def get_all_tables(db):
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    for table in cursor.fetchall():
        print(table)

    cursor.close()