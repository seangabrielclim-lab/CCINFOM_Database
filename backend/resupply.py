import mysql.connector

def add_resupply(db, supply_code, product_code, quantity, date_received, recent_date_received, quantity_received, shipping_code, resupply_status, resupply_id):
    cursor = db.cursor()

    query = """
        INSERT INTO resupply_record(supply_code, product_code, quantity, date_received, recent_date_received, quantity_received, shipping_code, resupply_status, resupply_id)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = [supply_code, product_code, quantity, date_received, recent_date_received, quantity_received, shipping_code, resupply_status, resupply_id]

    try:
        cursor.execute(query, values)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(e)
        return False
    finally:
        cursor.close()

def update_resupply(db, supply_code, quantity_received, resupply_status, recent_date_received):
    success = False
    cursor = db.cursor()

    query = """
        UPDATE resupply_record
        SET quantity_received = %s, resupply_status = %s, recent_date_received = %s
        WHERE supply_code = %s
    """

    values = [quantity_received, resupply_status, recent_date_received, supply_code]

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

def delete_resuuply(db, supply_code):
     success = False
     cursor = db.cursor()
     
     query = """
             DELETE FROM resupply_record
             WHERE supply_code = %s
         """
     value = [supply_code]
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
        cursor.close()

def get_resupply(db, supply_code):
    states_of_querying = ["empty", "not_empty", "error"]
    cursor = db.cursor()
    query = """
        SELECT * 
        FROM resupply_record
        WHERE supply_code = %s
    """
    values = [supply_code]
    try:
        cursor.execute(query, values)
        resupply = cursor.fetchone()
        if resupply:
            return resupply, states_of_querying[1]
        return resupply, states_of_querying[0]
    except Exception as e:
        db.rollback()
        return [], states_of_querying[2]
    finally:
        cursor.close()

def get_all_resupply(db, supply_code):
    states_of_querying = ["empty", "not_empty", "error"]
    cursor = db.cursor()
    query = """
        SELECT * 
        FROM resupply_record
    """
    values = [supply_code]
    try:
        cursor.execute(query, values)
        resupply = cursor.fetchall()
        if resupply:
            return resupply, states_of_querying[1]
        return resupply, states_of_querying[0]
    except Exception as e:
        db.rollback()
        return [], states_of_querying[2]
    finally:
        cursor.close()

def get_filtered_views(db, type_of_view, product_code):
    states_of_querying = ["empty", "not_empty", "error"]
    cursor = db.cursor()
    query = """
        SELECT supply_code, quantity_received, date_received
        FROM resupply_record
        WHERE product_code = %s
    """
    values = [product_code]
    try:
        cursor.execute(query, values)
        resupply = cursor.fetchall()
        if resupply:
            success = True
        return success
    except Exception as e:
        db.rollback()
        return success
    finally:
        cursor.close()