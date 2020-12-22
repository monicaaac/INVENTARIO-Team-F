import sqlite3

con = sqlite3.connect('database.db')
print('Base de datos abierta')

cursorObj = con.cursor()

codigo = [7]
codigo = tuple(codigo)

cursorObj.execute('DELETE FROM usuarios WHERE id = ?', codigo)
con.commit()

cursorObj.execute('SELECT * FROM usuarios')
data = cursorObj.fetchall()
[print(row) for row in data]
