# 💻📱 systemERP


Em breve descrição...



![React](https://img.shields.io/badge/React-18-blue?logo=react) 
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript) 
![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)  
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)


Este projeto foi desenvolvido com ***React + JavaScript + Django + Docker*** como parte do meu aprendizado prático para reforçar conceitos essenciais de desenvolvimento front-end com React, back-end com Django (API REST), persistência de dados com **MySQL** e boas práticas em automação e deploy com Docker.



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



## 💢 Troubleshoot Zone

1. Verifique se tem algum serviço utilizando a porta padrão do Django se tiver utilize outra porta no "runserver":
    ```bash 
        PS C:\Users\klaus\systemERP\backend\api> netstat -aon | findstr :8000
        TCP    127.0.0.1:8000         0.0.0.0:0              LISTENING       40132

        PS C:\Users\klaus\systemERP\backend\api> tasklist | findstr 40132
        Code.exe                     40132 Console                    2    106.364 K


2. Deletar todas as tabelas do MYSQL para evitar conflito migrate do Django:
    ```bash 
        mysql> USE systemerp;

        mysql> SHOW DATABASES;

        mysql> SET FOREIGN_KEY_CHECKS = 0;    

        mysql> DROP TABLE auth_group_permissions;
        mysql> DROP TABLE auth_group;
        mysql> DROP TABLE auth_permission;
        mysql> DROP TABLE auth_user_groups;
        mysql> DROP TABLE auth_user_user_permissions;
        mysql> DROP TABLE auth_user;
        mysql> DROP TABLE django_admin_log;
        mysql> DROP TABLE django_content_type;
        mysql> DROP TABLE django_migrations;
        mysql> DROP TABLE django_session;
       
        SET FOREIGN_KEY_CHECKS = 1;


## ⛏️ Como foi criado o projeto do zero

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

        PS C:\Users\klaus\systemERP\backend\api> pip install django-cors-headers

        PS C:\Users\klaus\systemERP\backend\api> pip install djangorestframework-simplejwt



4. Inicar projeto Django:
    ```bash
        PS C:\Users\klaus\systemERP\backend\api> django-admin startproject erp .

        PS C:\Users\klaus\systemERP\backend\api> django-admin startapp accounts

        PS C:\Users\klaus\systemERP\backend\api> django-admin startapp companies            

        PS C:\Users\klaus\systemERP\backend\api> python manage.py makemigrations

        PS C:\Users\klaus\systemERP\backend\api> python manage.py migrate

        PS C:\Users\klaus\systemERP\backend\api> python manage.py runserver 8080




## 📋 Documentação da API - Authentication

#### Autenticação - Criar Um Conta

```http
  POST /api/v1/auth/signup
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `name` | `string` | **Obrigatório** |
| `email` | `string` | **Obrigatório** |
| `password` | `string` | **Obrigatório** |

#### Autenticação - Fazer Login

```http
  POST /api/v1/auth/signin
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `email` | `string` | **Obrigatório** |
| `password` | `string` | **Obrigatório** |

#### Autenticação - Obter Um Usuário - (_Necessário Autenticação_)

```http
  GET /api/v1/auth/user
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Authorization` | `string` | **Obrigatório**. Access Token |


## 📋 Documentação da API - Companies - Employees

#### Funcionários - Listar Funcionários De  Uma Empresa - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/employees
```

#### Funcionários - Criar Um Funcionário - (_Necessário Autenticação_)

```http
  POST /api/v1/companies/employees
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `name` | `string` | **Obrigatório** |
| `email` | `string` | **Obrigatório** |
| `password` | `string` | **Obrigatório** |

#### Funcionários - Obter Um Funcionário - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/employees/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de um funcionário |

#### Funcionários - Editar Um Funcionário - (_Necessário Autenticação_)

```http
  PUT /api/v1/companies/employees/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de um funcionário |
| `groups` | `string` | **Opcional**. String com uma lista de ids de diversos grupos |
| `name` | `string` | **Opcional** |
| `email` | `string` | **Opcional** |

#### Funcionários - Deletar Um Funcionário - (_Necessário Autenticação_)

```http
  DELETE /api/v1/companies/employees/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de um funcionário |

## 📋 Documentação da API - Companies - Groups / Permissions

#### Grupos / Cargos - Gupos De Uma Empresa - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/groups
```

#### Grupos / Cargos - Criar Um Grupo - (_Necessário Autenticação_)

```http
  POST /api/v1/companies/groups
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- | 
| `name` | `string` | **Obrigatório** | 
| `permissions` | `string` | **Obrigatório**. String com uma lista de ids de diversas permissões |

#### Grupos / Cargos -  Obter Um Grupo - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/groups/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- | 
| `id` | `number` | **Obrigatório**. ID de um grupo |

#### Grupos / Cargos - Editar Um Grupo - (_Necessário Autenticação_)

```http
  PUT /api/v1/companies/groups/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de um grupo |
| `name` | `string` | **Opcional** | 
| `permissions` | `string` | **Opcional**. String com uma lista de ids de diversas permissões |

#### Grupos / Cargos - Deletar Um Grupo - (_Necessário Autenticação_)

```http
  DELETE /api/v1/companies/groups/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de um grupo |

#### Permissões - Permissões Disponíveis - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/permissions
```

## 📋 Documentação da API - Companies - Tasks

#### Tarefas - Tarefas De Uma Empresa - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/tasks
```

#### Tarefas - Criar Um Tarefa - (_Necessário Autenticação_)

```http
  POST /api/v1/companies/tasks
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- | 
| `employee_id` | `number` | **Obrigatório**. ID de um funcionário | 
| `status_id` | `number` | **Obrigatório**. ID de um status de tarefa |
| `title` | `string` | **Obrigatório** |
| `description` | `string` | **Opcional** |
| `due_date` | `date` | **Opcional**. Data no formato: d/m/Y H:M |

#### Tarefas - Obter Uma Tarefa - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/tasks/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de uma tarefa |

#### Tarefas - Editar Um Tarefa - (_Necessário Autenticação_)

```http
  PUT /api/v1/companies/tasks/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de uma tarefa |
| `employee_id` | `number` | **Opcional**. ID de um funcionário | 
| `status_id` | `number` | **Opcional**. ID de um status de tarefa |
| `title` | `string` | **Opcional** |
| `description` | `string` | **Opcional** |
| `due_date` | `date` | **Opcional**. Data no formato: d/m/Y H:M |

#### Tarefas - Deletar Uma Tarefa - (_Necessário Autenticação_)

```http
  DELETE /api/v1/companies/tasks/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de uma tarefa |




## ✍️ Autor

Desenvolvido com 💙 por **[Klaus Christian Kurth](https://github.com/KlausKurth)**  
📧 klausckurth@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/klaus-christian-kurth-soares-039937164/) 


📚 Referências:
    - [Documentação oficial do Django](https://www.djangoproject.com/download/)
    - [Django REST Framework](https://www.django-rest-framework.org/)
    - [Django cors headers](https://pypi.org/project/django-cors-headers/)
    - [Simple JSON Web Token)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)