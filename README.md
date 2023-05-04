# API Rest | Regiones de Chile 🇨🇱

# Detalle
Esta es una Api Rest donde permite registrar, actualizar, eliminar y listar las regiones de todo chile

# Tecnologias
- Python 3.10.9
- Django 4.2.1
- REST Framework
- MySql

# Instalación de Dependencias
Para instalar las dependencias del proyecto, se adjunta un archivo llamado requirements.txt con todas las librerias necesarias. Pero primero, se debe crear un entorno virtual con Python usando el comando:

    python -m venv env 

Después de ejecutar el comando, se creará una carpeta con el entorno virtual. Para activar el entorno virtual, ejecute el archivo activate.bat ubicado en env\Scripts\activate.bat. Con el entorno virtual activado, instale las dependencias del proyecto usando el comando:

    pip install -r requirements.txt

Posteriormente se instalarán las dependencias para ejecutar el proyecto.

# Migraciones
Para migrar los modelos a la base de datos, primero debe configurar el archivo settings.py con los detalles de conexión de la base de datos, tambien se debe crear una carpeta llamada migrations en la app regiones junto con un archivo __init__.py. Una vez que hayas hecho la configuración, ejecuta el comando:

    python manage.py makemigrations

Esto creará los archivos de migración. Luego, ejecute el comando:

    python manage.py migrate 

Esto ejecutará todas las migraciones y creará las tablas en la base de datos.

# Ejecución
Para ejecutar el proyecto, active el entorno virtual con las dependencias instaladas y luego ejecute el comando:

    python manage.py runserver (optional port number)
    
El número de puerto es opcional. Si no proporciona un número de puerto, el servidor se ejecutará en el puerto 8000 en localhost.