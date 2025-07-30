# systemERP
Em breve descrição...


![React](https://img.shields.io/badge/React-18-blue?logo=react) 
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript) 
![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)  
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)


Este projeto foi desenvolvido com ***React + JavaScript + Django + Docker*** como parte do meu aprendizado prático para reforçar conceitos essenciais de desenvolvimento front-end com React, back-end com Django (API REST), persistência de dados com **MySQL** e boas práticas em automação e deploy com Docker.


## Como funciona o systemERP?
Em breve descrição...


## 📸 Capturas de Tela
![Tela inicial](./screenshots/home_page.png)


## 🚀 Tecnologias utilizadas

- ⚛️ React (com Vite)

- 🟨 JavaScript (ES6+)

- 💅 CSS Modules para estilização

- 📦 Vite como bundler

- 🌐 Django como API backend

- 🐬 MySQL como base de dados

- 🐳 Docker para automação e ambiente de desenvolvimento




1. Crie um container MYSQL em seu DockerDesktop:
     ```bash
        PS C:\Users\klaus> docker run --name mysql -e MYSQL_ROOT_PASSWORD=#Welcome1988 -d -p 3306:3306 mysql:latest
        
        PS C:\Users\klaus> docker ps --all
        CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                         NAMES
        5d481f337ac4   mysql:latest   "docker-entrypoint.s…"   33 seconds ago   Up 24 seconds   0.0.0.0:3306->3306/tcp, [::]:3306->3306/tcp   mysql
        
        PS C:\Users\klaus\systemERP> docker exec -it mysql bash
        
        bash-5.1# mysql -u root -p'#Welcome1988' 
        mysql: [Warning] Using a password on the command line interface can be insecure.
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 9
        Server version: 9.4.0 MySQL Community Server - GPL

        Copyright (c) 2000, 2025, Oracle and/or its affiliates.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql>

        mysql> SHOW DATABASES;
        +--------------------+
        | Database           |
        +--------------------+
        | information_schema |
        | mysql              |
        | performance_schema |
        | sys                |
        +--------------------+
        4 rows in set (0.093 sec)
        






## Troubleshoot Zone
1. Verifique se tem algum serviço utilizando a porta padrão do Django se tiver utilize outra porta no "runserver":
    ```bash 
        PS C:\Users\klaus\systemERP\backend\api> netstat -aon | findstr :8000
        TCP    127.0.0.1:8000         0.0.0.0:0              LISTENING       40132

        PS C:\Users\klaus\systemERP\backend\api> tasklist | findstr 40132
        Code.exe                     40132 Console                    2    106.364 K


## Como foi criado o projeto do zero
1. Configurações MYSQL:
     ```bash
        PS C:\Users\klaus> docker run --name mysql -e MYSQL_ROOT_PASSWORD=#Welcome1988 -d -p 3306:3306 mysql:latest
        
        PS C:\Users\klaus> docker ps --all
        CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                         NAMES
        5d481f337ac4   mysql:latest   "docker-entrypoint.s…"   33 seconds ago   Up 24 seconds   0.0.0.0:3306->3306/tcp, [::]:3306->3306/tcp   mysql
        
        PS C:\Users\klaus\systemERP> docker exec -it mysql bash
        
        bash-5.1# mysql -u root -p'#Welcome1988' 
        mysql: [Warning] Using a password on the command line interface can be insecure.
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 9
        Server version: 9.4.0 MySQL Community Server - GPL

        Copyright (c) 2000, 2025, Oracle and/or its affiliates.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql>

        mysql> SHOW DATABASES;
        +--------------------+
        | Database           |
        +--------------------+
        | information_schema |
        | mysql              |
        | performance_schema |
        | sys                |
        +--------------------+
        4 rows in set (0.093 sec)

        mysql> CREATE DATABASE systemerp;
        Query OK, 1 row affected (0.047 sec)

        mysql> SHOW TABLES;
        +----------------------------+
        | Tables_in_systemerp        |
        +----------------------------+
        | auth_group                 |
        | auth_group_permissions     |
        | auth_permission            |
        | auth_user                  |
        | auth_user_groups           |
        | auth_user_user_permissions |
        | django_admin_log           |
        | django_content_type        |
        | django_migrations          |
        | django_session             |
        +----------------------------+
        10 rows in set (0.005 sec)




2. Configure o ambiente virtual Python:
    ```bash
        PS C:\Users\klaus\systemERP> python -m venv systemerp

        PS C:\Users\klaus\systemERP> systemerp\Scripts\activate

        PS C:\Users\klaus\systemERP> deactivate



3. Pendências Python PIP:
    ```bash
        PS C:\Users\klaus\systemERP\backend\api> python -m pip install Django==5.2.4

        PS C:\Users\klaus\systemERP\backend\api> pip install djangorestframework

        PS C:\Users\klaus\systemERP\backend\api> pip install markdown

        PS C:\Users\klaus\systemERP\backend\api> pip install django-filter

        PS C:\Users\klaus\systemERP\backend\api> pip install mysqlclient


4. Inicar projeto Django:
        PS C:\Users\klaus\systemERP\backend\api> django-admin startproject erp .

        PS C:\Users\klaus\systemERP\backend\api> python manage.py migrate

        PS C:\Users\klaus\systemERP\backend\api> python manage.py makemigrations

        PS C:\Users\klaus\systemERP\backend\api> python manage.py runserver 8080













## ✍️ Autor

Desenvolvido com 💙 por **[Klaus Christian Kurth](https://github.com/KlausKurth)**  
📧 klausckurth@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/klaus-christian-kurth-soares-039937164/) 


📚 Referências:
    - [Documentação oficial do Django](https://www.djangoproject.com/download/)
    - [Django REST Framework](https://www.django-rest-framework.org/)