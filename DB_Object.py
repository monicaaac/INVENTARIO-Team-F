import sqlite3

from sqlite3 import Error


def sql_connection():
    global con

    try:

        con = sqlite3.connect('database.db')
        print('Base de datos abierta')
        return con

    except Error:

        print(Error)


def sql_cerrar():
    global con
    try:
        con.close()
    except:
        print("La base de datos no se ha abierto")
    finally:
        print('Base de datos cerrada')


def sql_crear_producto(id, nombre, precio, cantidad, rutaimagen):
    global con

    entities = (id, nombre, precio, cantidad, rutaimagen)

    cursorObj = con.cursor()

    cursorObj.execute('INSERT INTO productos (id, nombre, precio, cantidad, imagen) VALUES(?, ?, ?, ?, ?)', entities)

    con.commit()


def sql_modificar_producto(id, nombre = '', precio = -1, cantidad = -1, rutaimagen= ''):
    global con
    cursorObj = con.cursor()

    if nombre != '' and precio != -1 and cantidad != -1 and rutaimagen != '':
        cursorObj.execute("UPDATE productos SET nombre = ?, precio = ?, cantidad = ?, imagen = ? where id = ?", (nombre, precio, cantidad, rutaimagen,id))

    if nombre != '':
        cursorObj.execute("UPDATE productos SET nombre = ? where id = ?", (nombre, id))

    if precio != -1:
        cursorObj.execute("UPDATE productos SET precio = ? where id = ?", (precio, id))

    if cantidad != -1:
        cursorObj.execute("UPDATE productos SET cantidad = ? where id = ?", (cantidad, id))

    if rutaimagen != '':
        cursorObj.execute("UPDATE productos SET imagen = ? where id = ?", (rutaimagen, id))

    con.commit()


def sql_modificar_producto_nombre(id, nombre):
    global con
    cursorObj = con.cursor()
    cursorObj.execute("UPDATE productos SET nombre = ? where id = ?", (nombre, id))
    con.commit()


def sql_modificar_producto_precio(id, precio):
    global con
    cursorObj = con.cursor()
    cursorObj.execute("UPDATE productos SET precio = ? where id = ?", (precio, id))
    con.commit()


def sql_modificar_producto_cantidad(id, cantidad):
    global con
    cursorObj = con.cursor()
    cursorObj.execute("UPDATE productos SET cantidad = ? where id = ?", (cantidad, id))
    con.commit()


def sql_modificar_producto_rutaimagen(id, rutaimagen):
    global con
    cursorObj = con.cursor()
    cursorObj.execute("UPDATE productos SET imagen = ? where id = ?", (rutaimagen, id))
    con.commit()


def sql_crear_usuario(usuario, clave, tipo):
    global con
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM usuarios')
    id = len(cursorObj.fetchall()) + 1
    print('el id es: ', id)
    cursorObj.execute("INSERT INTO usuarios (id, usuario, clave, tipo) VALUES(?, ?, ?, ?)", (id, usuario, clave, tipo))
    con.commit()


def sql_obtener_tabla_productos():
    global con
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM productos')

    rows = cursorObj.fetchall()

    return rows


def sql_obtener_tabla_usuarios():
    global con

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM usuarios')

    rows = cursorObj.fetchall()

    return rows


def sql_validacion_credenciales(username, password):
    global con

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM usuarios')

    rows = cursorObj.fetchall()

    captura = ''

    for row in rows:
        if row[1] == username:
            captura = row
            print(row)
            break
    if captura == '':
        return False, ''
    if row[2] == password:
        return True, captura[3]
    else:
        return False, ''


def sql_borrarproducto(id):
    global con

    cursorObj = con.cursor()
    id = int(id)

    codigo = []
    codigo.append(id)
    codigo = tuple(codigo)

    cursorObj.execute('DELETE FROM productos WHERE id = ?', codigo)
    con.commit()




