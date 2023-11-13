#Ejercicio 8
#Escribir un programa que pregunte por consola el precio de un 
#producto en euros con dos decimales y muestre por pantalla el 
#número de euros y el número de céntimos del precio introducido.

precio = input("Introduce el precio del producto, por favor usa dos decimales por ejemplo 3.35€ ------->  ")
dot ="."
index = precio.index(dot)

#data = precio[index:]

euro_ent = precio[:index]
euro_deci = precio[index+1:]

print("Los euros del producto son : ", euro_ent+"€")
print("Los centavos del producto son: ", euro_deci+"¢")
