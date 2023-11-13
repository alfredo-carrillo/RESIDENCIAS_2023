#Ejercicio 10
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

n = int(input("ingresa un numero entero por favor:  "))


if n%n == 0:
  print(f" {n} es numero primo")
  
else:
    print(f" {n} no es numero primo")
   

#for x in range(1, n+1):
#    
#    primos = x%x  ##queda pendiente este 
#
# if x == x%x==0:
#     print(x)
#