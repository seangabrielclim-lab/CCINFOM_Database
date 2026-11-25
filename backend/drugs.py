import mysql.connector

def add_drug(db, product_code, product_name, product_category, product_price, quantity_in_stock, minimum_stock_level):
    cursor = db.cursor()

    query = """
        INSERT INTO drugs_record(product_code, product_name, product_category, product_price, quantity_in_stock, minimum_stock_level)
        VALUES(%s, %s,%s,%s, %s,%s)
    """
    values = [product_code, product_name, product_category, product_price, quantity_in_stock, minimum_stock_level]

    try:
        cursor.execute(query, values)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(e)
        return False
    finally:
        cursor.close

def del_drug(db, product_code):
    success = False
    cursor = db.cursor()

    query = """
        DELETE FROM drug_record
        WHERE product_code = %s
    """

    value = [product_code]
    try:
        cursor.execute(query, value)
        db.commit()
        if cursor.rowcount >0 :
            sucess = True
        return success
    except Exception as e:
        db.rollback()
        print(e)
        return sucess
    finally:
        cursor.close

def update_drug(db, product_code, product_name, product_category, product_price, quantity_in_stock, minimum_stock_level):
    success = False
    cursor = db.cursor()

    query = """
        UPDATE drugs_record
        SET product_name = %s, product_category = %s, product_price = %s, quantity_in_stock = %s, minimum_stock_level = %s
        WHERE product_code = %s
    """

    values = [product_name, product_category, product_price, quantity_in_stock, minimum_stock_level, product_code]

    try:
        cursor.execute(query, values)
        db.commit()

        if cursor.rowcount > 0:
            success = True
        return success
    except Exception as e:
        db.rollback()
        return success

    finally:
        cursor.close()

def get_drug(db, product_code):
    sucess = False
    cursor = db.cursor()
    query = """
        SELECT *
        FROM drugs_record
        WHERE product_code = %s
    """
    values = [product_code]
    try:
        cursor.execute(query, values)
        drug = cursor.fetchone()
        if drug:
            sucess = True
        return sucess
    except Exception as e:
        db.rollback()
        return sucess
    finally:
        cursor.close()

def get_all_drugs(db, product_code):
    sucess = False
    cursor = db.cursor()
    query = """
        SELECT *
        FROM drugs_record
    """
    values = [product_code]
    try:
        cursor.execute(query, values)
        drug = cursor.fetchall()
        if drug:
            sucess = True
        return sucess
    except Exception as e:
        db.rollback()
        return sucess
    finally:
        cursor.close()


