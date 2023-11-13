#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
#Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(subjects)-1, -1, -1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 5:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))


#subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#passed = []
#for subject in subjects:
#    score = float(input("¿Qué nota has sacado en " + subject + "?"))
#    if score >= 5:
#        passed.append(subject)
#for subject in passed:
#    subjects.remove(subject)
#print("Tienes que repetir " + str(subjects))