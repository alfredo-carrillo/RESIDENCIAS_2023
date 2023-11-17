def linea_fichero():
    try:
        n = int(input("Introduce un número entero entre 1 y 10: "))
        m = int(input("Introduce el número de línea a mostrar: "))
        with open(f"tabla-{n}.txt", "r") as f:
            lineas = f.readlines()
            if 1 <= m <= 10:
                print(lineas[m - 1])
            else:
                print("Número de línea fuera de rango.")
    except FileNotFoundError:
        print(f"No se encuentra el archivo tabla-{n}.txt")
    except ValueError:
        print("Por favor, introduce un número entero.")
        
linea_fichero()