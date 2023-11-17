def nota(cifra):
    '''Función que elimina cambia las comas de separación de decimales por puntos de una cifra y la convierte en un real.
    Parámetros:
        - cifra: Es una cadena con una cifra.
    Devuelve:
        Un real con la cifra de la cadena después de cambiar el separador de decimales por punto.
    '''
    cifra = cifra.replace(',','.')
    return float(cifra) 

def calificaciones(ruta):
    '''Función que preprocesa los datos contenidos en un fichero con formato csv y devuelve una lista de diccionarios donde las claves de los diccionarios son los datos de la primera fila y los valores los datos de cada línea del fichero.
    
    Parámetros:
        - ruta: Es una cadena con la ruta del fichero.
    Devuelve:
        Una lista de diccionarios donde cada diccionario contiene los datos de una linea del fichero (a excepción de la primera línea), usando como claves los datos de la primera línea.
    '''
    try:
        # Abrimos el fichero en modo lectura
        f = open(ruta, 'r')
    except FileNotFoundError:
        print('El fichero no existe.')
        return
    # Leemos el fichero por líneas en una lista
    lineas = f.readlines()
    # Cerramos el fichero
    f.close()
    # Leemos las claves del primer elemento de la lista, eliminamos el cambio de línea que aparece al final y dividimos la cadena por el punto y coma.
    claves = lineas[0][:-1].split(";")
    # Creamos la lista de calificaciones
    calificaciones = []
    # Recorremos las líneas del fichero y para cada línea creamos un diccionario que añadimos a la lista de calificaciones.
    for i in lineas[1:]:
        # Eliminamos el cambio de línea del final y dividimos la cadena por el punto y coma.
        valores = i[:-1].split(";")
        # Creamos un diccionario vacío para ir añadiendo los datos de cada alumno.
        alumno = {}
        # Recorremos la lista de valores y los añadimos al diccionario.
        for j in range(len(valores)):
            alumno[claves[j]] = valores[j]
        # Añadimos el diccionario a la lista de calificaciones
        calificaciones.append(alumno)
    return calificaciones

def añadir_nota_final(calificaciones):
    '''Función que recibe una lista de diccionarios con las calificaciones de cada alumno en un curso, calcula la nota final del curso de cada alumno y la añade al diccionario del alumno.

    Parámetros:
        - calificaciones: Es una lista de diccionarios donde cada diccionario contiene los datos de un alumno (nombre, asistencia y notas de exámenes del curso).
    Devuelve:
        La lista de las calificaciones de los alumnos tras añadir a cada alumno de la lista su nota final del curso.
    '''

    def nota_final(alumno):
        '''Función que calcula la nota final del curso de un alumno.

        Parámetros:
            - alumno: Es un diccionario con las notas del alumno.
        Devuelve:
            El diccionario con los datos del alumno tras añadirle un nuevo par con la nota final del curso.
        '''
        if alumno['Ordinario1']: #Si el alumno se ha presentado al examen de repesca del primer parcial tomamos esa nota como la nota del primer parcial
            parcial1 = nota(alumno['Ordinario1'])
        elif alumno['Parcial1']:
            parcial1 = nota(alumno['Parcial1'])
        else: # No se ha presentado al primer parcial ni a la repesca en el ordinario
            parcial1 = 0
        if alumno['Ordinario2']: #Si el alumno se ha presentado al examen de repesca del segundo parcial tomamos esa nota como la nota del segundo parcial
            parcial2 = nota(alumno['Ordinario2'])
        elif alumno['Parcial2']:
            parcial2 = nota(alumno['Parcial2'])
        else: # No se ha presentado al segundo parcial ni a la repesca en el ordinario
            parcial2 = 0 
        if alumno['OrdinarioPracticas']: #Si el alumno se ha presentado al examen de repesca de prácticas tomamos esa nota como la nota de prácticas
            practicas = nota(alumno['OrdinarioPracticas'])
        elif alumno['Practicas']:
            practicas = nota(alumno['Practicas'])
        else:
            practicas = 0
        alumno['Final1'] = parcial1
        alumno['Final2'] = parcial2
        alumno['FinalPracticas'] = practicas
        alumno['NotaFinal'] = parcial1 * 0.3 + parcial2 * 0.3 + practicas * 0.4
        return alumno

    # Aplicamos la función nota_final a todos los alumnos
    return list(map(nota_final, calificaciones))

def aprobados_suspensos(calificaciones):
    '''Función que recibe una lista de diccionarios con las calificaciones de cada alumno en un curso, y devuelve la lista de aprobados y suspensos en el curso.

    Parámetros:
        - calificaciones: Es una lista de diccionarios donde cada diccionario contiene los datos de un alumno (nombre, asistencia y notas de exámenes del curso).
    Devuelve:
        - aprobados: Es una lista con los nombres de los alumnos aprobados.
        - suspensos: Es una lista con los nombres de los alumnos suspensos.
    '''
    # Creamos las listas de aprobados y suspensos vacías
    aprobados = []
    suspensos = []
    # Recorremos los alumnos del curso
    for alumno in calificaciones:
        # Si se cumplen las condiciones para aprobar añadimos el nombre del alumno a la lista de aprobados y si no a la de suspensos.
        if all([int(alumno['Asistencia'][:-1]) >= 75, alumno['Final1'] >= 4, alumno['Final2'] >=4, alumno['FinalPracticas'] >=4, alumno['NotaFinal'] >= 5]):
            aprobados.append(alumno['Apellidos'] + ', ' + alumno['Nombre'])
        else:
            suspensos.append(alumno['Apellidos'] + ', ' + alumno['Nombre'])
    return aprobados, suspensos

# Llamada a las funciones de prueba
print(añadir_nota_final(calificaciones('calificaciones.csv')))
aprobados, suspensos = aprobados_suspensos(añadir_nota_final(calificaciones('calificaciones.csv')))
print('Lista de aprobados:', aprobados)
print('Lista de suspensos:', suspensos)
