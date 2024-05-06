import psycopg2
#connect to the database by creating a connecting object
conn = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postgres",
    password = "abkk0615"
    )
#create a cursor to work with the database
cur = conn.cursor()
conn.set_session(autocommit=True)

cur.execute('SELECT name,phone_number FROM students_data')

print(cur.fetchall())

cur.execute('SELECT name, phone_number FROM students_data')

print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())

cur.execute('select name,phone_number from students_data')
print(cur.fetchmany())
print(cur.fetchmany())
print(cur.fetchmany())