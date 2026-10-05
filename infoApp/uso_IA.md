El historial es parte de la evidencia.
Registro de consultas (prompt, respuesta, adaptacion) mas explicacion del proceso escrita con sus propias palabras, sin IA.

prompt json: crea un arcivho json con 4 registros de articulos computacionales con precio.

Para este proyecto, yo utilicé. la IA, en.......
Se genera archivo json con uso de IA: Claro. Aquí tienes un archivo JSON válido con 30 productos de farmacia, incluyendo nombre, laboratorio, precio y requiere_receta.

1. Json sin precios

*** modificar el formato para loaddata (versión fixture)
*** adaptar la estructura y los campos de un archivo de datos
*** modificar el views.py que carga los datos json

2. Crear el models
3. Crear el admin
4. Crear las migraciones
    python manage.py makemigrations
    python manage.py migrate

*** python manage.py loaddata serviciosApp/datos.json
Carga datos desde un archivo JSON hacia la base de datos de Django

5. Comprobar que Django reconoce los modelos
    python manage.py check
6. Crear los datos en Django Admin
    Usuario administrador: python manage.py createsuperuser
        Username (leave blank to use 'sistemas'): pancho
        Email address: pancho@pancho.cl
        Password

7. En Admin Django
    SERVICIOS APP
        Servicios
        Precios servicios
*** Para idioma en el Admin setting.py 
    LANGUAGE_CODE = 'es'
    TIME_ZONE = 'America/Santiago'

8. Agregar un Servicio y Precios
9. Hacer que la página Precios muestre ese registro desde la base de datos.
10. Agregar el modelo a views.py y cambiar def precios (request)

