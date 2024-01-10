import psycopg2

class PG:

    connection=None
    cursor=None
   

    @classmethod
    def pg(cls):
        print("Connecting to db")
        db_config={
            'host':'db.pssbujkmzspdgqugjdzv.supabase.co',
            'database':'postgres',
            'user':'postgres',
            'password':'3jGSjyNnunEOPP5P',
            'port':'5432'
        }

        if cls.cursor is not None:
            return cls.cursor
        connection=psycopg2.connect(**db_config)
        cursor=connection.cursor()
        cls.connection=connection
        cls.cursor=cursor
        return cls.cursor
    
    @classmethod
    def pg_disconnect(cls):
        if cls.cursor is not None:
            cls.cursor.close
        if  cls.connection is not None:
            cls.connection.close()
    
class Student:

    def __init__(self):
        try:
            sql='''
            CREATE TABLE IF NOT EXISTS student(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            parent_id INTEGER REFERENCES parent(id),
            address_id INTEGER NOT NULL UNIQUE REFERENCES address(id) 
            )
            '''

            cursor=PG.pg()
            cursor.execute(sql)
            PG.connection.commit()
            print("Student Created Successfully")
        except Exception as e:
            print("Error creating table",e)
    
    def all(self):
        try:
            sql="SELECT * FROM student"
            cursor=PG.pg()
            cursor.execute(sql)
            result=cursor.fetchall()
            print("ALL students:",result)
    
        except Exception as e:
            print("ErrorGetting Students")


class Another:

    def __init__(self):
        try:
            sql='''
            CREATE TABLE IF NOT EXISTS another(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            parent_id INTEGER REFERENCES parent(id),
            address_id INTEGER NOT NULL UNIQUE REFERENCES address(id) 
            )
            '''

            cursor=PG.pg()
            cursor.execute(sql)
            PG.connection.commit()
            print("Student Created Successfully")
        except Exception as e:
            print("Error creating table",e)
    



a1=Another()