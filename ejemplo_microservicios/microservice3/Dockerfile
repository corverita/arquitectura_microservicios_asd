# Se indica qué tipo de proyecto es, incluyendo la versión del lenguaje
FROM python:3.9

# Se indica al OS del contenedor que se ejecute de manera non-interactive
# es decir, suprime prompts y solo acepta por defecto de manera automática.
ENV DEBIAN_FRONTEND=noninteractive

# Se instalan paquetes necesarios
RUN apt update; \
    apt -yq upgrade; \
    apt-get --allow-unauthenticated install -y --no-install-recommends \
    supervisor \
    apt-utils \
    nano; \
    apt-get -yq autoremove; \
    apt-get clean; \ 
    rm -rf /var/lib/apt/lists/*

# Se crean directorios que serán utilizados
RUN mkdir -p /usr/api
RUN mkdir -p /usr/api/logs
RUN mkdir -p /var/log/supervisor

# Se indica el directorio de trabajo
WORKDIR /usr/api

# Se copia el archivo gunicorn.conf en el directorio de trabajo del contenedor
COPY ./gunicorn.conf /etc/supervisor/conf.d/supervisord.conf

# Se copia el contenido de este directorio en el directorio de trabajo del contenedor
COPY . /usr/api

# Se actualiza pip y se instalan los requerimientos necesarios
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Se expone el puerto 49001 para acceder a la aplicación
EXPOSE 49003

# Se ejecuta el archivo supervisord que inicia el micro servicio en django
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]