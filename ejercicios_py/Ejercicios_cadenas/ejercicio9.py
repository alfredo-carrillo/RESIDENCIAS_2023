#Ejercicio 9
#Escribir un programa que pregunte al usuario la fecha de su nacimiento 
#en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
#Adaptar el programa anterior para que también funcione cuando el día o 
#el mes se introduzcan con un solo carácter.

fecha = input("Introduce la fecha de nacimiento usando el siguiente formato.., dd/mm/aaaa ----> :")

dia = fecha[0:2]
mes = fecha[2:4]
año = fecha[4:8] 



print("La fecha de cumpleaños ingresada es: [ ",dia+"/",mes+"/",año+" ]")


fecha2 = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha2[:fecha2.find('/')]
mesaño = fecha2[fecha2.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)