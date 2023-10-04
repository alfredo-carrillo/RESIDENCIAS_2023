#Ejercicio 4
##Escribir un programa que pregunte al usuario los números ganadores de# 
#la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.#
lotery = []
lotery2 = []

n = 0 # Establecemos un contador del largo del vector

while len(lotery) !=  8:
 lotery_num = input("Ingresa los numeros ganadores de la lotería primitiva:  ")
 lotery.append(lotery_num)


lotery.sort()
print("Los números ganadores son " + str(lotery))



#
#for _ in lotery:
#        n += 1 #Contamos la cantidad de caracteres dentro del vector
#    
#for i in range(n-1): 
#    # Le damos un rango n para que complete el proceso. 
#            for j in range(0, n-i-1): 
#            # Revisa la matriz de 0 hasta n-i-1
#             if lotery[j] > lotery[j+1] :
#                lotery[j], lotery[j+1] = lotery[j+1], lotery[j]
#            # Se intercambian si el elemento encontrado es mayor 
#            # Luego pasa al siguiente
#
#print ("El vector ordenado es: ",lotery)
#



#
#for x in range(len(lotery)):
#    
# for i in range(len(lotery)):   
#    if lotery[0]< lotery[::]:

    #print(lotery[1])

#  print(x)