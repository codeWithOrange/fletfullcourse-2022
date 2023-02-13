import sqlite3 

try:
    connection=sqlite3.connect('users.db')
    cursor=connection.cursor()
    query='''
        CREATE TABLE USERS(username varcha (100) not null, email varchar(100) not null, password varchar(10) not null)

    '''
    cursor.execute(query)
    


except sqlite3.Error as error:
    print('error occured in sqlite connecntion', error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print('connection closed')

