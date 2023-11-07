#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

n = int(input("Ingresa un numero entero"))
acum = ""
for x in range(0, n):
    acum += str(n)
    print(acum)