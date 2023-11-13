#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.


n = int(input("Ingresa un numero entero: "))


acum = ""

for i in range(1, n+1):  
  if i % 2 == 1: 
    acum += str(i)
    print(acum[::-1])