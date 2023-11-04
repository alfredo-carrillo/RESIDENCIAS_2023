
lista = [1,2,3,6,9,8,5,4,7,8,5,1,4,6,9,3,5,4]
lista_xi = []
lista_xi_2 = []
diccionario =  {}
len_lis = len(lista)

def devuelve_diccionario(lista):
   media =  sum(lista)/len_lis
   diccionario['media '] = media

   for xi in lista:     
      lista_xi.append(xi-media)
   for xi_2 in lista_xi:
      lista_xi_2.append(abs(xi_2**2))
   varianza = sum(lista_xi_2)
   varianza = round(varianza/(len_lis-1), 2)
   desv_estandar = round(varianza**0.5, 2)

   #print(suma_vari)
   diccionario['varianza '] = varianza
   diccionario['desviacion estandar'] =  desv_estandar
   return print(diccionario)

devuelve_diccionario(lista)