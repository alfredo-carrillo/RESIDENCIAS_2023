
#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola y un 
#número entero e imprima por pantalla en líneas distintas el nombre del usuario 
#tantas veces como el número introducido.

user_name = input("Escribe tu nombre porfavor: ")

n = int(input("\nIngresa cualquier numero en valor entero: "))


while n != 0:
     print(user_name)
     n = n - 1