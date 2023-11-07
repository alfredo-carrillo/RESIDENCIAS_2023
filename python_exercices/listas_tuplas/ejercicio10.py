#Ejercicio 10
#Escribir un programa que almacene en una lista los siguientes precios, 
#50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios = [50, 75, 46, 22, 80, 65, 8]
precios.sort()

print(f"el precio menor es : {precios[0]}\n y el precio mayor es: {precios[-1]}")


