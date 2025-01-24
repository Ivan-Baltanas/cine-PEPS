# Usamos una imagen base de Ubuntu 14.04
FROM ubuntu:14.04

# Actualizamos los repositorios y luego instalamos Apache y los módulos necesarios
RUN apt-get update && \
    apt-get install -y apache2 apache2-utils && \
    a2enmod proxy && \
    a2enmod proxy_http && \
    a2enmod rewrite && \
    apt-get clean

# Copiar el archivo de configuración personalizado de Apache
COPY demo.apache.conf /etc/apache2/sites-available/000-default.conf

# Copiar los archivos estáticos al directorio correspondiente en el contenedor
RUN rm /var/www/html/index.html

COPY ./static /var/www/html/static

# Exponer el puerto 80 para que Apache pueda servir el contenido
EXPOSE 80

# Iniciar Apache en primer plano
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]