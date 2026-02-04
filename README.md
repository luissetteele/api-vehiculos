# Despliegue de API REST con Jinja2 y PostgreSQL en Render

## 1. Añadir páginas web con Jinja2 a la API REST

En esta práctica se amplía la API REST desarrollada previamente incorporando páginas web renderizadas mediante **Jinja2**.

Para ello:

* Se crean plantillas HTML dentro del directorio `templates/`.
* Se configura el framework (por ejemplo Flask o FastAPI) para renderizar vistas con Jinja2.
* Se conectan las rutas web con los datos obtenidos desde la base de datos.

El objetivo es poder acceder a la información tanto mediante endpoints REST como mediante páginas web tradicionales.

---

## 2. Base de datos MySQL usando Docker Compose

Inicialmente, la aplicación utiliza **MySQL** como sistema gestor de bases de datos, levantado mediante **Docker Compose**.

Características principales:

* Servicio MySQL definido en `docker-compose.yml`.
* Variables de entorno para usuario, contraseña y base de datos.
* La API se conecta al contenedor MySQL usando la red interna de Docker.

Esto permite un entorno de desarrollo reproducible y aislado.

---

## 3. Migración de MySQL a PostgreSQL

Posteriormente, se sustituye MySQL por **PostgreSQL** como base de datos.

Cambios realizados:

* Sustitución del servicio MySQL por PostgreSQL en `docker-compose.yml`.
* Instalación del driver correspondiente (`psycopg2` o `asyncpg`).
* Adaptación de la cadena de conexión en el archivo `db.py`.

El objetivo es asegurar que la aplicación funcione correctamente usando PostgreSQL en local.

---

## 4. Despliegue de PostgreSQL en Render

Una vez verificado el funcionamiento local, se despliega la aplicación en la nube usando **Render**.

Pasos seguidos:

1. Subida del proyecto al repositorio Git.
2. Creación de una base de datos PostgreSQL desde el panel de Render.
3. Creación del servicio web enlazado al repositorio.
4. Definición de variables de entorno necesarias (URL de conexión a la base de datos).

Todo el proceso de despliegue queda documentado en este fichero Markdown.

---

## 5. Modificación del archivo `db.py`

Para que la aplicación funcione correctamente en Render, es necesario modificar el archivo `db.py`.

Se debe cambiar la línea de conexión a la base de datos para que lea la **URL desde una variable de entorno**, en lugar de usar valores fijos.

Esto permite que Render inyecte automáticamente la cadena de conexión proporcionada por su servicio PostgreSQL.

---

## 6. Error al conectar Git con Render

Al enlazar el repositorio Git con Render, se produce un error inicial debido a que la aplicación no encontraba correctamente la cadena de conexión a la base de datos.

El problema se debía a:

* Una línea incorrecta o incompleta en `db.py`.
* No se estaba leyendo la variable de entorno definida en Render.

---

## 7. Corrección del error en `db.py`

Una vez corregida la línea en `db.py` para que leyera la **URL desde la variable de entorno creada en Render con el mismo nombre**, la aplicación se despliega sin problemas.

Tras la corrección:

* El servicio se construye correctamente.
* La aplicación arranca sin errores.
* La conexión con PostgreSQL en la nube funciona correctamente.

---

## 8. Comprobación de acceso a la base de datos en Render

Una vez dentro del panel de Render, se comprueba que:

* La base de datos PostgreSQL está activa.
* La aplicación puede conectarse correctamente.
* Los endpoints y páginas web funcionan como se espera.

Esto confirma que el despliegue se ha realizado con éxito y que la API es completamente funcional en la nube.

---

## 9. Conclusión

Con esta práctica se ha conseguido:

* Integrar Jinja2 en una API REST.
* Migrar de MySQL a PostgreSQL.
* Desplegar una aplicación completa en Render.
* Utilizar variables de entorno para una configuración segura y flexible.

El proyecto queda preparado para un entorno de producción real.
