# Index.py: Archivo para arrancar nuestro sitio web.Aquí instalaremos los paquetes y los códigos
# Carpeta templates: va a tener todos los archivos html que quiero enviar, todo lo que el usuario vea
from flask import Flask, render_template, request, redirect, url_for, flash
#url_for es una función de Flask que genera una URL para la función especificada.
#render_template: te lleva a un archivo html
#from flask_mysqldb import MySQL
# __name__:variable que me da python, es para confirmar que estoy en el archivo principal, quiere decir que es el archivo que me va a arrancar la aplicación
app = Flask(__name__)
# Vamos a hacer dos rutas, la función route() es para hacer rutas


#Mysql Connection
#app.config['MYSQL_HOST']='localhost'
#app.config['MYSQL_USER']='root'
#app.config['MYSQL_PASSWORD']=''
#app.config['MYSQL_DB']='flaskcontacts'
#mysql = MySQL(app)


@app.route("/")  # cuando se pone ("/") quiere decir que es mi pagina principal
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/proyectos")
def proyectos():
    return render_template("proyectos.html")

@app.route("/analisisprocesos")
def analisisprocesos():
    return render_template("analisisprocesos.html")

@app.route("/cienciadedatos")
def cienciadedatos():
    return render_template("cienciadedatos.html")

@app.route("/inteligenciaartificial")
def inteligenciaartificial():
    return render_template("inteligenciaartificial.html")



#@app.route("/Dataengineer")
#def redirect_to_dataengineer():
#    return  redirect(url_for('dataengineer'))







#@app.route('/Dataengineer')
#def dataengineer():
#    cur=mysql.connection.cursor()
#    cur.execute('SELECT * FROM contacts')
#    data=cur.fetchall()
     # Aqui hacemos la consulta para que aparezcan los datos que ya han sido agregados a la tabla
#    return render_template('dataengineer.html', contacts=data)

# settings: es para decirle, como va ir proteguida nuestra cesión
app.secret_key = "mysecretkey"


#@app.route('/Dataengineer/add_contact', methods=['POST'])
#def add_contact():
#    if request.method == 'POST':
#        fullname = request.form['fullname']
#        phone = request.form['phone']
#        email = request.form['email']
#        cur=mysql.connection.cursor() #esto se llama cursor, y es para saber donde la conexión (mas o menos es eso)
#        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)',
#                    (fullname, phone, email)) # aqui se "Escriben" las consultas sql select, into, insert
#        # INSERT INTO contacts : significa "Insertar dentro de contactos"
#        mysql.connection.commit() # Aquí se ejecutan las consultas y en este caso se guardan las consultas
#        flash('Contact Added successfully') #Esto "flash es para agregar un mensaje"
#        print(fullname)
#        print(phone)
#        print(email)
#        return redirect(url_for('dataengineer')) 
    # lo que hace con "return" esto es retornar a la vista de index nuevamente para seguir cargando datos

#,methods=['GET', 'POST']

#@app.route('/Dataengineer/edit/<id>')
#def get_contact(id):
#    cur=mysql.connection.cursor()
#    cur.execute('SELECT * FROM contacts WHERE id= %s', [id])
#    data = cur.fetchall()
#    return render_template('edit-contact.html', contact =data[0])

#,methods=['POST']
#@app.route('/Dataengineer/update/<id>',methods=['POST'])
#def update_contact(id):
#    if request.method == 'POST':
#        fullname =request.form['fullname']
#        phone =request.form['phone']
#        email =request.form['email']
#        cur=mysql.connection.cursor()
#        cur.execute("""UPDATE contacts
#                    SET fullname=%s,
#                    phone=%s,
#                    email=%s
#                    WHERE id=%s
#                    """,(fullname, phone, email, id))
#        mysql.connection.commit()
#        flash('Contact Update Succesffuly')
#        return redirect(url_for('dataengineer'))


#@app.route('/Dataengineer/delete/<string:id>') 
# Esta ruta delete recibe un parametro string de tipo id. 
# De esta manera le digo que cuando reciba una ruta delete
# debe tener al lado un id para luego nosotros usar ese numero para poder borrarlo

#def delete_contact(id):
#    cur=mysql.connection.cursor() #Aquí obtenemos el cursor
#    cur.execute('DELETE FROM contacts WHERE id={0}'.format(id)) # Aquí ejecutamos hacemos la consulta
#    mysql.connection.commit()
#    flash('Contact Removed Successfully')
#    return redirect(url_for('dataengineer'))





@app.route("/curiosidades")
def curiosidades():
    return render_template("curiosidades.html")

@app.route("/curriculum")
def curriculum():
    return render_template("curriculum.html")

if __name__ == "__main__":  # esta es una validación para asegurarnos que estamos en la pagina principal
    app.run(host='0.0.0.0', port=5000,debug=False)  # debug=True con esto decimos que nuestra pagina va a a estar en un periodo de pruebay así no tenemos que estar todo el tiempo ejecutando "python index.py" y se va actualizando solo, luego en producción hay que ponerle off para que no se edite
    