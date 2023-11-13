pan = 3.49

descuento = (3.49*60)/100
pan_ayer = round((pan-(3.49*60)/100), 2)


print(pan_ayer)

venta = int(input("Cuantas barras de pan del dpia anterior se han vendido el día de hoy?  :"))

venta_total = pan_ayer*float(venta)

print("\nLas barras de pan horneadas al día tienen un precio de 3.49€ c/u\n")

print("Las barras que son del día anterior tienen un descuento del 60%, equivalente a :", str(descuento)+"€ del precio total")

print("La venta total del día de hoy de los panes rancios es de : ", str(venta_total)+"€")


