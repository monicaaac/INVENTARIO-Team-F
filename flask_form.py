from flask import Flask, render_template, request
import DB_Object

app = Flask(__name__)


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
        ruta_imagen = request.form.get('archivo')
        codigo = request.form.get('codigo')
        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        cantidad = request.form.get('cantidad')

        print(ruta_imagen)

        DB_Object.sql_connection()
        DB_Object.sql_crear_producto(codigo, nombre, precio, cantidad, ruta_imagen)
        DB_Object.sql_cerrar()

        return render_template("home.html")

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
    if action == 'Modificar':
        return '<h1>Producto modificado</h1>'
    if action == 'Eliminar':
        return '<h1>Producto Eliminado</h1>'


@app.route("/crearusuario/", methods=["GET", "POST"])
def crearusuario():
    global tipo_usuario
    if tipo_usuario == 'admin':
        return render_template('crear_usuario.html')
    else:
        return render_template("login.html")


@app.route("/buscarproducto/", methods=["GET", "POST"])
def buscarproducto():
    return('<h1>Falta pagina buscar producto</h1>')


@app.route("/signout", methods=["GET", "POST"])
def signout():
    global tipo_usuario
    tipo_usuario = ''

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
