
def contar_palabras(url):
    '''
    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        with request.urlopen(url) as f:
            contenido = f.read()
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        return len(contenido.split())

print(contar_palabras('https://colab.research.google.com/github/asalber/aprendeconalf/blob/master/content/es/docencia/python/ejercicios/soluciones/ficheros/ejercicio4.ipynb#scrollTo=TUUPAiKkPIqc'))
print(contar_palabras('https://no-existe.txt'))