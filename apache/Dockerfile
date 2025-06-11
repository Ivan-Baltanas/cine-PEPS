# Usamos una imagen base de Ubuntu 24.04
FROM ubuntu:24.04

# Actualizamos los repositorios y luego instalamos Apache y los módulos necesarios
RUN apt-get update && \
    apt-get install -y apache2 apache2-utils git libapache2-mod-security2&& \
    a2enmod proxy && \
    a2enmod proxy_http && \
    a2enmod rewrite && \
    apt-get clean

# Copiar el archivo de configuración personalizado de Apache
COPY apache/demo.apache.conf /etc/apache2/sites-available/000-default.conf

# Descargar OWASP CRS
RUN git clone --depth 1 https://github.com/coreruleset/coreruleset.git /opt/owasp-crs && \
    cp /opt/owasp-crs/crs-setup.conf.example /opt/owasp-crs/crs-setup.conf && \
    ln -s /opt/owasp-crs /etc/modsecurity/owasp-crs

# Configurar Apache para cargar CRS sin conflictos
RUN echo "Include /etc/modsecurity/owasp-crs/crs-setup.conf" > /etc/apache2/mods-enabled/security2.conf && \
    echo "Include /etc/modsecurity/owasp-crs/rules/*.conf" >> /etc/apache2/mods-enabled/security2.conf
# Copiar los archivos estáticos al directorio correspondiente en el contenedor
RUN rm /var/www/html/index.html && \
    cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf && \
    sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/' /etc/modsecurity/modsecurity.conf

#COPY ./static/*.h /var/www/html

# Exponer el puerto 80 para que Apache pueda servir el contenido
EXPOSE 80

# Iniciar Apache en primer plano
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
