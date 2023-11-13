#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

pedidos_payasos = input("Ingresa cuantos payasos quieres: ")
pedidos_muñecas = input("Ingresa cuantas muñecas quieres: ")

print(pedidos_muñecas)
print(pedidos_payasos)

peso_total = int(pedidos_muñecas)*75 + int(pedidos_payasos)*112
peso_gramos = peso_total
peso_total = peso_total / 1000


print("El peso total del pedido es : ", str(peso_total)+"kg    &    el peso total en gramos es: ", str(peso_gramos)+"g")