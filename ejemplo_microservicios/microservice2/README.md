# Microservice2: Dart - Ejemplo de Arquitecturas Microservicios

Esta carpeta contiene el código fuente del Microservice 2 para el sistema Ejemplo de Arquitecturas Microservicios. El microservicio fue desarrollada utilizando el lenguaje de programación Dart.

## Estructura del Directorio

- hello_dart: Directorio que almacena el código fuente del microservicio.
- Dockerfile: Archivo que contiene las configuraciones necesarias para el despliegue del microservicio en Docker.

### Construcción y ejecución del microservicio 2

- Estas son algunas consideraciones a tomar en cuenta para construir y ejecutar el contenedor del microservicio 2. Si ya se llevaron acabo estos pasos que son mencionados también en el archivo README.md de la carpeta raíz, por favor omitirlos.

   ```shell
   $ cd microservice2

   $ docker build -t api-dart:1.0 .

   $ docker run -d --name api-dart --network tyk --ip 172.15.0.5 api-dart:1.0
   ```

   En Linux:

   ```shell
   $ cd microservice2

   $ sudo docker build -t api-dart:1.0 .

   $ sudo docker run -d --name api-dart --network tyk --ip 172.15.0.5 api-dart:1.0
   ```


## Versión

1.0.0 - Marzo 2021

## Autores

* **Perla Velasco**
* **Jorge Alfonso Solís**