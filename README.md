# Certificados

Este es un proyecto de ejemplo para la creación de certificados utilizando Python y Django.

## Requisitos

- Python 3.8 o superior
- Django 3.2 o superior

## Instalación

1. Clonar el repositorio:

git clone https://github.com/EdwardAJ6/Certificados.git


2. Acceder al directorio del proyecto:
cd Certificados


3. Crear un entorno virtual:

python -m venv env


4. Activar el entorno virtual:

- Windows: 

  ```
  env\Scripts\activate
  ```

- Linux/macOS:

  ```
  source env/bin/activate
  ```

5. Instalar los requerimientos:

pip install -r requirements.txt


6. Realizar las migraciones:

python manage.py migrate


7. Crear un usuario administrador:

python manage.py createsuperuser


## Uso

1. Iniciar el servidor:

python manage.py runserver


2. Acceder a la página de administración en `http://localhost:8000/admin`

3. Ingresar con las credenciales del usuario administrador creado anteriormente.

4. Crear un nuevo curso y sus respectivas etapas.

5. Acceder a la página principal en `http://localhost:8000`

6. Ingresar el nombre del usuario y seleccionar el curso correspondiente.

7. Completar todas las etapas del curso.

8. Generar el certificado en la página de detalles del curso.

## Créditos

- [Edward Iva Alba Jerez](https://github.com/EdwardAJ6)
