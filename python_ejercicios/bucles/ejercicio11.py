#Ejercicio 11
#Escribir un programa que pida al usuario una palabra y luego muestre por 
#pantalla una a una las letras de la palabra introducida empezando por la última.

w = input("Introduce una palabra : ")

w = w[::-1]

for i in w:
    print(i)
