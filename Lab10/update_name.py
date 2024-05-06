#CSV - comma separated values
import psycopg2
newname = input("Newname: ")
oldname = input("Oldname: ")

#connect to the database by creating a connecting object
conn = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postgres",
    password = "abkk0615",
    )
#create a cursor to work with the database
cur = conn.cursor()
conn.set_session(autocommit=True)

cur.execute(f"""update students_data
            SET name = '{newname}'
            WHERE name = '{oldname}'
""")