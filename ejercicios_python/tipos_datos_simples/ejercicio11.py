## INVERSION A PLAZO DE AÑOS EN EL BANCO ##

interes= 4 # La taza de interes evaluada al 4% de la inversion primaria

ingreso = float(input("Ingresa la cantidad a invertir en cantidad de enteros: "))
años = int(input("Ingresa los plazos en cuestion de años a atender para la uinvesión:"))

inversion =  (ingreso*interes)/100

ganancia = (inversion + ingreso)

for i in range(4): 
    
    if i == 0: 
        print("\nGenerando la inversión......\n")
        
    else:
     print("El interes del año ", str(i)+" tiene un valor de: ", str(round(inversion, 2)))
     
     print("La ganancia generada el año ", str(i)+" sería : " + str(round(ganancia,2))+"\n")
     
     ingreso = float(ganancia)
     
     inversion =  (ingreso*interes)/100  
    
     ganancia = (inversion + ingreso)