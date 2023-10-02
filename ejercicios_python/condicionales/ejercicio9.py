#Ejercicio 9
#Escribir un programa para una empresa que tiene salas de juegos 
#para todas las edades y quiere calcular de forma automática el 
#precio que debe cobrar a sus clientes por entrar. El programa 
#debe preguntar al usuario la edad del cliente y mostrar el precio 
#de la entrada. Si el cliente es menor de 4 años puede entrar gratis,
#si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

usuario_edad = int(input("Introduce tu edad : "))

if usuario_edad <= 4:
    print("Tu entrada es gratis") 
elif usuario_edad < 18:
    print("Debes pargar 5€")
elif usuario_edad > 18:
    print("Dees pagar 10€")
else:
    usuario_edad = ""
