#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

#tablas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

for x in range(1, 11):

    int(x)
    
    if x == x:
     print(f"\nLa tabla del {x} es:\n ")

     for tab in range(1, 11):
        result = x * int(tab)
        print(f" {x} x {tab} es: {result}")
    
