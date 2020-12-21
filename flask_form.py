from flask import Flask, render_template, request
import DB_Object

app = Flask(__name__)

usuario = ''

@app.route("/")
def show_login_form():
    return render_template("login.html")


@app.route("/validar/", methods=["GET", "POST"])
def validar_usuario():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    DB_Object.sql_connection()
    validacion = DB_Object.sql_validacion_credenciales(username, password)
    DB_Object.sql_cerrar()

    if validacion[0] is True:
        return render_template("home.html")
    elif validacion[0] is False:
        return render_template("login.html")


@app.route("/modificar/", methods=["GET", "POST"])
def show_modificar_form():
    action = request.form.get('action')
    print(action)
    if action == 'Modificar':
        return '<h1>Producto modificado</h1>'
    if action == 'Eliminar':
        return '<h1>Producto Eliminado</h1>'




if __name__ == '__main__':
    app.run(debug=True)
