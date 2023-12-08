Archivo Index.py: Archivo para arrancar nuestro sitio web.Aquí instalaremos render_template

Carpeta templates: va a tener todos los archivos html que quiero enviar, todo lo que el usuario vea.

Static: Así llamaremos a nuestra carpeta que tiene nuestros archivos estáticos. Aquí pondremos nuestros archivos de CSS o JavaScript

Motores de plantilla: estos tenemos en Python y lo que hacen es extender la funcionalidad de las plantillas de mi html

Layout.html: aquí pondremos todo el código que podamos reutilizar, o sea todo el código que va a ir en todas las paginas en el encabezado y pie de la pagina, luego se pone el codigo de cada pagina dentro del bloque 

Ejecutar en la consola "python index.py", o sea index.py es el nombre del archivo que corre las cosas y por el cual podemos ver en la pagina la app corriendo.

Creación de entorno Virtual: este sirve para separar nuestros proyectos de los otros proyectos, y de esta forma hacerlos mas livianos porque así solo tienen instaladas las librerías necesarias y no todas las de la compu
Pagina https://www.youtube.com/watch?v=fxavwHPJ36o&t=3253s empieza a crear el entorno virtual en el minuto 40
1.Ponemos todos nuestros archivos con código dentro de una carpeta que llamaremos src.
2.Para crear el entorno virtual vamos a usar un paquete de python que se llame "virtual env" https://docs.python-guide.org/dev/virtualenvs/
3.Creamos nuestro entorno virtual poniendo "python -m venv venv" en la consola en la carpeta en la que lo queramos crear.
4.Instalar Heroku CLI
5.Crear archivo requeriments.txt
6.Crear archivo runtime.text (minuto 50 del video): este es para decirle que python está corriendo en mi aplicación.
7.Crear archivo Procfile : este le dice que archivo tiene que ejecutar cuando mi aplicación inicia, o sea que archivo va a ejecutar.
Instalamos guvicorn: para esto entramos a la carpeta Scripts dentro de venv por consola, y dentro de la consola (en Portafolio/venv/Scripts) instalamos o ejecutamos pip install gunicorn