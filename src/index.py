# Index.py: Archivo para arrancar nuestro sitio web.Aquí instalaremos los paquetes y los códigos
from flask import Flask, render_template
# Carpeta templates: va a tener todos los archivos html que quiero enviar, todo lo que el usuario vea
# __name__:variable que me da python, es para confirmar que estoy en el archivo principal, quiere decir que es el archivo que me va a arrancar la aplicación
app = Flask(__name__)
# Vamos a hacer dos rutas, la función route() es para hacer rutas


@app.route("/")  # cuando se pone ("/") quiere decir que es mi pagina principal
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":  # esta es una validación para asegurarnos que estamos en la pagina principal
    app.run(debug=True)  # debug=True con esto decimos que nuestra pagina va a a estar en un periodo de pruebay así no tenemos que estar todo el tiempo ejecutando "python index.py" y se va actualizando solo, luego en producción hay que ponerle off para que no se edite
    