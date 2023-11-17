
import math

def calculadora_cientifica():
    
    valor = int(input("Introduce un valor entero: "))
    funcion = input("Selecciona una función (seno, coseno, tangente, exponencial, logaritmo): ")


    print("\nTabla:")
    print("{:<10} {:<15}".format("Entero", funcion.capitalize()))

    # Calcular y mostrar resultados para cada entero de 1 al valor introducido
    for i in range(1, valor + 1):
        resultado = None

        if funcion == "seno":
            resultado = math.sin(i)
        elif funcion == "coseno":
            resultado = math.cos(i)
        elif funcion == "tangente":
            resultado = math.tan(i)
        elif funcion == "exponencial":
            resultado = math.exp(i)
        elif funcion == "logaritmo":
            resultado = math.log(i)

        # Mostrar el resultado en la tabla
        print("{:<10} {:<15}".format(i, resultado))

# Llamar a la función
calculadora_cientifica()