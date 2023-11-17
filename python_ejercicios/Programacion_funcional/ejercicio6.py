
# Ejercicio 6
def get_calificaciones(notas):
    def asignar_calificacion(nota):
        if nota >= 90:
            return 'A'
        elif nota >= 80:
            return 'B'
        elif nota >= 70:
            return 'C'
        elif nota >= 60:
            return 'D'
        else:
            return 'F'
    return [asignar_calificacion(nota) for nota in notas]

print(get_calificaciones([100, 45, 78, 69, 85, 96, 88, 97, 56, 1]))