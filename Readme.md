Static: Así llamaremos a nuestra carpeta que tiene nuestros archivos estáticos. Aquí pondremos nuestros archivos de CSS o JavaScript

Motores de plantilla: estos tenemos en Python y lo que hacen es extender la funcionalidad de las plantillas de mi html

Layout.html: aquí pondremos todo el código que podamos reutilizar

Creación de entorno Virtual:
1.Ponemos todos nuestros archivos con código dentro de una carpeta que llamaremos src.
2.Para crear el entorno virtual vamos a usar un paquete de python que se llame "virtual env" https://docs.python-guide.org/dev/virtualenvs/
3.Creamos nuestro entorno virtual poniendo "python -m venv venv" en la consola en la carpeta en la que lo queramos crear.
4.Instalar Heroku CLI
5.Crear archivo requeriments.txt
6.Crear archivo runtime.text : este es para decirle que python está corriendo en mi aplicación.
7.Crear archivo Procfile : este le dice que archivo tiene que ejecutar cuando mi aplicación inicia, o sea que archivo va a ejecutar.
Instalamos guvicorn: para esto entramos a la carpeta Scripts dentro de venv por consola, y dentro de la consola (en Portafolio/venv/Scripts) instalamos o ejecutamos pip install gunicorn