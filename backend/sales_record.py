import mysql.connector
from datetime import date as dt

# -- Adding Records -- #
def add_record(db):
    cursor = db.cursor()

    transaction_code:int
    product_code:int = 0;
    shipping_code:int = 0;
    customer_code:int = 0;
    quantity_sold:int = int(input("quantity sold:"))
    date_sold = dt.fromisoformat(input("Enter a date (YYYY-MM-DD): "))
    order_status:str
    destination = input("country: ")

    
    sql = ("INSERT INTO sales_record (quantity_sold, "
            "destination_country, date_sold) VALUES (%s, %s, %s)")
    
    val = (quantity_sold, destination, date_sold);
    cursor.execute(sql, val)
    
    db.commit();
  
# -- Updating Records -- #
def update_status(db):
    cursor = db.cursor()
    
    allowed_statuses = ("pending", "complete")

    while (True):
        status = input("Enter Status: ")
        if status not in allowed_statuses:
            print(f"Invalid status. Choose from: {allowed_statuses}")
        else:
            break;
        
    code = input("Enter transaction code: ")

    sql = ("UPDATE sales_record SET order_status = %s WHERE transaction_code = %s")
    adr = (status, code)
    
    cursor.execute(sql, adr)
    
    db.commit()
    
def update_country(db):
    cursor = db.cursor()
    
    country = input("Enter new country: ")
    code = input("Enter transaction code: ")
    
    sql = ("UPDATE sales_record SET destination_country = %s WHERE transaction_code = %s")
    adr = (country, code)
    
    cursor.execute(sql, adr)
    
    db.commit()
    
def update_date(db):
    cursor = db.cursor()
    
    date = input("Enter a date (YYYY-MM-DD): ")
    parsed_date = dt.fromisoformat(date)
    code = input("Enter transaction code: ")
    
    sql = ("UPDATE sales_record SET date_sold = %s WHERE transaction_code = %s")
    adr = (parsed_date, code)
        
    cursor.execute(sql, adr)
        
    db.commit()
    

# -- Deleting Records -- #
def delete_record(db):
    cursor = db.cursor()
    
    code = input("Enter transaction code: ")
    
    sql = "DELETE FROM sales_record WHERE transaction_code = %s"
    increment_reset = "ALTER TABLE sales_record AUTO_INCREMENT = 1"
    adr = (code,)
    
    cursor.execute(sql, adr)
    cursor.execute(increment_reset)
    
    db.commit();
  
# -- View/Filter Records -- #  
def view_record(db):
    cursor = db.cursor();
    
    shipping_code = input("Enter shipping code: ")
    transaction_code = input("Enter transaction code: ")
    
    sql = ("SELECT * FROM sales_record WHERE shipping_code = %s OR transaction_code = %s")
    adr = (shipping_code, transaction_code)
    
    cursor.execute(sql, adr)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
def view_record_by_country(db):
    cursor = db.cursor();
        
    country = input("Enter country: ")
        
    sql = ("SELECT * FROM sales_record WHERE destination_country = %s")
    adr = (country, )
        
    cursor.execute(sql, adr)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
def view_record_by_date(db):
    cursor = db.cursor();
    
    date = input("Enter a date (YYYY-MM-DD): ")
    parsed_date = dt.fromisoformat(date)
    
    sql = ("SELECT * FROM sales_record WHERE date_sold = %s")
    adr = (parsed_date, )
    
    cursor.execute(sql, adr)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
def view_record_by_status(db):
    cursor = db.cursor();
    
    allowed_statuses = ("pending", "complete")
    
    while (True):
        status = input("Enter Status: ")
        if status not in allowed_statuses:
            print(f"Invalid status. Choose from: {allowed_statuses}")
        else:
            break;
        
    sql = ("SELECT * FROM sales_record WHERE order_status = %s")
    adr = (status, )
        
    cursor.execute(sql, adr)
    rows = cursor.fetchall()
    for row in rows:
        print(row)