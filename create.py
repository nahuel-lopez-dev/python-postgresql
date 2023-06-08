import psycopg2

DROP_USERS_TABLE = 'DROP TABLE IF EXIST users'

USERS_TABLE = """
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
"""

if __name__ == '__main__':
    
    try:
        connect = psycopg2.connect('postgresql://user:password@localhost/databasename')
        
        with connect.cursor() as cursor:
            
            cursor.execute(DROP_USERS_TABLE)
            cursor.execute(USERS_TABLE)
            
            connect.commit()
            
    except psycopg2.OperationalError as err:
        print('No fue posible realizar la conexión')
        print(err)
    
    
    connect.close()