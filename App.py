from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
#from pymysql import cursors


#Mysql Connection
app = Flask(__name__)
app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskclient'
#app.config['MYSQL_DATABASE_HOST']='localhost'
#app.config['MYSQL_DATABASE_PORT']='3306'
#app.config['MYSQL_DATABASE_USER']='root'
#app.config['MYSQL_DATABASE_PASSWORD']=''
#app.config['MYSQL_DATABASE_DB']='flaskclient'
#app.config['MYSQL_DATABASE_CHARSET']='utf-8'
#app.config['MYSQL_DATABASE_SOCKET']='/var/run/mysqld/mysqld.sock'
#app.config['MYSQL_CURSORCLASS']=''
mysql = MySQL(app)
#mysql = MySQL(cursorclass=cursors.DictCursor)
#mysql.init_app(app)

# setting
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('Select * from cliente')
    data = cur.fetchall()
    #print(data)
    return render_template('index.html',clients=data)
    #return("Hola")

@app.route('/add', methods=['POST'])
def add_client():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ip_antena = request.form['ip_antena']
        ip_router = request.form['ip_router']
        cur = mysql.connection.cursor()
        #print(nombre)
        #print(ip_router)
        #print(ip_antena)
        #cursor = mysql.get_db().cursor()
        cur.execute('Insert into cliente (nombre,ip_antena,ip_router) values (%s, %s, %s)',
        (nombre,ip_antena,ip_router))
       # mysql.connection.commit()
        mysql.connection.commit()
        flash('Contact added successfully')
        return redirect(url_for('Index'))
        
  
    

@app.route('/edit/<string:id>')
def edit_client(id):
    cur = mysql.connection.cursor()
    #cur.execute('select * from cliente where id = '+id+'')
    cur.execute('select * from cliente where id = %s',[id])
    data = cur.fetchall()
    print(data[0])
    return render_template('edit.html',clients = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        ip_antena = request.form['ip_antena']
        ip_router = request.form['ip_router']
        cur = mysql.connection.cursor()
        cur.execute("""
        update cliente
        set nombre = %s,
        ip_antena = %s,
        ip_router = %s
        where id = %s
        """,(nombre,ip_antena,ip_router,id))
        cur.connection.commit()
        flash('Contact Updated Successfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_client(id):
    cur = mysql.connection.cursor()
    #cur.execute('Delete from cliente where id= {0}'.format(id))
    cur.execute('Delete from cliente where id = '+id+'')
    #print("contacto: "+id)
    cur.connection.commit()
    #return 'Eliminar Contacto: '+id
    flash('Client removed successfull')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000,debug = True)




