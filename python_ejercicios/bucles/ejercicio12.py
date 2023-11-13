#Ejercicio 12
#Escribir un programa en el que se pregunte al usuario por una 
#frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase

w = input("ingresa una palabra: ")
l = input("Igresa una letra: ")

#count = w.count(l)
#
#print(count)
#
    
counter = 0
for x in w :
    if x == l:
        counter += 1
print(f"la letra [{l}] aparecio {counter} veces")