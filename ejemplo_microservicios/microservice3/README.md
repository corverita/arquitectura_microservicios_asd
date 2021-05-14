# Microservice3: django - Ejemplo de Arquitecturas Microservicios

Esta carpeta contiene el código fuente del Microservice 3 para el sistema Ejemplo de Arquitecturas Microservicios. El microservicio fue desarrollada utilizando el lenguaje de programación python y el framework django.

## Estructura del Directorio

- hello_django: Directorio que almacena el código fuente de la aplicación hello_django.
- microservice3: Directorio que almacena el código fuente de la aplicación en general.
- db.sqlite3: Archivo de la base de datos del microservicio.
- Dockerfile: Archivo que contiene las configuraciones necesarias para el despliegue del microservicio en Docker.
- gunicorn.conf: Archivo que contiene las configuraciones necesarias para el despliegue del microservicio.
- manage.py: Archivo para el manejo del sistema desarrollado con el Framework django.
- requirements.txt: Archivo que contiene las dependencias de la aplicación.

### Construcción y ejecución del microservicio 3

- Estas son algunas consideraciones a tomar en cuenta para construir y ejecutar el contenedor del microservicio 3. Si ya se llevaron acabo estos pasos que son mencionados también en el archivo README.md de la carpeta raíz, por favor omitirlos.

   ```shell
   $ cd microservice3

   $ docker build -t api-django:1.0 .

   $ docker run -d --name api-django --network tyk --ip 172.15.0.6 api-django:1.0
   ```

   En Linux:

   ```shell
   $ cd microservice3

   $ sudo docker build -t api-django:1.0 .

   $ sudo docker run -d --name api-django --network tyk --ip 172.15.0.6 api-django:1.0
   ```

## Versión

1.0.0 - Marzo 2021

## Autores

* **Perla Velasco**
* **Jorge Alfonso Solís**