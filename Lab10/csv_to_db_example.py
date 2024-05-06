#CSV - comma separated values
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


#create a new table
cur.execute("""create table if not exists students_data(
            name varchar(255),
            phone_number varchar(20)
        
);
""")
conn.commit()
import csv

filename = 'student.csv'
with open(filename,"r") as csfile:
    csvreader = csv.reader(csfile,delimiter=',')
    for row in csvreader:
        name,phone_number = row
        #create new students
        cur.execute(f"""insert into students_data (name, phone_number) VALUES
                    
                    ('{name}','{phone_number}')
        """)
        conn.commit()
name = input()
phone_number = input()
cur.execute(f"""insert into students_data (name, phone_number) VALUES
                    
                    ('{name}','{phone_number}')
        """)
conn.commit()



