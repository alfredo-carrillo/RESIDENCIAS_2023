def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    subjects = map(str.upper, scores.keys())
    grades = map(grade, scores.values())
    return dict(zip(subjects, grades))

print(apply_grade({'Matemáticas':8.5, 'Física':8.6, 'Química':10.00, 'Economía':8.2, 'Historia':9.4, 'Programación':7.6}))