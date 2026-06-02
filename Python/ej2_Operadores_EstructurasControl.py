'''
 EJERCICIO:
      - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
        Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
        (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
      - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
        que representen todos los tipos de estructuras de control que existan
        en tu lenguaje:
        Condicionales, iterativas, excepciones...
      - Debes hacer print por consola del resultado de todos los ejemplos.

      DIFICULTAD EXTRA (opcional):
      Crea un programa que imprima por consola todos los números comprendidos
      entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

      Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
     
'''

# Operadores aritméticos
a = 10
b = 3
print("Suma:", a + b)          # 13
print("Resta:", a - b)         # 7
print("Multiplicación:", a * b) # 30
print("División:", a / b)      # 3.333...
print("División entera:", a // b) # 3
print("Módulo:", a % b)        # 1
print("Potencia:", a ** b)     # 1000

# Operadores de comparación
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Operadores lógicos
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Operadores de asignación
c = 5
print("c inicial:", c)
c += 2
print("c += 2:", c)
c -= 1
print("c -= 1:", c)
c *= 3
print("c *= 3:", c)
c //= 2
print("c //= 2:", c)
c %= 3
print("c %= 3:", c)

# Operadores de identidad
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]
print("lista1 is lista2:", lista1 is lista2)   # True
print("lista1 is lista3:", lista1 is lista3)   # False (objetos distintos)
print("lista1 is not lista3:", lista1 is not lista3)

# Operadores de pertenencia
print("2 in lista1:", 2 in lista1)
print("4 not in lista1:", 4 not in lista1)

# Operadores a nivel de bits
m = 6   # 110
n = 3   # 011
print("m & n:", m & n)   # AND -> 010 -> 2
print("m | n:", m | n)   # OR  -> 111 -> 7
print("m ^ n:", m ^ n)   # XOR -> 101 -> 5
print("~m:", ~m)         # NOT -> -7 (complemento a dos)
print("m << 1:", m << 1) # desplaza a la izquierda -> 12
print("m >> 1:", m >> 1) # desplaza a la derecha -> 3

# Condicionales
edad = 20
if edad < 18:
    print("Menor de edad")
elif 18 <= edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")

# Bucles: while
i = 0
while i < 3:
    print("while i:", i)
    i += 1

# Bucles: for
for j in range(3):
    print("for j:", j)

# Uso de break y continue
for k in range(5):
    if k == 2:
        continue
    if k == 4:
        break
    print("k en for con continue/break:", k)

# Excepciones
try:
    num = int("10")
    print("Conversión correcta:", num)
    num2 = int("hola")  # esto lanza ValueError
    print("Esto no se imprime")
except ValueError as e:
    print("Ocurrió un ValueError:", e)
finally:
    print("Bloque finally ejecutado")


print("Números válidos (Python):")
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num, end=" ")
print()  # salto de línea
