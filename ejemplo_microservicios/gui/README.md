# GUI - Ejemplo de Arquitecturas Microservicios

Esta carpeta contiene el código fuente de la GUI para el sistema Ejemplo de Arquitecturas Microservicios. La GUI fue desarrollada utilizando el framework Flask.

## Estructura del Directorio

- static: Directorio que almacena los archivos estáticos que utiliza la aplicación.
- templates: Directorio que almacena los archivos html utilizados para la interfaz gráfica de la aplicación.
- .python-version: Archivo con la versión utilizada de Python.
- Dockerfile: Archivo que contiene las configuraciones necesarias para el despliegue de la GUI.
- gui.py: Archivo que contiene el código fuente de la aplicación.
- gunicorn.conf: Archivo de configuraciones para el despliegue de la app en el contenedor.
- requirements.txt: Archivo que contiene las dependencias de la aplicación.
- wsgi.py: Archivo de configuraciones para el despliegue de la app.

### Construcción y ejecución de la GUI

- Estas son algunas consideraciones a tomar en cuenta para construir y ejecutar el contenedor de la interfaz de usuario. Si ya se llevaron acabo estos pasos que son mencionados también en el archivo README.md de la carpeta raíz, por favor omitirlos.

#### Construcción del contenedor de la GUI

- Ahora es momento de construir el contenedor de la GUI, para lograrlo ejecutamos los siguientes comandos:

   ```shell
   $ cd gui

   $ docker build -t gui:1.0 .
   ```

   En Linux:

   ```shell
   $ cd gui

   $ sudo docker build -t gui:1.0 .
   ```

#### Ejecución del contenedor de la GUI

- Para levantar el contenedor de la GUI ejecutamos el siguiente comando:

   ```shell
   $ docker run -d --name gui -p 5000:5000 gui:1.0
   ```

   En Linux:

   ```shell
   $ sudo docker run -d --name gui -p 5000:5000 gui:1.0
   ```

- Si todo se ejecutó con éxito podemos corroborar que nuestros contenedores se encuentran corriendo ejecutando el siguiente comando:

   ```shell
   $ docker ps
   ```

   En Linux:

   ```shell
   $ sudo docker ps
   ```

   Este comando nos mostrará los contenedores que se encuentran corriendo, en la columna Status, debemos observar la palabra UP en los contenedores gui, api-python, api-dart, api-django, redis y tykio/tyk-gateway.

- Ya que confirmamos que nuestros contenedores se encuentran corriendo podremos ingresar a nuestro navegador y verificar que el sistema de ejemplo para probar los microservicios se encuentra funcionando correctamente, ingresamos a la siguiente url: 

> http://localhost:5000/


## Versión

1.0.0 - Marzo 2021

## Autores

* **Perla Velasco**
* **Jorge Alfonso Solís**

* **Luis Alberto Gómez Delgado**
* **Martín Salas Orozco**
* **Jose De Jesus Jimenez Arguelles**
* **Gerardo Jimenez Arguelles**
* **Oscar Leonardo Corvera Espinosa**
