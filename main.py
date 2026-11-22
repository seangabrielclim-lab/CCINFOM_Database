from database import init_database, get_all_tables
import sales_record_management as srm

def main():
    db = init_database()
    get_all_tables(db)
    
    # for _ in range(3):
    #     srm.add_record(db)
        
    # srm.view_record(db)
    # srm.update_date(db)
    srm.view_record_by_country(db)
    srm.view_record_by_date(db)
    srm.view_record_by_status(db)
    # srm.delete_record(db)

if __name__ == "__main__":
    main()