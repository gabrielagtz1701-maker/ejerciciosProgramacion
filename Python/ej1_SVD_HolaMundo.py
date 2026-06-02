# #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
#### Dificultad: Fácil | Publicación: 26/12/23 | Corrección: 02/01/24

## Ejercicio

'''
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
'''
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

'''
Sitio oficial Python
https://www.python.org/
'''

# Comentario de una sola linea
'''
Comentario de varias lineas
Sin problemas
'''

# Variable
variable = "Python"

# Constante, Python no tiene constantes, pero se suele utilizar mayusculas 
CONSTANTE = 3.1416

# Tipos de datos primitivos (variables)
my_int = 43 # Entero, no tiene decimales
my_float = 3.14 # Flotante, tiene decimales
my_bool_True = True # Booleano, verdadero
my_bool_False = False # Booleano, false
my_string = "Cadena de texto con comillas dobles"
my_other_string = 'Cadena de texto con comillas simples'

# Imprimir por terminal
print ("Hola Pyhton!") # Imprimir texto
print("Hola " +  variable + "!") # Concatenacion
print(f"Hola {variable}!") # Formateado

# Imprimir tipo de texto
print(type(my_int))
print(type(my_float))
print(type(my_bool_True))
print(type(my_bool_False))
print(type(my_string))
print(type(my_other_string))


