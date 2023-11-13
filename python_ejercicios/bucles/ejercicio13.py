#Ejercicio 13
#Escribir un programa que muestre el eco de todo lo que el 
#usuario introduzca hasta que el usuario escriba “salir” que terminará

eco = input("Introduce mensaje a imprimir en bucle: ------>  ")

while eco != "salir":
        print(eco)
        eco = input("Introduce mensaje a imprimir en bucle: ------>  ")