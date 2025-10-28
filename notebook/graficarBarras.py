import matplotlib.pyplot as plt

def generarBarra(tablaOrdenada, columnaX, columnaY, titulo):

    colores=[
        "#8258C7",
        "#58C783",
        "#80C758",
        "#C7C758",
        "#C7585A"
    ]

    agrupacionDatos=tablaOrdenada.groupby(columnaX)[columnaY].sum()
    plt.figure(figsize=(10,5))
    plt.bar(agrupacionDatos.index,agrupacionDatos.values,color=colores)
    plt.title(titulo)
    plt.xlabel(columnaX)
    plt.ylabel(columnaY)
    plt.show()