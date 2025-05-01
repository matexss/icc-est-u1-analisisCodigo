import benchmarking as Ben
import metodos_ordenamiento as MetO

# Ejecutar benchmark
if __name__ == "__main__":
    print("Funciona")

    benchmark = Ben.Benchmarking()
    metodos_ordenamiento = MetO.MetodosOrdenamiento()

    tam = 10000
    arreglo_base = benchmark.build_arreglo(tam)

    # Diccionario llamado metodos con 2 claves: burbuja y seleccion
    metodos = {
        "burbuja": metodos_ordenamiento.sortByBubble,
        "seleccion": metodos_ordenamiento.sortBySelection
    }

    resultados = []
    for nombre, metodo in metodos.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
        tuplaresultados=(tam,nombre,tiempo)
        resultados.append(tuplaresultados)
    
    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print(f"Tiempo de {nombre} para {tam} elementos: {tiempo:.6f} segundos")