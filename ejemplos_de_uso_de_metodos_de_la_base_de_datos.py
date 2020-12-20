import DB_Object

DB_Object.sql_connection()

# Ejemplo de creacion de producto
try:
    DB_Object.sql_crear_producto(8, 'Perfume', 35000, 20, r'E:\arrebatan.jpg')
except:
    DB_Object.sql_cerrar()

DB_Object.sql_cerrar()

# Ejemplo de edicion de tabla de productos
DB_Object.sql_connection()

DB_Object.sql_modificar_producto(2, 'Antonio')
DB_Object.sql_modificar_producto_nombre(3, 'Julian')
DB_Object.sql_modificar_producto_rutaimagen(8, 'nuevaruta')
DB_Object.sql_modificar_producto_precio(5, 56000)
DB_Object.sql_modificar_producto_cantidad(4, 65)

DB_Object.sql_cerrar()

# Ejemplo de creacion de usuario
DB_Object.sql_connection()

DB_Object.sql_crear_usuario('otrousuario', 'clave', 'admin')

DB_Object.sql_cerrar()


# Ejemplo de obtener base de datos de productos
DB_Object.sql_connection()
productos = DB_Object.sql_obtener_tabla_productos()
DB_Object.sql_cerrar()

for row in productos:
    print(row)

# Ejemplo de obtener base de datos de usuarios
DB_Object.sql_connection()
usuarios = DB_Object.sql_obtener_tabla_usuarios()
DB_Object.sql_cerrar()
print(usuarios)

for row in usuarios:
    print(row)


#Ejemplo de validacion de usuario
DB_Object.sql_connection()
DB_Object.sql_validacion_credenciales('favillamizar@uninorte.edu.co', '123456')
DB_Object.sql_cerrar()