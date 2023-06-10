import psycopg2

DROP_USERS_TABLE = 'DROP TABLE IF EXIST users'

USERS_TABLE = """
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
"""
##### CRUD #####

# Create
def create_user(connect, cursor):
    """ A) Crear Usuario"""
    username = input('Ingresa un username:')
    email = input('Ingresa un email:')
    
    query = 'INSERt INTO users(username, email) VALUE(%s, %s)'
    values = (username, email)
    
    cursor.execute(query, values)
    connect.commit()
    
    print('>>> Usuario creado')

# Read
def list_users(connect, cursor):
    """ B) Listar Usuarios"""
    query = 'SELECT id, username, email FROM users'
    cursor.execute(query)
    
    for id, username, email in cursor.fetchall():
        print(f'{id} - {username} - {email}')
    
    print('Listado de Usuarios')

# Update
def update_user(connect, cursor):
    """ C) Actualizar Usuario"""
    print('Usuario actualizado')

# Delete
def delete_user(connect, cursor):
    """ D) Eliminar Usuario"""
    print('Usuario eliminado')

def default(*args):
    print('¡Opción no válida!')

if __name__ == '__main__':
    
    options = {
        'a': create_user,
        'b': list_users,
        'c': update_user,
        'd': delete_user
    }
    
    try:
        connect = psycopg2.connect('postgresql://user:password@localhost/databasename')
        
        with connect.cursor() as cursor:
            
            # cursor.execute(DROP_USERS_TABLE)
            # cursor.execute(USERS_TABLE)
            
            connect.commit()
            
            while True:
                
                for function in options.values():
                    print(function.__doc__)
                
                print('quit para salir')
                
                option = input('Selecciona una opción válida').lower()
                
                if option == 'quit' or option == 'q':
                    break 
                
                function = options.get(option, default)
                function(connect, cursor)   
            
    except psycopg2.OperationalError as err:
        print('No fue posible realizar la conexión')
        print(err)
    
    
    connect.close()