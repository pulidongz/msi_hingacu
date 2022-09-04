FROM python:3.10.4-buster

# Install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log


RUN mkdir -p /home/msi_hingacu
RUN mkdir -p /home/msi_hingacu/backend
RUN mkdir -p /home/msi_hingacu/frontend
COPY /backend/requirements.txt start-server.sh /home/msi_hingacu/
COPY backend /home/msi_hingacu/backend/
WORKDIR /home/msi_hingacu/
RUN pip3 install -r requirements.txt
RUN chown -R www-data:www-data /home/msi_hingacu

# Start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/home/msi_hingacu/start-server.sh"]