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
def create_user():
    """ A) Crear Usuario"""
    print('Usuario Creado')

# Read
def list_users():
    """ B) Listar Usuarios"""
    print('Listado de Usuarios')

# Update
def update_user():
    """ C) Actualizar Usuario"""
    print('Usuario actualizado')

# Delete
def delete_user():
    """ D) Eliminar Usuario"""
    print('Usuario eliminado')

def default():
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
            
            cursor.execute(DROP_USERS_TABLE)
            cursor.execute(USERS_TABLE)
            
            connect.commit()
            
            while True:
                
                for function in options.values():
                    print(function.__doc__)
                
                print('quit para salir')
                
                option = input('Selecciona una opción válida').lower()
                
                if option == 'quit' or option == 'q':
                    break 
                
                function = options.get(option, default)
                function()   
            
    except psycopg2.OperationalError as err:
        print('No fue posible realizar la conexión')
        print(err)
    
    
    connect.close()