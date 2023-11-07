def contar_palabras(cadena):
    palabras = cadena.lower().split()
    frecuencia = {}

    for palabra in palabras:
        palabra = palabra.strip('.,!?;:"()[]{}')
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

def palabra_mas_repetida(diccionario):
    if not diccionario:
        return None, 0

    palabra_mas_comun = max(diccionario, key=diccionario.get)
    frecuencia = diccionario[palabra_mas_comun]

    return palabra_mas_comun, frecuencia

# Ejemplo de uso
cadena = "Este es un ejemplo. Para poder probar las palabras repetidas dentro de una cadena y darle un mejor oreden."
frecuencias = contar_palabras(cadena)
palabra, frecuencia = palabra_mas_repetida(frecuencias)

print("Frecuencia de cada palabra:")
for palabra, freq in frecuencias.items():
    print(f"{palabra}: {freq}")

print(f"Palabra más repetida: '{palabra}' frecuencia repetida {frecuencia}")
