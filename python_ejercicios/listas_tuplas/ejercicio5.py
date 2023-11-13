#Ejercicio 5#
#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados# por comas5

num = []
for x in range(1, 10+1):
    str(x)
    num.append(x)


    #num =",".join(num[::-1])
print(num[::-1])

