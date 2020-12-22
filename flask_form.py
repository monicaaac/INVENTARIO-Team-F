from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
import DB_Object

app = Flask(__name__)

UPLOAD_FOLDER = r'C:\Users\57301\Desktop\Pagina web\INVENTARIO-Team-F-main\static'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



tipo_usuario = ''


@app.route("/")
def show_login_form():
    global tipo_usuario
    tipo_usuario = ''
    return render_template("login.html")


@app.route("/validar/", methods=["GET", "POST"])
def validar_usua():
    global tipo_usuario
    tipo_usuario = ''

    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    DB_Object.sql_connection()
    validacion = DB_Object.sql_validacion_credenciales(username, password)
    DB_Object.sql_cerrar()

    if validacion[0] is True:
        tipo_usuario = validacion[1]
        print(tipo_usuario)
        if tipo_usuario == 'admin':
            return render_template("home.html")
        elif tipo_usuario == 'vend':
            return render_template("home1.html")
    elif validacion[0] is False:
        return render_template("login.html")

@app.route("/recuperar_psswd")
def recuperar_psswd():
    return render_template("recuperar_psswd.html")


@app.route("/crearproducto/")
def show_crearproducto_form():
    global tipo_usuario
    if tipo_usuario == 'admin':
        return render_template('crear_producto.html')
    else:
        return render_template("login.html")


@app.route("/crearproducto/crear/", methods=["GET", "POST"])
def show_crearproducto():
    global tipo_usuario
    if tipo_usuario == 'admin':
        if request.method == 'POST':
            file = request.files['file']
            codigo = request.form.get('codigo')
            nombre = request.form.get('nombre')
            precio = request.form.get('precio')
            cantidad = request.form.get('cantidad')

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(file.filename)

            DB_Object.sql_connection()
            DB_Object.sql_crear_producto(codigo, nombre, precio, cantidad, file.filename)
            DB_Object.sql_cerrar()

        if tipo_usuario == 'admin':
            return render_template('home.html')
        if tipo_usuario == 'vend':
            return render_template('home1.html')

    else:
        return render_template("login.html")



@app.route("/modificar/")
def show_modificar_form():
    global tipo_usuario
    return render_template('modificar_eliminar_producto.html')



@app.route("/modificar/mod/", methods=["GET", "POST"])
def modificar():
    action = request.form.get('action')
    print(action)
    if tipo_usuario == 'admin':
        if request.method == 'POST':
            if 'file' in request.files:
                file = request.files['file']
            codigo = request.form.get('codigo')
            nombre = request.form.get('nombre')
            precio = request.form.get('precio')
            cantidad = request.form.get('cantidad')

            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print(file.filename)

            DB_Object.sql_connection()
            if action == 'Modificar':
                if codigo:
                    if nombre:
                        DB_Object.sql_modificar_producto_nombre(codigo, nombre)
                    if precio:
                        DB_Object.sql_modificar_producto_precio(codigo, precio)
                    if cantidad:
                        DB_Object.sql_modificar_producto_cantidad(codigo, cantidad)
                    if file:
                        DB_Object.sql_modificar_producto_rutaimagen(codigo, file.filename)
                DB_Object.sql_cerrar()
                return render_template("home.html")

            if action == 'Eliminar':
                DB_Object.sql_borrarproducto(codigo)
                DB_Object.sql_cerrar()
                return render_template("home.html")

    else:
        return render_template("login.html")


@app.route("/crearusuario/", methods=["GET", "POST"])
def crearusuario():
    global tipo_usuario
    if tipo_usuario == 'admin':
        return render_template('crear_usuario.htm')
    else:
        return render_template("login.html")


@app.route("/crearusuario/crear/", methods=["GET", "POST"])
def crearusuarioo():
    global tipo_usuario
    if tipo_usuario == 'admin':
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            tipo = request.form.get('tipo')

            DB_Object.sql_connection()
            DB_Object.sql_crear_usuario(username, password, tipo)
            DB_Object.sql_cerrar()

        if tipo_usuario == 'admin':
            return render_template('home.html')
        if tipo_usuario == 'vend':
            return render_template('home1.html')

    else:
        return render_template("login.html")


@app.route("/modificarinventario/", methods=["GET", "POST"])
def show_modificarinventario():
    global tipo_usuario
    if tipo_usuario == 'admin' or tipo_usuario == 'vend':
        return render_template('modificar_inventario.htm')
    else:
        return render_template("login.html")


@app.route("/modificarinventario/mod/", methods=["GET", "POST"])
def modificarinventario():
    global tipo_usuario
    if tipo_usuario == 'admin' or tipo_usuario == 'vend':
        if request.method == 'POST':
            codigo = request.form.get('codigo')
            cantidad = request.form.get('cantidad')

            DB_Object.sql_connection()
            DB_Object.sql_modificar_producto_cantidad(codigo, cantidad)
            DB_Object.sql_cerrar()
        if tipo_usuario == 'admin':
            return render_template('home.html')
        if tipo_usuario == 'vend':
            return render_template('home1.html')

    else:
        return render_template("login.html")


@app.route("/productos/", methods=["GET", "POST"])
def show_productos():
    filename = []
    DB_Object.sql_connection()
    rows = DB_Object.sql_obtener_tabla_productos()
    DB_Object.sql_cerrar()

    print(rows)
    return render_template("productos.html", rows=rows)


@app.route("/buscarproducto/", methods=["GET", "POST"])
def buscarproducto():
    return('<h1>Falta pagina buscar producto</h1>')


@app.route("/signout/", methods=["GET", "POST"])
def signout():
    global tipo_usuario
    tipo_usuario = ''

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
