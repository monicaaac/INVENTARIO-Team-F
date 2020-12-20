      
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Login():
    return render_template('Login.html')

@app.route('/recuperar_psswd')
def recuperar_psswd():
    return render_template('recuperar_psswd.html')



if __name__ == '__main__':
    app.run(debug=True)

