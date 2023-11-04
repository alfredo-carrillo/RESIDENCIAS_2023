lista = [1,2,3,6,9,8,5,4,7,8,5,1,4,6,9,3,5,4]
lista2 =  []

def media(lista):
   for x in lista:
      square = x**2
      lista2.append(square)
      
   return print(f"la lista con sus cuadrados es [ {lista} ^ 2 ] ---->   {lista2} ")


media(lista)