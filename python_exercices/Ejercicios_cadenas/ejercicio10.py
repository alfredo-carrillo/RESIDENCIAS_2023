#Ejercicio 10
#Escribir un programa que pregunte por consola por los productos 
#de una cesta de la compra, separados por comas, y muestre por 
#pantalla cada uno de los productos en una línea distinta.
import re



cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')

cesta = re.sub("\ |","",cesta)
print(cesta.replace(',', '\n'))
