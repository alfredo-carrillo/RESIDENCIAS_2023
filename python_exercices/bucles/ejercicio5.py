#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, 
#el interés anual y el número de años, y muestre por pantalla el 
#capital obtenido en la inversión cada año que dura la inversión.

inversion = int(input("Ingresa la cantidad de inversion "))

interes = int(input("Ingresa el interes anual a manejar "))

años = int(input("Ingresa los años a invertir"))



for x in range(1, años+1):

 inversion_obtenida = (float(inversion)*float(interes)*float(años))/100

 inversion = inversion_obtenida + inversion  
    
 print(f"la inversion del año {x} es {round(inversion_obtenida, 2)} con un total de {inversion}")