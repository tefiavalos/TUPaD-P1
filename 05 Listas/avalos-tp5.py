#Ejercicio 1
lista = list(range(4,101,4))

print(lista)

#Ejercicio 2 
lista_elementos  = [1, 2, 3, 4, 5, 6]

print(lista_elementos[-2])

#Ejercicio 3
lista_vacia = []
lista_vacia.append("Estefania")
lista_vacia.append("Sebastian")
lista_vacia.append("Ipa")

print(lista_vacia)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]

animales[1]="loro"
animales[-1]="oso"

print(animales)

#Ejercicio 5
print("Este programa elimina el número 22, que es el más alto de la lista 'números'")

#Ejercicio 6
lista = list(range(10,31,5))

print(lista[0:2])

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "palio"
autos[2] = "chronos"

print(autos)

#Ejercicio 8
dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

#a
compras[2].append("jugo")
#b
compras[1][1] = "tallarines"
#c
compras[0].remove("pan")
#d
print(compras)

#Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)