public class ej1_SVD_HolaMundo {

    /*
    00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
    Dificultad: Fácil | Publicación: 26/12/23 | Corrección: 02/01/24

    Ejercicio

      ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
      - Recuerda que todas las instrucciones de participación están en el
        repositorio de GitHub.

      Lo primero... ¿Ya has elegido un lenguaje?
      - No todos son iguales, pero sus fundamentos suelen ser comunes.
      - Este primer reto te servirá para familiarizarte con la forma de participar
        enviando tus propias soluciones.

      EJERCICIO:
      - Crea un comentario en el código y coloca la URL del sitio web oficial del
        lenguaje de programación que has seleccionado.
      - Representa las diferentes sintaxis que existen de crear comentarios
        en el lenguaje (en una línea, varias...).
      - Crea una variable (y una constante si el lenguaje lo soporta).
      - Crea variables representando todos los tipos de datos primitivos
        del lenguaje (cadenas de texto, enteros, booleanos...).
      - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

      ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
      debemos comenzar por el principio.

     Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.
      */

    public static void main(String[] args) {
        /*
        Sitio oficial Java
        https://www.oracle.com/java/
         */

        // Comentario de una sola liena
        /*
        Comentario de varias lineas
        Sin problemas
         */

        // Variable
        String variable = "Java";

        // Constante
        final double PI = 3.1416;

        // Tipos de datos primitivos
        byte b = 1;
        short s = 2;
        int entero = 10;
        long largo = 1000L;
        float decimal = 3.14f;
        double grande = 2.78955;
        char letra = 'A';
        boolean booleano = true;

        // Imprimir por terminal
        System.out.println("Hola Java");
        System.out.println("Hola " + variable);
        System.out.println(String.format("Hola %s", variable));
    }

}
