from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from pymysql import cursors

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PORT']='3306'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='flaskclient'
app.config['MYSQL_DATABASE_CHARSET']='utf-8'
app.config['MYSQL_DATABASE_SOCKET']='C:/xampp/mysql/mysql.sock'
app.config['MYSQL_CURSORCLASS']='DictCursor'

#mysql = MySQL()
mysql = MySQL(cursorclass=cursors.DictCursor)
mysql.init_app(app)

@app.route('/')
def Index():
    return render_template('index.html')
    #return("Hola")

@app.route('/add_client', methods=['POST'])
def add_client():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ip_router = request.form['ip_router']
        ip_antena = request.form['ip_antena']
        cur = mysql.get_db().cursor()  
       # cursor = mysql.get_db().cursor()
        cur.execute('Insert into client (nombre,ip_antena,ip_router) values (%s, %s, %s)',
        (nombre,ip_antena,ip_router))
        return 'Recived'
        
  
    

@app.route('/edit')
def edit_client():
    return 'Editar Contacto'

@app.route('/delete')
def delete_client():
    return 'Eliminar Contacto'

if __name__ == '__main__':
    app.run(port = 5000,debug = True)




