#Ejercicio 3
#Escribir un programa que pida al usuario dos 
#números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.

print("programa para realizar uns division entre dos numeros....")

num1 = float(input("ingresa el divisor "))
num2 = float(input("ingresa el dividendo "))

if num1 == 0 or num2 == 0:
    print("err it cannot be an 0 operation ")
else:
    result = num1/num2

    print("el resultado es : ", result)