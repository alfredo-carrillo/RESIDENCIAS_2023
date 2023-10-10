#Ejercicio 8
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo

palabra = input("Ingresa una palabra averificar: ")

if palabra == palabra[::-1]:
    print("es palindromo")
else:
    print("no es palindromo")

   #
   # if palabra[x] == palabra[::-1]:
   #    print(f"La palabra { palabra } es un palindromo y el resultado es", palabra[x] )