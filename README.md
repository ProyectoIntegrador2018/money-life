# PersonalDevelopment

Este proyecto es un videojuego de finanzas personales, el cual consiste en simular de una forma interactiva la vida de una persona con base en las desiciones economicas que se presenten, tratando de impitar las oportunidades que comunmente se presentan en la vida cotidiana de una persona de nivel socioeconimico medio. El juego tendra como variables eventos de tipio micro y macro, aparte de toma de deciciones en forma de inverciones, gastos personales y modificaciones de tu estado economico actual, todas estas variables tendran un efecto tanto positivo como negativo en tu ganancias y deudas diarias, aparte de evaluar el nivel de comodidad o felicidad con el cual cuenta tu personaje con las deciciones y eventos previos.

El juego comenzara con una persona estudiante de aproximadamente 18 años y se ira incrementando la edad con forme pase los turnos, cada turno sera lo equivalente a un periodo de 2 semanas o 1 mes, y en cada uno de estos sucederan los eventos y las deciociones previamente dichas. El juego terminara cuanto tus deciciones te ayan llevado a tener un estilo de vida feliz y economicamente autosustentable, o a los 65 años de edad, dando el juego como perdido en este punto.  

## Comenzando

Para poder correr el proyecto en tu maquina local, primeramente deberas colar el repositorio en tu disco local de la siguiente manera:

Repositorio de github: **https://github.com/ChristopherParga/PersonalDevelopment**

Para clonarlo en tu disco local:

`clone https://github.com/ChristopherParga/PersonalDevelopment.git`

## Pre-requisitos

Antes de correr este proyecto, deberas de tener instalado en tu computadora los siguientes frameworks

1. Angular CLI: 10.1.0
2. Django 3.1.1.
3. Pyhton 3.8.3
4. mySQL 8.0.9

## Instalación

#### Angular

Para instalar angular se necesitaran los siguientes comandos...

Primero necesitara instalar el intsalador de paquetes npm

`npm install install`

Despues deberas instalar angular CLI, lo que vendria siendo el manejado de paquetes de angular

`npm install -g @angular/cli`

Por ultimo, dentro del proyecto instalaras todos los paquetes con 

`npm install`

o

`ng install`

#### Django

Debes de contar con el instalador pip, el cual viene por dejecto en Mac y Linux

Despues para instalar Django se usa el siguiente comando

`sudo pip install django`

#### Python

Para instalar python es tan sencillo como poner el siguiente comando

`brew install python3`

#### MySql

Para instalar mySql solamente se requiere el siguiente comando

`brew install mysql`

## Validacion de instalacion

Para validar que se haya instalado de forma corecta, puedes desplegar la varcion con la que cuentas o poner a correr el servidor

#### Correr el servidor 

1. Angular: `ng s`
2. Django: `python manage.py runserver`
3. MySql: `brew services start mysql`

#### Ver verciones

1. Angular: `ng version`
2. Django: 
⋅⋅* `python`
⋅⋅* `import django`
⋅⋅* `django.VERSION`
1. Python: `python --version`
2. MySql: `mysql -v`

## Ejecutando pruebas de proyecto funcionando

Por el momento no se cuenta con ninguna prueba

## Documentacion

Para mas informacion de las herramientas utilizadas, puedes consultar las paginas oficiales de cada una de estas

###### Angular
[https://angular.io/docs]

###### Django
[https://docs.djangoproject.com/es/3.1/]

###### Python
[https://docs.python.org/es/3/]

###### Mysql
[https://dev.mysql.com/doc/]
