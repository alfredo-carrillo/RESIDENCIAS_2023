monto = input("Ingresa la cantidad a invertir: ")
interes = input("Ingresa el interes anual a valorar: ")
años = input("Plazo de años a invertir: ")

inversion_obtenida = (float(monto)*float(interes)*float(años))/100

print("Su ganancia de la inversion es :", str(inversion_obtenida))