def parsear_pib(url):
    '''
    Función que parsea un fichero con pibs de países.
    Parámetros:
        url: Es una cadena con la url del fichero de texto que contiene el pib per cápita.
    Devuelve:
        Un diccionario con pares pais:pibs donde pibs es, a su vez, un diccionario con los años y los pibs del país.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        with request.urlopen(url) as f:
            datos = f.read().decode('utf-8').split('\n') # Leer los datos y guardar cada línea en una lista.
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        # Obtenemos los años de la primera linea del fichero.
        años = datos.pop(0).split('\t')[1:]
        # Creamos el diccionario prinpipal para guardar los pibs de todos los países.
        dict_pibs = {}
        # Bucle iterativo para recorrer las líneas del fichero.
        for pais in datos:
            datos_pais = pais.split('\t')
            # Obtenemos el código del país de los dos últimos caracteres del primer campo de la linea.
            codigo_pais = datos_pais.pop(0)[-2:]
            # Construimos un diccionario con los años y el pib del pais.
            dict_pais = {}
            # Bucle iterativo para recorrer los pibs del país.
            for i in range(len(datos_pais)):
                dict_pais[años[i].strip()] = datos_pais[i].strip()
            # Añadimos el diccionario con los pib del país al diccionario principal
            dict_pibs[codigo_pais] = dict_pais
        return dict_pibs

def pib(pibs, pais = "ES"):
    '''
    Función que recibe un diccionario con los pibs de los países y muestra por pantalla los pibs de un país dado.

    Parámetros:
        - pibs: Es un diccionario con los pibs de los países como el que devuelve la función parsear_pibs.
        - pais: Es una cadena con el código del país.

    Salida:
        Muestra por pantalla los pibs del país indicado.
    '''

    print("Año\tPIB")
    for i, j in pibs[pais].items():
        print(i, '\t', j)

pais = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', pais)
pib(parsear_pib("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"), pais)

