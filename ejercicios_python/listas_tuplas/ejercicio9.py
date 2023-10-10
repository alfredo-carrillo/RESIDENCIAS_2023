#Ejercicio 9
#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

w = input("ingresa la palabra: ")

a, e, i, o, u = 0, 0, 0, 0, 0

vocales = ['a', 'e', 'i', 'o', 'u']

#print(vocales[0])
for x in range(len(w)):
 
    if w[x] == vocales[0]:
        a += 1
    if w[x] == vocales[1]:
        e += 1
    if w[x] == vocales[2]:
        i += 1
    if w[x] == vocales[3]:
        o += 1
    if w[x] == vocales[4]:
        u += 1
   

print(f" a = {a}\n e = {e}\n i = {i}\n o = {o}\n u = {u} ")