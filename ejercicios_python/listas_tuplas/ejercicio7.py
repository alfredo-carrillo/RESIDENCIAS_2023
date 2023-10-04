#Ejercicio 7
#Escribir un programa que almacene el abecedario en una lista, 
#elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

abecedario = []

# Definir el rango de caracteres ASCII que deseas agregar a la lista
inicio = 97  # Código ASCII del espacio en blanco
fin = 122   # Último código ASCII imprimible

# Llenar la lista con los códigos ASCII
for codigo in range(inicio, fin + 1):
    abecedario.append(chr(codigo))

print(abecedario)