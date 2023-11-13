#Ejercicio 6
#Escribir un programa que pida al usuario que introduzca una frase 
#en la consola y una vocal, y después muestre por pantalla la misma 
#frase pero con la vocal introducida en mayúscula.

frase = input("Intruduce cualquier frase a procesar: ")
vocal = input("Introduzca la vocal a convertir en mayuscula")


print(frase.replace(vocal, vocal.upper()))
