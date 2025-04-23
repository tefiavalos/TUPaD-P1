# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
   print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene

numero = str(int(float(input("Ingresá un número entero: "))))
contador = 0

for digito in numero:
    contador += 1

print(f"{numero} tiene {contador} dígitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero_uno = int(float(input("Ingresá un número entero: "))) + 1
numero_dos = int(float(input("Ingresá otro número entero: ")))
suma = 0

for i in range(numero_uno, numero_dos):
    suma += i

print(suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero = int(float(input("Ingresá un número entero: ")))
suma = 0

while numero != 0:
    suma += numero
    numero = int(float(input("Ingresá otro número entero: ")))
    
print(suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número

numero_usuario = int(float(input("Ingresá un número entero: ")))
NUMERO = 8
contador = 1

while numero_usuario != NUMERO:
    numero_usuario = int(float(input("No es correcto. Tenés otra oportunidad: ")))
    contador += 1

print(f"Felicitaciones, necesitaste {contador} intentos para lograrlo.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, 0 - 1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(float(input("Ingresá un número entero: ")))
suma = 0

for i in range(0, numero + 1):
    suma += i

print(suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

for i in range(0, 100):
    numero = int(float(input("Ingresá el número entero: ")))

    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

    if numero > 0:
        contador_positivos += 1
    else:
        contador_negativos += 1


print(f"Hay {contador_pares} números pares, {contador_impares} impares, {contador_negativos} números negativos y {contador_positivos} positivos")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

CANTIDAD_NUMEROS = 100
suma = 0

for i in range(0, CANTIDAD_NUMEROS):
    numero = int(float(input("Ingresá el número entero: ")))
    suma+=numero

print(f"El promedio de tus números es {suma / CANTIDAD_NUMEROS}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745


numero = input("Ingresá el número entero: ")
numero_invertido = ""

for i in numero:
    numero_invertido = i + numero_invertido

print(f"Tu número invertido es: {numero_invertido}")