Prueba tecnica para Bookline.Ai 

Estre proyecto consta de una API dockerizada realizada en FastAPI. 
Esta estructurada en una estructura por capas, aplicando arquitecturas DDD
Cuenta también con un sistema de logging por archivos.

La API tiene dos endpoints, un GET de coches disponibles a servervar en una fecha en especifico, y un POST para realizar la reserva sobre un coche deseado. Estos datos se almacenan de manera local empleando un archivo JSON. 

Los endpoints son los siguientes: 
    
    - /api/v1/cars/available
        Tipo: GET 
        Toma: Parametro por query specified_date de tipo DATETIME.DATE
        Devuelve: 
            - 200 : Lista de coches disponibles en esa fecha, sus nombres y fechas reservadas (no disponibles) 

    - /api/v1/cars/book_a_car
        Tipo: POST 
        Toma: 
            - Parametro por query booking_date de tipo DATETIME.DATE
            - Parametro por query car_name de tipo string
        Devuelve: 
            - 200 : Mensaje de confirmacion de reserva
            - 400 : Mensaje indicando imposibilidad de realización de reserva

El puerto para acceder a la API es: 8888
Y la URL para la documentacion: /api/docs
