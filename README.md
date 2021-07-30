# Examen1BIM-Analisis-Datos
Repositorio creado para el examen de Análisis de Datos

## 1) Twitter
  ###### a) Locations
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

  ###### a) Track
  - Las líneas que cambian para consultar por tendencias son las siguientes:
  
    -  **db = server.create('juegosolimpicostrack')**
    -  **twitterStream.filter(track=['juegos olimpicos','olimpiadas'])**
    
       Esta última es la que indica las palabras para basar la búsqueda
    ![image](https://user-images.githubusercontent.com/58191417/127721830-6c3a2c4f-962b-4dbc-847a-3b82b64496f0.png)

