#Traer un registro de N ventas para analizar con pandas
#Primeros pasos con pandas

from data.listasSimuladas import generar_ventas
from notebook.graficarBarras import generarBarra
from notebook.generarReportes import crearTabla
import pandas as pd

datos_simulados=generar_ventas(1000)

#Organizando la fuente de datos con pandas
tablaOrdenada=pd.DataFrame(datos_simulados)

#1. Obtener la informacion general de la fuente de datos
#print(tablaOrdenada.info())

#2. Obtener la informacion estadistica basica (descriptiva) de la fuente de datos
#print(tablaOrdenada.describe())

#3. Obtener la informacion de los primeros N registros de la fuente de datos
#print(tablaOrdenada.head(20))

#4. Obtener la informacion de los ultimos N registros de la fuente de datos
#print(tablaOrdenada.tail(20))

#5. Acceder a una columna (Seleccionar) en especifico
#print(tablaOrdenada["vendedor"])

#6. Acceder a varias columnas al mismo tiempo
#print(tablaOrdenada[["vendedor", "producto", "total"]])

#7. PUEDO APLICAR AGRUPACIONES (AGRUPAR DATOS NUMERICOS Y STRING)
#print(tablaOrdenada.groupby("producto")["total"].sum())
#print(tablaOrdenada.groupby("vendedor")["total"].sum())
#print(tablaOrdenada.groupby("fecha")["total"].sum().head(31))


##################################################################################
#TRANSFORMANDO DATOS CON PANDAS 
#APLICANDO FILTROS O DATA QUERIES

#PROFE
#Yo puedo obtener de los datos las ventas realizadas en enero de 2025?
queryUno=tablaOrdenada.query("fecha >= '2025-01-01' and fecha <= '2025-01-31' ")
crearTabla(queryUno,"reportes/tablaUno.html","Ventas de enero",200)

#Yo como adminsitrador del PV puedo ver la cantidad mayor o iguales 3?
queryDos=tablaOrdenada.query("cantidad >= 3")
#Yo como administrador del PV puedo ver cuales fueron las ventas del producto JEAN AJUSTADO
queryTres=tablaOrdenada.query("producto == 'Jean ajustado' ")
#Yo puedo puedo obtener las ventas de tallas M O L
tallasFiltradas=['M','L']
queryCuatro=tablaOrdenada.query("talla.isin(@tallasFiltradas)")
#Yo como lider de bodega puedo acceder a los productos cuyo preciounitario  entre los 150k y 300k
queryCinco=tablaOrdenada.query("precioUnitario >=150000 and precioUnitario<= 300000")
#Yo puedo ver las ventas que hizo Juan Jose Gallego
querySeis=tablaOrdenada.query("vendedor == 'Juan Jose Gallego' ")
#Yo puedo obtener las ventas de los fines de semana
#Cree una columna con el numero del dia de la semana Lunes=0, Domingo=6
tablaOrdenada["fecha"]=pd.to_datetime(tablaOrdenada["fecha"])
tablaOrdenada["dia_semana"]=tablaOrdenada["fecha"].dt.day_of_week
queriSiete=tablaOrdenada.query("dia_semana == 5 and dia_semana == 6")
#Yo puedo ver ventas cuyo total sea mayor a 1Millon
queryOcho=tablaOrdenada.query("total > 1000000 ")
#Yo quiero ver todas las ventas de todos los prductos excluyendo las faldas
queryNueve=tablaOrdenada.query("producto!='Falda'")
#yo puedo ver las ventas entre dos fechas especificas
queryDiez=tablaOrdenada.query("fecha >= '2025-01-01' and fecha <= '2025-01-31' ")


#=========================== YO ==========================

#yO QUIERO VER VENTAS CON CANTIDAD >3 Y TOTAL >600K
queryOnce = tablaOrdenada.query("cantidad > 3 and total > 600000")
crearTabla(queryOnce, "reportes/tablaDos.html", "Ventas con cantidad >3 y total >600K", 200)
#VENTAS DE PRODUCTOS QUE CONTENGAN LA PALABRA CAMISA
queryDoce = tablaOrdenada.query("producto == 'Camiseta Polo'")
#VENTAS DE VENDEDORES CUYO NOMBRE CONTIENE LA PALABRA JUAN
queryTrece = tablaOrdenada.query("vendedor == 'Juan Pablo Gil'")
#OBTENER LAS VENTAS CON PRECIO UNITARIO MAYOR AL PROMEDIO GENERAL
queryCatorce = tablaOrdenada.query("precioUnitario > @tablaOrdenada['precioUnitario'].mean()")
#OBTENER LAS VENTAS CON TOTAL MAYOR AL DOBLE DEL PRECIO UNITARIO
queryQuince = tablaOrdenada.query("total > 2 * precioUnitario")
#VENTAS DE TALLAS NUEMRICAS 
queryDieciseis = tablaOrdenada.query("talla in ['38','40','42']")
#VENTAS DE PANTALON O JEAN AJUSTADO CON CANTIDAD >= 2
queryDiecisiete = tablaOrdenada.query("(producto == 'Pantalón' or producto == 'Jean ajustado') and cantidad >= 2")
#VENTAS >400K Y TALLA NO NUMERICA
queryDieciocho = tablaOrdenada.query("total > 400000 and talla not in ['38','40','42']")
crearTabla(queryDieciocho, "reportes/tablaTres.html", "Ventas >400K y talla no numerica", 200)
#VENTAS DE TODOS MENOS LAS DE RAUL
queryDiecinueve = tablaOrdenada.query("vendedor != 'Raul Cossio'")
#VENTAS ORDENADAS POR TOTAL DESCENDENTE
queryVeinte = tablaOrdenada.sort_values(by="total", ascending=False)
crearTabla(queryVeinte, "reportes/tablaCuatro.html", "Ventas ordenadas por total descendente", 200)



#GRAFICAS A GENERAR
#total de ventas por producto
generarBarra(tablaOrdenada,"producto","total","Ventas totales por producto")
#total de ventas con cantidad >=3
filtroUno=tablaOrdenada.query("cantidad >= 3")
generarBarra(filtroUno,"producto","total","Ventas > 3 productos")
#total de ventas por vendedor
generarBarra(tablaOrdenada,"vendedor","total","Desempeño de vendedores en la tienda san diego")


# ========================= YO ======================

#total de ventas de productos caros (>400k)
filtroDos = tablaOrdenada[tablaOrdenada['total'] > 400000  ]
generarBarra(filtroDos, "producto", "total", "Ventas de productos caros (>400k)")
#GRAFICAR LAS VENTAS DE ENERO
tablaOrdenada['fecha'] = pd.to_datetime(tablaOrdenada['fecha'])
filtroTres = tablaOrdenada[tablaOrdenada['fecha'].dt.month == 1]
generarBarra(filtroTres, "producto", "total", "Ventas de enero")
#GRAFICAR LAS VENTAS DE JEANS AJUSTADOS POR VENDEDOR
filtroCuatro = tablaOrdenada[tablaOrdenada['producto'] == 'Jean ajustado']
generarBarra(filtroCuatro, "vendedor", "total", "Ventas de Jeans ajustados por vendedor")
#UNIDADES VENDIDADAS DE TALLA XL
filtroCinco = tablaOrdenada[tablaOrdenada['talla'] == 'XL']
generarBarra(filtroCinco, "producto", "cantidad", "Unidades vendidas de talla XL")
#PROPONEME UNA GRAFICA 
#GRAFICAR LAS VENTAS DE FALDA DEL MES FEBRERO y sus vendedores
filtroSeis = tablaOrdenada[(tablaOrdenada['producto'] == 'Falda') & (tablaOrdenada['fecha'].dt.month == 2)]
generarBarra(filtroSeis, "vendedor", "total", "Ventas de faldas en febrero por vendedor")
