# Microservice1: Python - Ejemplo de Arquitecturas Microservicios

Esta carpeta contiene el código fuente del Microservice 1 para el sistema Ejemplo de Arquitecturas Microservicios. El microservicio fue desarrollada utilizando el lenguaje de programación python y el framework Falcon.

## Estructura del Directorio

- deployment: Directorio que almacena el archivo gunicorn.conf para el despliegue del microservicio.
- hello_python: Directorio que almacena el código fuente del microservicio.
- .python-version: Archivo con la versión utilizada de Python.
- Dockerfile: Archivo que contiene las configuraciones necesarias para el despliegue del microservicio 1 en Docker.
- requirements.txt: Archivo que contiene las dependencias de la aplicación.

### Construcción y ejecución del microservicio 1

- Estas son algunas consideraciones a tomar en cuenta para construir y ejecutar el contenedor del microservicio 1. Si ya se llevaron acabo estos pasos que son mencionados también en el archivo README.md de la carpeta raíz, por favor omitirlos.

   ```shell
   $ cd microservice1

   $ docker build -t api-python:1.0 .

   $ docker run -d --name api-python --network tyk --ip 172.15.0.4 api-python:1.0
   ```

   En Linux:

   ```shell
   $ cd microservice1

   $ sudo docker build -t api-python:1.0 .

   $ sudo docker run -d --name api-python --network tyk --ip 172.15.0.4 api-python:1.0
   ```


## Versión

1.0.0 - Marzo 2021

## Autores

* **Perla Velasco**
* **Jorge Alfonso Solís**