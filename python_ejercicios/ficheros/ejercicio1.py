# Ejercicio 1
def generar_tabla():
    try:
        n = int(input("Introduce un número entero entre 1 y 10: "))
        if 1 <= n <= 10:
            with open(f"tabla-{n}.txt", "w") as f:
                for i in range(1, 11):
                    f.write(f"{n} x {i} = {n * i}\n")
            print(f"Tabla de multiplicar de {n} guardada en tabla-{n}.txt")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Por favor, introduce un número entero.")
        
generar_tabla()