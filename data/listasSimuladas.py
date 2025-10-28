#Rutina para simular un set de datos utilizando estructuras de python
#Utilizaremos Listas y diccionarios (MOCKS)

import random
from datetime import datetime, timedelta

def generar_ventas(numeroVentas):

    productos=[
        {"nombre":"Camiseta Polo", "precio":150000},
        {"nombre":"Pantalón", "precio":350000},
        {"nombre":"Jean ajustado", "precio":250000},
        {"nombre":"Camisa leñadora", "precio":200000},
        {"nombre":"Falda", "precio":120000}
    ]
    tallas=["S","M","L","XL","38","40","42"]
    vendedores=["Juan Pablo Gil","Raul Cossio","Carlos Franco","Anyi David","Juan Jose Gallego"]
    ventas=[]
    fechaInicio=datetime(2025,1,1)

    #Iterar segun el numero de ventas que me piden simular
    for _ in range(numeroVentas):
        producto =random.choice(productos)
        cantidad=random.randint(1,5)
        fecha=fechaInicio+timedelta(days=random.randint(0,90))
        ventas.append(
            {
                "fecha":fecha.strftime("%Y-%m-%d"),
                "producto":producto["nombre"],
                "precioUnitario":producto["precio"],
                "talla":random.choice(tallas),
                "cantidad":cantidad,
                "vendedor":random.choice(vendedores),
                "total":producto["precio"]*cantidad

            }
        )
    return(ventas)



