import pyodbc

def database_connection():
    #We established connection between server and python by pyodbc
    conn_string = ("Driver={SQL Server Native Client 11.0};"
                          "Server=THAPPETA\THAPPETA;"
                          "Trusted_Connection=yes;"
                          "user=sa;"
                          "password=root;")
    my_con = pyodbc.connect(conn_string,  autocommit = True)

    # Create a Database on MS SQL Server
    cursor = my_con.cursor()
    query = "CREATE DATABASE Savith_Reddy;"
    cursor.execute(query)

def database_creation():
    database_connection()
    conn_string = ("Driver={SQL Server Native Client 11.0};"
                          "Server=THAPPETA\THAPPETA;"
                          "database=Savith_Reddy;"
                          "Trusted_Connection=yes;"
                          )

    my_con = pyodbc.connect(conn_string,  autocommit = True)
    cursor = my_con.cursor()
    create_table_query = """
    CREATE TABLE Student (
    id int NOT NULL IDENTITY(1, 1),
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    age int,
    PRIMARY KEY (id)
    );
    """
    cursor.execute(create_table_query)
    insert_records_query = """
    INSERT INTO
    Student (first_name, last_name, age)
    VALUES
    ('Savith', 'Reddy', 28),
    ('Prathap', 'Reddy', 24),
    ('Swetha', 'Reddy', 24),
    ('Akhil', 'Reddy', 88)
    """
    cursor.execute(insert_records_query)

	
    select_record = '''SELECT * FROM Student'''
    cursor.execute(select_record)
    print(10*"*"+"before update"+10*"*")   
    for row in cursor:
        print(row)


    update_query = """
    UPDATE
    Student
    SET
    age = 29
    WHERE
    first_name = 'Akhil'

    """

    cursor.execute(update_query )
    select_record = '''SELECT * FROM Student'''
    cursor.execute(select_record)
    
    print(10*"*"+"after update"+10*"*")     
    for row in cursor:
        print(row)

    delete_query = "DELETE Student WHERE First_name = 'Prathap'"
    cursor.execute(delete_query)
    
    select_record = '''SELECT * FROM Student'''
    cursor.execute(select_record)
    print(10*"*"+"after delete"+10*"*")  
    for row in cursor:
        print(row)



if __name__ == '__main__':
    database_creation()




