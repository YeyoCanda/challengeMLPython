CONSIDERACIONES:

DOCUMENTACION:

En la ruta MicroServicio\documentation se encuentran tres archivos, por favor tener en cuenta las siguientes observaciones:

1.) jsonEntrada.json - Este archivo contiene el json de entrada que necesita el metodo challenge para ser invocado la url es http://127.0.0.1:5000/challenge

2.) FileMLChallenge.postman_collection.json - Colección de postman para invocar los dos metodos implementados.

3.) openapi.yaml - Documentación del servicio realizada en swagger, se puede importar el archivo en el editor disponible en https://editor.swagger.io/

BASE DE DATOS:

Mi maquina no es personal, así que tengo algunas restricciones y no puedo actualizar algunos componentes del sistema operativo. En este caso, tuve problemas con la instalación de Docker, en la carpeta MicroServicio\db se encuentra la imagen del error y la configuración de la imagen que iba a utilizar (mysql). Por esta razón, decidí utilizar una base de datos Cosmos DB en Azure con la configuración de mongoDB, adjunto la imagen en la que se evidencia la persistencia desde el microservicio. El microservicio tiene una operación para limpiar la bd.

DESAFIO TEORICO:

Procesos, hilos y corrutinas 
•	Un caso en el que usarías procesos para resolver un problema y por qué. 
•	Un caso en el que usarías threads para resolver un problema y por qué. 
•	Un caso en el que usarías corrutinas para resolver un problema y por qué. 

Optimización de recursos del sistema operativo 
Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos información en una API HTTP. ¿Cómo lo harías? Explicar. 


Análisis de complejidad 
•	Dados 4 algoritmos A, B, C y D que cumplen la misma funcionalidad, con complejidades O(n 2 ), O(n 3 ), O(2 n ) y O(n log n), respectivamente, ¿Cuál de los algoritmos favorecerías y cuál descartarías en principio? Explicar por qué. 

•	Asume que dispones de dos bases de datos para utilizar en diferentes problemas a resolver. La primera llamada AlfaDB tiene una complejidad de O(1) en consulta y O(n 2 ) en escritura. La segunda llamada BetaDB que tiene una complejidad de O(log n) tanto para consulta, como para escritura. ¿Describe en forma sucinta, qué casos de uso podrías atacar con cada una?
