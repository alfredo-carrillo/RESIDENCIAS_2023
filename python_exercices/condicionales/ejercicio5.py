#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años 
#y tener unos ingresos iguales o superiores a 1000 € mensuales. 
#Escribir un programa que pregunte al usuario su edad y sus ingresos 
#mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Ingresa tu edad."))

ingresos_mensuales = int(input("Inserta tus ingresos mensuales :"))

if edad >= 16 and ingresos_mensuales >= 1000:
    print("Usted ya debe tributar ..... :c")

else:
    print("Usted aún no debe tributar, felicidades!")

