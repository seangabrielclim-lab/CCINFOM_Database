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
    except mysql.connector.Error as e:
        db.rollback()
        print(e)
        return False
    finally:
        cursor.close()

def del_drug(db, product_code):
    success = False
    cursor = db.cursor()

    query = """
        DELETE FROM drugs_record
        WHERE product_code = %s
    """

    value = [product_code]
    try:
        cursor.execute(query, value)
        db.commit()
        if cursor.rowcount >0 :
            success = True
        return success
    except mysql.connector.Error as e:
        db.rollback()
        print(e)
        return success
    finally:
        cursor.close()

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
    except mysql.connector.Error as e:
        db.rollback()
        print(e)
        return success

    finally:
        cursor.close()

def get_drug(db, product_code):
    states_of_querying = ["empty", "not_empty", "error"]
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
            return drug, states_of_querying[1]
        return drug, states_of_querying[0]
    except mysql.connector.Error as e:
        print(e)
        return [], states_of_querying[2]
    finally:
        cursor.close()

# this would return a tuple the first element being the drug record itself then second one is if it was successful
def get_all_drugs(db):
    states_of_querying = ["empty", "not_empty", "error"]
    cursor = db.cursor()
    query = """
        SELECT *
        FROM drugs_record
    """
    try:
        cursor.execute(query)
        drugs = cursor.fetchall()
        if drugs:
            return drugs, states_of_querying[1]
        return drugs, states_of_querying[0]
    except mysql.connector.Error as e:
        print(e)
        return [], states_of_querying[2]
    finally:
        cursor.close()

# FOR THE UI PEOPLE THE PARAM THATS BEING PASSED TO DETERMINE WHAT TYPE OF FILTERED VIEW COULD BE CHANGED TO WHATEVER IS EASIER FOR YOU PERO ILL ASSUME INT FOR NOW HEHEHEHEHE
def filtered_views(db,type_of_view, product_category=None, origin_country=None, start_date=None, end_date=None):
    states_of_querying = ["empty", "not_empty", "error"]
    cursor = db.cursor()
    try:
        if type_of_view == 1:
            query = """
                    SELECT product_code, product_name, availability_status
                    FROM drugs_record
                    WHERE product_category = %s
                """
            values = [product_category]
            cursor.execute(query, values)
            records = cursor.fetchall()
        elif type_of_view == 2:
            query = """
                    SELECT product_code, product_name, availability_status
                    FROM drugs_record
                    WHERE quantity_in_stock < minimum_stock_level
                """
            cursor.execute(query)
            records = cursor.fetchall()
        elif type_of_view == 3:
            query = """
                    SELECT DISTINCT d.product_code, d.product_name, d.availability_status
                    FROM drugs_record d
                    JOIN resupply_record r ON d.product_code = r.product_code
                    JOIN transportation_record t ON r.shipping_code = t.shipping_code
                    WHERE t.origin_country = %s
                """
            values = [origin_country]
            cursor.execute(query, values)
            records = cursor.fetchall()
        elif type_of_view == 4:
            query = """
                    SELECT product_code, product_name, availability_status
                    FROM drugs_record
                    WHERE quantity_in_stock = 0
                """
            cursor.execute(query)
            records = cursor.fetchall()
        elif type_of_view == 5:
            query = """
                    SELECT DISTINCT d.product_code, d.product_name
                    FROM drugs_record d
                    JOIN resupply_record r ON d.product_code = r.product_code
                    WHERE COALESCE(r.recent_date_received, r.date_received) BETWEEN %s AND %s
                """
            values = [start_date, end_date]
            cursor.execute(query, values)
            records = cursor.fetchall()
        else:
            print(f"Invalid type_of_view: {type_of_view}")
            return [], states_of_querying[2]

        if records:
            return records, states_of_querying[1]
        return records, states_of_querying[0]
    except mysql.connector.Error as e:
        print(f"ERROR running filtered view: {e}")
        return [], states_of_querying[2]
    finally:
        cursor.close()




