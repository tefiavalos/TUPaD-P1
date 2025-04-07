#Ejercicio1
edad_usuario = int(input('Ingresá tu edad: '))

if edad_usuario > 18:
  print("Sos mayor de edad")

#Ejercicio2
nota_usuario = int(input('Ingresá tu nota: '))

if nota_usuario >= 6:
  print("Aprobado")
else:
  print("Desaprobado")

#Ejercicio3
numero_usuario = int(input('Ingresá un número: '))

if numero_usuario % 2 == 0:
  print("Ha ingresado un número par")
else:
  print("Por favor, ingrese un número par")

#Ejercicio4
edad_usuario = int(input('Ingresá tu edad: '))

if edad_usuario < 12:
  print("Niño/a")
elif edad_usuario < 18:
  print("Adolescente")
elif edad_usuario < 30:
  print("Adulto joven")
else:
  print("Adulto")

#Ejercicio5
contraseña = len(input('Ingresá tu contraseña: '))

if contraseña >= 8 and contraseña <= 14:
  print("Contraseña correcta")
else:
  print("Debe tener entre 8 y 14 caracteres")

#Ejercicio6
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]  
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
  print("Sesgo positivo")
elif media < mediana and mediana < moda:
  print("Sesgo negativo")
elif media == moda == mediana:
  print("Sin sesgo")
else:
  pass

#Ejercicio7
frase = input("Ingresá la frase: ")

if frase[-1] == "a" or frase[-1] == "e" or frase[-1] == "i" or frase[-1] == "o" or frase[-1] == "u":
    print(frase + "!")
else:
    print(frase)

#Ejercicio8
nombre = input("Ingresá tu nombre: ")
opcion = int(input("Si querés tu nombre en mayúsculas ingresá 1, en minúsculas 2, Primera letra mayúscula 3: "))

if opcion == 1:
  print(nombre.upper())
elif opcion == 2:
  print(nombre.lower())
elif opcion == 3:
  print(nombre.title())
else:
  print("Opción inválida")

#Ejercicio9
magnitud_terremoto = int(input("Ingresá la magnitud del terremoto: "))
 
if magnitud_terremoto < 3:
  print("Muy leve")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
  print("Leve")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
  print("Moderado")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
  print("Fuerte")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
  print("Muy fuerte")
elif magnitud_terremoto >= 7:
  print("Extremo")
else:
  pass

#Ejercicio10
hemisphere = input("Ingresá tu hemisferio (N/S): ")
day = int(input("Ingresá el día de la fecha (1-31): "))
month = int(input("Ingresá  el mes de la fecha (1-12): "))

if hemisphere.upper() == "N":
    if  (day >= 21 and month == 12) or (month == 1 and month == 2) or (month == 3 and day <= 20):
        print("Invierno")
    elif (day >= 21 and month == 3) or (month > 3 and month < 6) or (month == 6 and day <= 20):
        print("Primavera")
    elif (day >= 21 and month == 6) or (month > 6 and month < 9) or (month == 9 and day <= 20):
        print("Verano")
    elif (day >= 21 and month == 9) or (month < 9 and month > 12) or (month == 12 and day <= 20):
        print("Otoño")
    else: print('Fecha inválida')
elif hemisphere.upper() == "S":
    if  (day >= 21 and month == 12) or (month == 1 and month == 2) or (month == 3 and day <= 20):
        print("Verano")
    elif (day >= 21 and month == 3) or (month > 3 and month < 6) or (month == 6 and day <= 20):
        print("Otoño")
    elif (day >= 21 and month == 6) or (month > 6 and month < 9) or (month == 9 and day <= 20):
        print("Invierno")
    elif (day >= 21 and month == 9) or (month < 9 and month > 12) or (month == 12 and day <= 20):
        print("Privamera")
    else: print('Fecha inválida')
else: print('Hemisferio inválido')

