#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña 
#en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "contraseña"
password = input("Ingrese la contraseña porfavor: ")

while password  != contraseña :

    password = input("\nContraseña incorrecta, por favor introduzcala de nuevo: ")

    if password == contraseña:
        print("\nContraseña exitosa, hasta pronto")
