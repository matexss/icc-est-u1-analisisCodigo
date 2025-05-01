import random
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    def __init__(self, tam=50000):
        print(f"Iniciando Benchmarking con {tam} elementos")
        self.arreglo = self.build_arreglo(tam)

    def ejemplo(self):
        self.mOrdenamiento = MetodosOrdenamiento()

        tarea1 = lambda: self.mOrdenamiento.sortByBubble(self.arreglo)
        tiempomilis = self.contar_con_current_time_milles(tarea1)
        tiemponano = self.contar_con_nano_time(tarea1)

        print(f"Tiempo en milisegundos (time.time): {tiempomilis:.3f} ms")
        print(f"Tiempo en segundos (perf_counter_ns): {tiemponano:.6f} s")

    def build_arreglo(self, size):    
        return [random.randint(0, 49999) for _ in range(size)]

    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()  
        tarea()
        fin = time.time()
        return (fin - inicio) * 1000.0  # milisegundos

    def contar_con_nano_time(self, tarea):
        inicio = time.perf_counter_ns()
        tarea()
        fin = time.perf_counter_ns()
        return (fin - inicio) / 1_000_000_000.0  # segundos

    def medir_tiempo(self, tarea, array):
        inicio = time.perf_counter()
        tarea(array)
        fin = time.perf_counter()
        return fin - inicio
