# Microservicio Usuarios

Microservicio desarrollado en python y desplegado en Azure Functions para la aplicacion web RestBit. Este microservicio se encarga de administrar la creacion, la actualizacion y la recuperacion de la informacion de los usuarios administradores de los restaurantes. Ademas es clave para el proceso de manejo de sesiones y login.

##### URL: 'https://microservicio-usuarios.azurewebsites.net/api

# Funciones

#### method = POST | endpoint: /httptrigger1'

Json request body:

{  

    "id_restaurante": int,  
    "password": string,  
    
}

#### method = PUT | endpoint: /httptrigger2'

Json request body:

{  

    'old_password': string,
    'new_password': string,
    'id_restaurante': int
  
}

#### method = GET | endpoint: /httptrigger3'

Json request body:

{  

    "id_restaurante": int
    'password': string,
        
}
