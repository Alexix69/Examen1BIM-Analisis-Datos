# Examen1BIM-Analisis-Datos
Repositorio creado para el examen de Análisis de Datos

## a) Twitter
  ###### 1) Locations
  - Importamos las librerías necesarias, en este caso Tweepy
  
  ![image](https://user-images.githubusercontent.com/58191417/127720919-659b02ab-6aa7-4a75-8ff1-08ae1cf24f10.png)
  
  - Es importante establecer las keys proporcionadas por Twitter para cosechar los datos
  
  ![image](https://user-images.githubusercontent.com/58191417/127720735-95a6da2a-9ad8-4329-b206-f40f0453685f.png)
  
  - La clase listener hace uso de los métodos que tiene tweepy para generar el json, se da el "id" y se evalúa si este ya está ingresado en la BD. 
  - Todo esto dentro de un try-except por si se presenta alguna excepcion.
  
  ![image](https://user-images.githubusercontent.com/58191417/127720950-8364c177-cc51-476b-843a-540ca2333f0f.png)
  
  - Se pasa las credenciales a los métodos validadores
  
  ![image](https://user-images.githubusercontent.com/58191417/127721044-122bae3a-879e-4fcd-b356-5422baa332a6.png)
  
  - Esta es la parte que cambiara dentro del código conforme a las consultas que se haga, en este caso se genera un BD para cada ciudad:
    - Nagoya
    - Nagano
    - New York
  - Ya que se busca por localizaciones, es necesario cambiar las coordenadas provistas por Bounding Box para cada ciudad en la línea **twitterStream.filter(locations=[137.910101,36.460702,138.318899,36.835734])**
   
  ![image](https://user-images.githubusercontent.com/58191417/127721086-fa8a2037-8951-476b-bd42-9c7956b5e4f4.png)
  
  **-> Comprobamos en la interfaz de Fauxton la creación de una BD por cada ciudad <-**
  ![image](https://user-images.githubusercontent.com/58191417/127721610-b8730920-71a2-4a7d-b415-2258edda00b4.png)

  ###### 2) Track
  - Las líneas que cambian para consultar por tendencias son las siguientes:
  
    -  **db = server.create('juegosolimpicostrack')**
    -  **twitterStream.filter(track=['juegos olimpicos','olimpiadas'])**
    
       Esta última es la que indica las palabras para basar la búsqueda
    ![image](https://user-images.githubusercontent.com/58191417/127721830-6c3a2c4f-962b-4dbc-847a-3b82b64496f0.png)

## b) TikTok

  Para tiktok-scraper es necesario ejecutar los comandos:
  
   - Iniciará el scraper mediante npm
   
   **npm i -g tiktok-scraper**
  
  - Hecho esto basta ejecutar el comando con los parametros siguientes para que nos genere un CSV:

  Usuario 1: **tiktok-scraper user stamkkk -t csv**
  
   ![image](https://user-images.githubusercontent.com/58191417/127723791-fa78aeb3-1623-4f02-a9df-1d7ad53d14b8.png)

  Usuario 2: **tiktok-scraper user dannapaola -t csv**
  
  ![image](https://user-images.githubusercontent.com/58191417/127723799-bed0bef6-23c3-4d78-9bde-e6cb5fdfb65c.png)
  
  Para importar el CSV a MySQL verificamos los pasos:
  
  ![image](https://user-images.githubusercontent.com/58191417/127723817-c9370ae0-b59f-46c4-a84b-14c1ec0d7b40.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723822-67755cdf-44e6-4ec4-9563-9b238c4d49d1.png) 
  
  ![image](https://user-images.githubusercontent.com/58191417/127723828-3877d95e-6dd4-44da-8489-9c66c18b9a54.png)

  Comprobamos que la BD se haya insertar de manera correcta (por la extensión de la misma, solo se adjuntan capturas que comprueben el hecho)
  
  ![image](https://user-images.githubusercontent.com/58191417/127723855-b0076644-5b7b-498a-9cc9-09e419f06941.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723859-bfe04f9f-8cb8-4462-baf6-60ee16ad3534.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723863-d5f270fc-1040-45d8-8a86-52a69f89ae2d.png)

  ###### Mismo proceso para el otro usuario:
  
  ![image](https://user-images.githubusercontent.com/58191417/127723874-9c72810a-5026-4941-a83d-7fe2691922dd.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723877-8c22e9eb-1b54-4c7c-8093-06ecd0dd6119.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723881-8ab70164-2585-4e90-9e90-a266808dbed5.png)

  Comprobamos:
  
  ![image](https://user-images.githubusercontent.com/58191417/127723892-a2f71e6d-f919-4f84-b48a-08c3e4077864.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723897-869d0652-5cdc-493e-a939-bed49523b494.png)

  ![image](https://user-images.githubusercontent.com/58191417/127723905-0a854b54-f6a1-4c41-b58a-48383d509835.png)

  
