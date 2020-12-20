# from flask import Flask

# app= Flask(__name__)
# @app.route("/")
# def hola():
#         return "<h1>hola soy yamile</h1>"

# if __name__=='__main__':
#     app.run()

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('login.html')

if __name__=='__main__':
    app.run()

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template('login.html')


#     if __name__=='__main__':
#         app.run()