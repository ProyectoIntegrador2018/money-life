# Deployment
El despliegue completo de la aplicacion se realiza por separado backend y frontend con el uso de diferentes herramientas como vscode, github, docker, docker hub y azure. A continuacion se muestra el diagrama de deployment de la aplicacion:
![alt text](https://github.com/ProyectoIntegrador2018/money-life/blob/actualizacionarchivos/DeploymentDiagram.png)

## Como hacer deployment manual de los componentes. 
1.	Instalar VScode e instalar las siguientes extensiones, Azure Tools, Docker (tambien instalarlo en su equipo) y crear cuenta en docker hub.
1.	Instalar Nodejs para poder instalar angular:
    * Mediante el siguiente link: https://nodejs.org/en/download/
    * Al terminar la instalacion correr el siguiente comando en terminal:
    * npm install -g @angular/cli
1.	Instalar python 3.8:
    * Mediante el siguiente link: https://www.python.org/downloads/
1.	Instalar Docker:
    * Mediante el siguiente link: https://www.docker.com/products/docker-desktop
1.  Instalar MySQL:
    * Mediante el siguiente link: https://dev.mysql.com/downloads/installer/
    * Instalar (opcional) MySQL Workbench con el mismo instalador del paso pasado.
1.	Crear en Azure un servidor de base de datos de MySQL
1.  Conectar MySQL Workbench al servidor de azure utilizando los datos que te dados al crear el servidor.
1.  Comprobar conexion con el servidor de la base de datos y crear una base de datos llamada moneydb.
1.	Instalar las librerias requeridas de python en el documento requirements.txt.
1.	Crear/Tener cuenta en Azure
1.	Clonar el repositorio de github ubicado en https://github.com/ProyectoIntegrador2018/money-life/tree/v4.0
1.	Crear en Azure 1 web App services para el front.
1.	Abrir la carpeta de front en vscode.
1.	Iniciar sesion en Azure en vscode.
1.	Correr el siguiente comando para construir la aplicacion de frontend:
    * ng build --prod
    * Dar click derecho a la carpeta generada (usualmente dist/project-name/) y dar click en la opcion de deploy to web app en Azure.
1.	Para hacer el deployment del backend es necesario utilizar la estructura de proyecto mostrada en el branch backDocker del repositorio de github.
1.	Clonar la branch de dockerBack.
1.	Abrir la carpeta clonada del repositorio en vscode.
1.	En azure crear un nuevo servicio de contenedor blobs, con accesso publico.
1.	Crear la carpeta de static y media en el servicio. 
1.	Iniciar sesion en docker hub en vscode. 
1.	Construir el contenedor de la aplicacion con el siguiente comando:
    * docker-compose --build
1.	Teniendo la imagen creada, por default se llama django_app dar click derecho en el contenedor en la extension de vscode de Docker y dar click el push para subirlo a su cuenta de Docker Hub.
1.	En Azure crear un nuevo web App service para el back, seleccionando la opcion de imagen de docker como ambiente.
1.  Enlazar la ubicacion del contenedor en docker con el servidor de azure y dar click en crear imagen.  
1.	Esperar unos minutos en lo que se crea el servidor y se hace el deployment del contenedor en azure..
1.	Al estar terminado puede hacer uso de la aplicacion.
