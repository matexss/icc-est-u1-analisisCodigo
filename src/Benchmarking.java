import java.util.Random;

public class Benchmarking {
    MetodosOrdenamiento metodosOrdenamiento = new MetodosOrdenamiento();

    public Benchmarking() {
        // Constructor vacío o con inicialización opcional
    }

    public void tempo() {
        int[] arreglo = generarArregloAleatorio(10000); // menor tamaño para tiempos razonables

        Runnable tarea1 = () -> metodosOrdenamiento.burbujaTradicional(arreglo);
        Runnable tarea2 = () -> metodosOrdenamiento.seleccionPrimero(arreglo);
        Runnable tarea3 = () -> metodosOrdenamiento.insercionPrimero(arreglo);

        System.out.println("Benchmark:");
        System.out.println("Burbuja Tradicional: " + medirConNanoTime(tarea1) + " ms");
        System.out.println("Selección Primero:   " + medirConNanoTime(tarea2) + " ms");
        System.out.println("Inserción Primero:   " + medirConNanoTime(tarea3) + " ms");
    }

    public int[] generarArregloAleatorio(int i) {
        int[] arreglo = new int[i];
        Random random = new Random();
        for (int j = 0; j < i; j++) {
            arreglo[j] = random.nextInt(10000);
        }
        return arreglo;
    }

    public double medirConNanoTime(Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000.0;
    }

    public double medirConCurrenTime(Runnable tarea) {
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio) / 1000.0;
    }
}
