FROM alpine:3.16.0

#Python
RUN apk update
RUN apk add python3
RUN apk add py3-pip
RUN apk add python3-tkinter
RUN pip install mysql-connector-python
RUN pip install tkcalendar
RUN apk add ttf-dejavu fontconfig

#GIT
RUN apk add git
#BASH
RUN apk add bash

#SSH for X11 forwarding
#RUN apk add xeyes
RUN apk add openssh-server
RUN apk add xauth
RUN mkdir /var/run/sshd
RUN mkdir /root/.ssh
RUN chmod 700 /root/.ssh
RUN ssh-keygen -A
RUN sed -i "s/^.*PasswordAuthentication.*$/PasswordAuthentication no/" /etc/ssh/sshd_config
RUN sed -i "s/^.*X11Forwarding.*$/X11Forwarding yes/" /etc/ssh/sshd_config
RUN sed -i "s/^.*X11Forwarding.*$/X11Forwarding yes/" /etc/ssh/sshd_config
RUN grep "^X11UseLocalhost" /etc/ssh/sshd_config || echo "X11UseLocalhost no" >> /etc/ssh/sshd_config

# Configure supervisor to control SSH process
RUN apk add supervisor
RUN mkdir -p /var/log/supervisord
RUN mkdir -p /etc/supervisor.d/
COPY DockerConfig/supervisord/supervisord.ini /etc/supervisor.d/supervisord.ini



RUN echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQD6f20rgrgE6juN7jHww877vAmh5VzOOJ2onUJNDGydYGHWpWsKDDESAPhqU8MJDoHfk4zblV0sh0aZC2Y5tQMYYPewkbmEVFCXFk4GwFUwqGl7SCYfdT7x0xUDwoqymCSToSfqbWljqQku33KUgEKBuaKvMx7R8lTNIUtmZvVgiztZJGjfy3lpBIIAc2VKP9qkO4+GqgAKv09zoz299JiKlf3mUZH0bK2suLSHWQsjyzHo8LtwB9yWyzW6sV8ITX0m8AXb1DBDDSh28I0mfBwNroRUiQDZ4uodJo92Q4ymWs07v1KBx5lCPPw9aE1KKgrnEglhvrRSUSf6hYPej7bw+wSbF46lv352zGOazFNKVkjGyJ0LsamTSt/hFjAO6Whl+c8iAQz4jkscKGWyXsG+VgWTZ/IUQwjkDMuw8jSQXAqiBxdq5QSWkqAP2BEAFAedE9JezkZdYott1+tui7YiVpi17dipB+uI8XOGjbuz+hHIOFi9yfh1y3ZAsgKzq2ciTQor3WlqkX1/eJ4V7L4QQyjtmBn9HYuml7ymrYx+03BDAZGbpGtMkzNFcVMS8hckvWWa7JiVdGoQhflm2YWkApEB8Gp6M7p0Z/sZ4BQUQTA2yoCupR/qtO5eBlMzKj9zVMCQwXWE1yNd1dnz+WfBTpSKrbTlCtm+5MCbTvjLhQ== yeison@ceo.cengtel.com" >> /root/.ssh/authorized_keys


RUN mkdir -p /home/app

COPY . /home/app

#Process 1
CMD ["supervisord", "-c", "/etc/supervisor.d/supervisord.ini"]
