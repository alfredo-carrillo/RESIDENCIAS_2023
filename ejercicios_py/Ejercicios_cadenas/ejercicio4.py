#Ejercicio 4
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
#donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
#(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número 
#de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

prefijo = "+34"
extension = "+34-913724710-56"

num = input("Ingresa el numero de telefo con el siguiente formato,  +34-XXX000XXX-56: ")


print("El numero de telefono registrado fue :", num+"\n")

for caracteres in num:
    if caracteres == "+34-" and caracteres == "-52":

#num.remove("+34", "-52")

        print("El numero de telefono sin el prefijo + 34 y extemsion -52 es:", caracteres )
