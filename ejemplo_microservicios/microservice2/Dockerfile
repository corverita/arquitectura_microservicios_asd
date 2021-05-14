# Se indica qué tipo de proyecto es
FROM google/dart

# Se indica la version a utilizar de TINI y se realiza la descarga desde github
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini

# Se le dan permisos de ejecución al archivo tini y de indica como Entrypoint
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Se copian los archivos del directorio actual al directorio del contenedor
COPY . .

# Se ejecuta el archivo app.dart para iniciar el micro servicio.
RUN dart2native hello_dart/app.dart -o a.out
CMD ["./a.out"]