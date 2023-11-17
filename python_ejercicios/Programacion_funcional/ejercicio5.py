
def dic_oalabras(frase):
    
    palabras = frase.split()
    diccionario_longitudes = {}


    for palabra in palabras:
        diccionario_longitudes[palabra] = len(palabra)

    return diccionario_longitudes


cadena = "Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."
dict = dic_oalabras(cadena)
print(dict)
