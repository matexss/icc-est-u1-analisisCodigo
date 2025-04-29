import java.util.Random;

public class Benchmarking {

    private MetodosOrdenamiento metodos = new MetodosOrdenamiento();

    public void tempo() {
        int[] arreglo = generarArregloAleatorio(1000000); 

        // Medir tiempo con burbujaTradicional
        Runnable tareaBurbuja = () -> metodos.burbujaTradicional(arreglo);

        double tiempo = medirConNanoTime(tareaBurbuja);
        System.out.println("Tiempo en segundos: " + tiempo);
    }

    private int[] generarArregloAleatorio(int tamaño) {
        Random random = new Random();
        int[] arreglo = new int[tamaño];
        for (int i = 0; i < tamaño; i++) {
            arreglo[i] = random.nextInt(10000);
        }
        return arreglo;
    }

    public double medirConNanoTime(Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }
}
