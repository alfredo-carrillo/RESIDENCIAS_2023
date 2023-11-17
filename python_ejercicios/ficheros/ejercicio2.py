# Ejercicio 2
def mostrar_tanlaN():
    try:
        n = int(input("Introduce un número entero entre 1 y 10: "))
        with open(f"tabla-{n}.txt", "r") as f:
            contenido = f.read()
            print(f"\nTabla de multiplicar de {n}:\n{contenido}")
    except FileNotFoundError:
        print(f"No se encuentra el archivo tabla con el valor -{n}.txt")
    except ValueError:
        print("Por favor, introduce un número entero.")
        
mostrar_tanlaN()