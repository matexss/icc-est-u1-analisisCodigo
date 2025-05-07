from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt

if __name__ == "__main__":

    print("Funciona")

    # Prueba básica de copia de listas
    a = [2, 4, 6]
    b = a.copy()
    print("a original:", a)
    print("b copia   :", b)
    b = b * 2
    print("a después :", a)
    print("b * 2     :", b)

    # Instanciar clases
    metodos = MetodosOrdenamiento()
    benchmarking = Benchmarking()

    # Tamaños de entrada a probar
    tamanios = [500, 1000, 2000]
    resultados = []

    # Diccionario con los métodos de ordenamiento
    metodosD = {
        "burbuja": metodos.sortByBubble,
        "seleccion": metodos.sortBySelection
    }

    # Ejecutar cada método con cada tamaño
    for tam in tamanios:
        arreglo_base = benchmarking.build_arreglo(tam)

        for nombre, metodo in metodosD.items():
            tiempo = benchmarking.medir_tiempo(metodo, arreglo_base)
            tuplaResultado = (tam, nombre, tiempo)
            resultados.append(tuplaResultado)

    # Mostrar resultados en consola
    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print(f"tamaño: {tam}, método:  {nombre}, tiempo: {tiempo:.6f} segundos")

    # Clasificar los tiempos según el método
    tiempos_by_metodo = {
        "burbuja": [],
        "seleccion": [],
    }

    # Clasificar los métodos según su nombre
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    # Crear una gráfica
    plt.figure(figsize=(10, 6))

    # Graficar una línea de tiempo para cada método
    # x = tamaño del arreglo, y = tiempo obtenido
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker='o')

    # Agregar parámetros visuales
    plt.title("Comparación de tiempos de ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True)
    plt.legend()  # Muestra qué color representa cada método
    plt.show()