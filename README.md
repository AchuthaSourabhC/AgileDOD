# AgileDOD
A Web to manage Agile Definition of Done for Agile sprints using Django and Docker

## Steps to build and run
```bash
docker-compose build
docker-compose up

```
## Creating super user
First log into the container. For this you need the continaer name
List the running container and use the nam give under NAMES column at the last
```bash
docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
376d2beac2b8        app_web             "bash -c 'python3 ..."   17 minutes ago      Up 6 minutes        0.0.0.0:8000->8000/tcp   app_web_1
30a22ec9894c        mysql               "docker-entrypoint..."   17 minutes ago      Up 6 minutes        0.0.0.0:3306->3306/tcp   app_mysql_1

```
Login to the continaer using the container name
```bash
docker exec -it app_web_1 bash
```
Once logged-in then run this command to create super user:
```bash
root@376d2beac2b8:/asm# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@mail.com
Password: **********
Password (again): **********
Superuser created successfully.

```
