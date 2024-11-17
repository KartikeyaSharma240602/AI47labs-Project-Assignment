import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'Satyam@2608'
port_id = 5432

con = None
try:
    with psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    ) as con :
        
        with con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur : 

            cur.execute('DROP TABLE IF EXISTS employee')

            create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                            id      int PRIMARY KEY,
                            name    varchar(40) NOT NULL,
                            salary  int,
                            dept_id varchar(30)
                        )
                    '''
            cur.execute(create_script)

            insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'Kartikeya', 2, 'D1'), (2, 'Satyam', 200000, 'D1'), (3, 'Rishab', 199999, 'D1'), (4, 'Prateek', 199999, 'D1')]
            
            for record in insert_values :
                cur.execute(insert_script, record)

            cur.execute('SELECT * FROM employee')
            for record in cur.fetchall() : 
                print(record['name'], record['salary'])

            #print(cur.fetchone())
            #print(cur.fetchone())

            #print(cur.fetchmany(size=3))

            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)

            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_value = ('Satyam',)
            cur.execute(delete_script, delete_value)

            print('Salary after update : ')
            cur.execute('SELECT * FROM employee')
            for record in cur.fetchall() :
                print (record['name'], record['salary'])

except Exception as error : 
    print(error)
finally :
    if con is not None :
        con.close()