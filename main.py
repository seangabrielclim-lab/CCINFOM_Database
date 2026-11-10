from database import init_database, get_all_tables

def main():
    db = init_database()
    get_all_tables(db)

if __name__ == "__main__":
    main()