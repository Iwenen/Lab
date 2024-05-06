import psycopg2

name = input()
#connect to the database by creating a connecting object
conn = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postgres",
    password = "1223",
    port =5433
    )
#create a cursor to work with the database
cur = conn.cursor()
conn.set_session(autocommit=True)
#delete students table
cur.execute(f"""delete from students_data
            where name = '{name}'
""")
conn.commit()
