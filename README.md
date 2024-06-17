## Social Network

[[_TOC_]]

---

:scroll: **START**


### Introduction

Social networks have transformed the way we communicate, advertise and lead our lives during the past 2 decades.
Many of us have one or multiple profiles on one or several networks, and we use them on a daily basis to communicate and share information.

---

### Task description

We are tasked with developing a small social network, where **users** can _create_ their profiles, make _friends_ or _follow_ each other.
They are able to create **posts**, which could be _public_ (visible to their friends and followers), or _private_ (only visible to their friends).

The users that can see a post, have also the option to _like_ (or _unlike_ if they've liked it before).
A single user can only like a single post once (they can like as many posts as they like, but each individual only once).

Finally, all users can request to see their wall, which is a list of all the posts created by themselves, their friends, and the public posts of the people they follow.

The **user** has:
- fullName: the user's full name

The **posts** have:
- text: A string value, representing the contents of the post
- visibility: can be either **public** or **private**

Develop a set of REST service APIs based on the swagger file provided - [swagger file](social-network-swagger.yaml), that allows users to:
- Users can create their profiles (`POST /users`)
- They can make friends or follow other users (`POST /users/{user1Id}/{friends|followers}/{user2Id}`)
- For the follower relationship, the second passed userId becomes a follower of the first passed userId (user1Id <-isFollowedBy- user2Id)
- They can create posts, that are public or private (`POST /posts`)
- Request to see their wall, which contains all posts that are visible to them, sorted by latest to earliest (from the creation time descending) (`GET /walls/{userId}`)

You can open the swagger file using a tool like [Swagger Editor](https://editor.swagger.io/), which provides a good visual representation of the methods needed, their format, sample requests and responses.

### Requirements

While implementing your solution **please take care of the following requirements**:

#### Functional requirements

- The REST API methods should be implemented based on the specification provided in the linked swagger file;
- Add 2 new API methods (they're not defined in the swagger file) that enable a user to like a post, and unlike a post they've already liked. When returning the list of posts in the `/walls` method, add a new attribute to each post returned, containing the number of likes it has;
- There is no need for UI.

#### Non-functional requirements

- The project must be buildable and runnable;
- The project must have Unit tests;
- The project must have a README file with build/run/test instructions (use a DB that can be run locally, e.g. in-memory, via container);
- Any data required by the application to run (e.g. reference tables, dummy data) must be preloaded in the database;
- Input/output data must be in JSON format;
- Use a framework of your choice, but popular, up-to-date, and long-term support versions are recommended.

---
:scroll: **END**

## Social Network

# Social Network

[[TOC]]

:scroll: **START**

## Introducción

Las redes sociales han transformado la manera en que nos comunicamos, publicitamos y llevamos nuestras vidas durante las últimas dos décadas. Muchos de nosotros tenemos uno o varios perfiles en una o varias redes, y las usamos a diario para comunicarnos y compartir información.

---

## Descripción de la Tarea

Se nos ha encomendado desarrollar una pequeña red social, donde **usuarios** puedan _crear_ sus perfiles, hacerse _amigos_ o _seguirse_ entre ellos. Pueden crear **posts**, que pueden ser _públicos_ (visibles para sus amigos y seguidores), o _privados_ (solo visibles para sus amigos).

Los usuarios que pueden ver una publicación, también tienen la opción de _darle like_ (o _quitarle el like_ si ya lo han hecho antes). Un solo usuario solo puede dar like a una publicación una vez (pueden dar like a tantas publicaciones como deseen, pero cada una solo una vez).

Finalmente, todos los usuarios pueden solicitar ver su muro, que es una lista de todas las publicaciones creadas por ellos mismos, sus amigos, y las publicaciones públicas de las personas que siguen.

El **usuario** tiene:
- **fullName**: el nombre completo del usuario

Las **publicaciones** tienen:
- **text**: Un valor de cadena, que representa el contenido de la publicación
- **visibility**: puede ser **public** o **private**

Desarrolla un conjunto de API de servicios REST basadas en el archivo swagger proporcionado - [archivo swagger](social-network-swagger.yaml), que permita a los usuarios:
- Crear sus perfiles (`POST /users`)
- Hacer amigos o seguir a otros usuarios (`POST /users/{user1Id}/{friends|followers}/{user2Id}`)
  - Para la relación de seguidor, el segundo userId pasado se convierte en seguidor del primer userId pasado (user1Id <-isFollowedBy- user2Id)
- Crear publicaciones, que son públicas o privadas (`POST /posts`)
- Solicitar ver su muro, que contiene todas las publicaciones que son visibles para ellos, ordenadas de la más reciente a la más antigua (desde la hora de creación descendente) (`GET /walls/{userId}`)

Puedes abrir el archivo swagger usando una herramienta como [Swagger Editor](https://editor.swagger.io/), que proporciona una buena representación visual de los métodos necesarios, su formato, solicitudes y respuestas de ejemplo.

---

## Requisitos

### Requisitos funcionales

- Los métodos de la API REST deben implementarse basándose en la especificación proporcionada en el archivo swagger enlazado;
- Agregar 2 nuevos métodos de API (no están definidos en el archivo swagger) que permitan a un usuario darle like a una publicación, y quitarle el like a una publicación que ya le han dado like. Al devolver la lista de publicaciones en el método `/walls`, agrega un nuevo atributo a cada publicación devuelta, que contenga el número de likes que tiene;
- No es necesario una interfaz de usuario.

### Requisitos no funcionales

- El proyecto debe ser construible y ejecutable;
- El proyecto debe tener pruebas unitarias;
- El proyecto debe tener un archivo README con instrucciones de compilación/ejecución/prueba (usa una base de datos que se pueda ejecutar localmente, por ejemplo, en memoria, vía contenedor);
- Cualquier dato requerido por la aplicación para ejecutarse (por ejemplo, tablas de referencia, datos de prueba) debe precargarse en la base de datos;
- Los datos de entrada/salida deben estar en formato JSON;
- Usa un framework de tu elección, pero se recomiendan versiones populares, actualizadas y con soporte a largo plazo.

---

:scroll: **END**

---

## Abordaje General del Proyecto en FastAPI

### 1. Estructura del Proyecto

- **Directorio del Proyecto**: Organiza tu proyecto con carpetas claras para el código de la aplicación, configuraciones, modelos, controladores, y pruebas.

### 2. Configuración de FastAPI

- **Inicializa la Aplicación**: Configura la aplicación principal de FastAPI en un archivo principal (por ejemplo, `main.py`).
- **Configuración de la Base de Datos**: Define y configura la conexión a la base de datos, utilizando un ORM como SQLAlchemy o una base de datos NoSQL como MongoDB.

### 3. Definición de Modelos

- **Modelos Pydantic**: Define los modelos de datos utilizando Pydantic para validación de datos y esquemas de solicitudes y respuestas.
- **Modelos de Base de Datos**: Define los modelos de base de datos utilizando un ORM o directamente con la base de datos de tu elección.

### 4. Creación de Endpoints

- **Usuarios**: Define los endpoints para la creación de usuarios, gestión de amigos y seguidores.
- **Publicaciones**: Define los endpoints para la creación de publicaciones, gestión de visibilidad, y obtención del muro de publicaciones.
- **Likes**: Define los endpoints adicionales para dar like y quitar like a publicaciones.

### 5. Manejo de Errores y Excepciones

- **Errores Comunes**: Implementa manejo de errores para solicitudes inválidas, errores del servidor y otros casos de error comunes.
- **Respuestas Personalizadas**: Configura respuestas de error personalizadas usando HTTPException de FastAPI.

### 6. Pruebas Unitarias

- **Configuración de Pruebas**: Configura un entorno de pruebas usando pytest o cualquier otro framework de pruebas.
- **Pruebas de Endpoints**: Implementa pruebas unitarias para todos los endpoints asegurando que las funcionalidades cumplen con los requisitos.

### 7. Documentación y README

- **Documentación Swagger**: Asegúrate de que la documentación generada automáticamente por FastAPI esté actualizada.
- **Archivo README**: Proporciona instrucciones claras en el README sobre cómo construir, ejecutar y probar la aplicación.

### 8. Pre-carga de Datos

- **Datos Iniciales**: Asegúrate de que la base de datos esté pre-cargada con datos necesarios para la operación básica de la aplicación.
  
### 9. Despliegue

- **Configuración del Entorno**: Prepara un entorno de despliegue, ya sea en la nube (AWS, GCP, Azure) o en un servidor local.
- **Dockerización**: Considera crear un contenedor Docker para tu aplicación para facilitar el despliegue y la escalabilidad.
- **Configuración CI/CD**: Configura pipelines de integración y entrega continua para automatizar pruebas, construcciones y despliegues.

---

## Detalles Adicionales

### Seguridad

- **Autenticación y Autorización**: Implementa mecanismos de autenticación (por ejemplo, JWT) y autorización para proteger los endpoints sensibles.
- **Protección de Datos**: Asegúrate de que los datos sensibles estén encriptados y de que la aplicación cumpla con las normativas de protección de datos aplicables.

### Optimización y Escalabilidad

- **Optimización de Consultas**: Optimiza las consultas a la base de datos para mejorar el rendimiento.
- **Escalabilidad Horizontal**: Considera estrategias de escalabilidad horizontal, como balanceo de carga y microservicios, para manejar el aumento de usuarios y datos.

### Monitoreo y Logging

- **Monitoreo de Aplicaciones**: Implementa herramientas de monitoreo para rastrear el rendimiento y la salud de la aplicación.
- **Logging**: Configura un sistema de logging eficiente para registrar y analizar errores y eventos importantes.

---

### Recursos y Herramientas

- **Swagger Editor**: Utiliza [Swagger Editor](https://editor.swagger.io/) para visualizar y editar el archivo de especificación de la API.
- **FastAPI Documentation**: Consulta la [documentación oficial de FastAPI](https://fastapi.tiangolo.com/) para obtener guías y referencias.
- **Base de Datos**: Considera el uso de bases de datos relacionales como PostgreSQL o MySQL, o bases de datos NoSQL como MongoDB, dependiendo de los requisitos específicos de tu aplicación.

### Enlaces Útiles

- [Swagger Editor](https://editor.swagger.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [pytest Documentation](https://docs.pytest.org/en/stable/)

---

:scroll: **END**