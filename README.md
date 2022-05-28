# Unidad 3 - Topicos especiales Telematica ST0263

# Laboratorio 5 - Big data

1. Se inicia el Laboratorio en AWS y se hace la creacion de un Cluster EMR con una previamente descargada clave .pem para la posterior conexion por medio de SSH
<img width="1070" alt="Screen Shot 2022-05-28 at 7 38 50 AM" src="https://user-images.githubusercontent.com/68828858/170825886-3d142994-faa7-4a1e-a152-0610ad9ebfe9.png">
<img width="1074" alt="Screen Shot 2022-05-28 at 7 39 06 AM" src="https://user-images.githubusercontent.com/68828858/170825887-388242ff-dc71-4ab0-ae4e-4a2397bd412a.png">

2. Creamos los busckets para el almacenamiento de los datasets cumpliendo con el orden del mismo se inicializa /raw
   ### URL:  https://https://jflopezgdatalake.s3.amazonaws.com/raw/datasets/
   
<img width="988" alt="Screen Shot 2022-05-28 at 7 41 55 AM" src="https://user-images.githubusercontent.com/68828858/170825981-e2c48434-d22e-41cd-b325-82a7481eb961.png">
<img width="942" alt="Screen Shot 2022-05-28 at 7 42 54 AM" src="https://user-images.githubusercontent.com/68828858/170826005-061e23f2-15fd-49ed-90ce-5921987520cd.png">

3. Configuramos nuestras inbound rules para el acceso a los aplicativos 

Importante adicionalmente abrir el puerto 22 para la conexion por SSH al cluster en consola

<img width="1125" alt="Screen Shot 2022-05-28 at 7 41 18 AM" src="https://user-images.githubusercontent.com/68828858/170826070-2209a5ab-7bad-4ccc-89cb-4374b2014f8f.png">

4. Copiamos las credenciales y ya tendremos acceso en consola al cluster EMR

<img width="1052" alt="Screen Shot 2022-05-28 at 7 41 02 AM" src="https://user-images.githubusercontent.com/68828858/170826160-ab4ca4e6-36c2-413e-9939-16b98ad18e77.png">

5. Con la consola EMR se puede acceder al HUE por medio del comando y tener acceso a los archivos ademas te la interaccion con los buckets y todas las acciones de listado, creacion, borrado etc:

<img width="942" alt="Screen Shot 2022-05-28 at 7 51 05 AM" src="https://user-images.githubusercontent.com/68828858/170826295-0faea707-a06f-4d82-a6f5-c12b9616eace.png">
<img width="955" alt="Screen Shot 2022-05-28 at 7 51 20 AM" src="https://user-images.githubusercontent.com/68828858/170826302-04f5b1c4-a9bc-4b2f-b4f7-78c20c8011f5.png">
<img width="951" alt="Screen Shot 2022-05-28 at 7 51 33 AM" src="https://user-images.githubusercontent.com/68828858/170826307-4959b070-1493-4409-a2f4-795ead187760.png">
