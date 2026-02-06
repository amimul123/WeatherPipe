import psycopg2
from api_request import fetch_data 

def connect_to_db():
    print("connecting to db...")
    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            dbname="db",
            user="db_user",
            password="db_password"
        )
        return conn
    except psycopg2.Error as e:
        print(f"db connection fail: {e}")
        raise

def create_table(conn):
    print("creating table if not exist")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            create schema if not exists dev;
            create table if not exists dev.raw_weather_data(
                id serial primary key,
                lat float,
                long float,
                temp float,
                time timestamp,
                inserted_at timestamp default now()
            );
        """)
        conn.commit()
        print("Table was created")

    except psycopg2.Error as e:
        print(f"table creation fail: {e}")
        raise


def insert_record(conn, data):
    print("Inserting records...")
    try:
        
        cursor = conn.cursor()
        cursor.execute("""
            insert into dev.raw_weather_data(
                lat,
                long,
                temp,
                time,
                inserted_at
            ) values (%s, %s, %s, %s, NOW())
        """,
        (
            data["latitude"],
            data["longitude"],
            data["temperature"],
            data["time"]
        )
        )
        conn.commit()
        print("Insert ")

    except psycopg2.Error as e:
        print(f"insertion fail: {e}")
        raise


def main():
    try:
        conn = connect_to_db()
        create_table(conn)
        data = fetch_data()
        insert_record(conn, data)
    except Exception as e:
        print(f"execution error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("DB connection closed.")

# main()
