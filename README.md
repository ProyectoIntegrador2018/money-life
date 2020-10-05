# Nombre del proyecto

Money Life (Sitio Web)

## Introducción

Este proyecto es un videojuego de finanzas personales, el cual consiste en simular de una forma interactiva la vida de una persona con base en las decisiones económicas que se presenten, tratando de imitar las oportunidades que comúnmente se presentan en la vida cotidiana de una persona de nivel socioeconómico medio. El juego tendrá como variables eventos de tipio micro y macro, aparte de toma de decisiones en forma de inversiones, gastos personales y modificaciones de tu estado económico actual, todas estas variables tendrán un efecto tanto positivo como negativo en tu ganancias y deudas diarias, aparte de evaluar el nivel de comodidad o felicidad con el cual cuenta tu personaje con las decisiones y eventos previos.

El juego comenzará con una persona estudiante de aproximadamente 18 años y se ira incrementando la edad con forme pase los turnos, cada turno será lo equivalente a un periodo de 2 semanas o 1 mes, y en cada uno de estos sucederán los eventos y las decisiones previamente dichas. El juego terminara cuanto tus decisiones te hayan llevado a tener un estilo de vida feliz y económicamente autosustentable, o a los 65 años, dando el juego como perdido en este punto.


## Tabla de contenidos

* [Detalle de Cliente](#client-details)
* [Ambiente URLS](#environment-urls)
* [Miembros del equipo](#team-members)
* [Tecnología utilizada](#technology-stack)
* [Recursos de gestión](#management-resources)
* [Configuración del proyecto](#setup-the-project)
* [Ejecutar herramientas para desarrollo](#running-the-stack-for-development)
* [Detener el proyecto](#stop-the-project)
* [Restaurar Base de Datos](#restoring-the-database)
* [Debugging](#debugging)
* [Ejecución de especificaciones](#running-specs)
* [Checar código de posibles riesgos](#checking-code-for-potential-issues)

### Detalle de Cliente

| Nombre                          | Email                | Rol                                                                               |
| ------------------------------ | -------------------- | ---------------------------------------------------------------------------------- |
| Rubén Manuel Aguilar Marroquín | ruben.aguilar@tec.mx | Profesor de finanzas ITESM Campus Mty. |

### Ambiente URLS

[localhost](http://localhost:3000/) 

### Miembros del equipo

Versión 1.0
| Nombre                              | Email                   | Rol                              |
| --------------------------------- | ----------------------- | --------------------------------- |
|Rodrigo Valencia Maciel            | A00818256@itesm.mx      | Desarrollador                     |
|Rodrigo Esparza Giacomelli         | A00819564@itesm.mx      | Desarrollador                     |
|Christopher David Parga Jaramillo  | A00818942@itesm.mx      | Desarrollador                     |


### Tecnológia utilizada


| Tecnológia      | Versión      |
| --------------- | ------------ |
| Angular CLI     | 10.1.0       |
| Django          | 3.1.1        |
| Pyhton          | 3.8.3        |
| mySQL           | 8.0.9        |


### Recursos de gestión

Debes solicitar acceso para acceder a estos recursos

[Github repo](https://github.com/ChristopherParga/PersonalDevelopment)

[Trello](https://trello.com/b/qKyp3rHZ/personal-development)

[Drive](https://drive.google.com/drive/folders/1tLua2-ePArqoOsd-bFwI_NKb_JG6Xsz8?usp=sharing)

## Desarrollo

### Configuración del proyecto

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

###### Correr el servidor 

1. Angular: `ng s`
2. Django: `python manage.py runserver`
3. MySql: `brew services start mysql`

###### Ver versiones

1. Angular: `ng version`
2. Django: 
⋅⋅* `python`
⋅⋅* `import django`
⋅⋅* `django.VERSION`
1. Python: `python --version`
2. MySql: `mysql -v`

### Documentación

Para mas información de las herramientas utilizadas, puedes consultar las paginas oficiales de cada una de estas

###### Angular
https://angular.io/docs

###### Django
https://docs.djangoproject.com/es/3.1/

###### Python
https://docs.python.org/es/3/

###### Mysql
https://dev.mysql.com/doc/



