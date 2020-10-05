# Configuración de login

##### Angular

Para instalar angular se necesitarán los siguientes comandos...

Primero necesitara instalar el instalador de paquetes npm

`npm install install`

Después deberás instalar angular CLI, lo que vendría siendo el manejado de paquetes de angular

`npm install -g @angular/cli`

Por ultimo, dentro del proyecto instalaras todos los paquetes con 

`npm install`

o

`ng install`

##### Django

Debes de contar con el instalador pip, el cual viene por defecto en Mac y Linux

Después para instalar Django se usa el siguiente comando

`sudo pip install django`

##### Python

Para instalar python es tan sencillo como poner el siguiente comando

`brew install python3`

##### MySql

Para instalar mySql solamente se requiere el siguiente comando

`brew install mysql`

### Ejecutar herramientas para desarrollo

Para validar que se haya instalado de forma correcta, puedes desplegar la versión con la que cuentas o poner a correr el servidor

###### Validar versiones

1. Angular: `ng version`
2. Django: 
⋅⋅* `python`
⋅⋅* `import django`
⋅⋅* `django.VERSION`
1. Python: `python --version`
2. MySql: `mysql -v`

###### Correr el servidor 

1. Angular: `ng s`
2. Django: `python manage.py runserver`
3. MySql: `brew services start mysql`

Ingresar a la siguiente liga http://127.0.0.1:8000/admin/login/?next=/admin/ 

Usuario: user
Contraeña: user