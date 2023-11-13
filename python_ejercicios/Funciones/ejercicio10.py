list_conv = []
bin_to_dec = [1, 1, 1, 1]
list_conv_invertida = []
pos_elevar = []



def deci_bin (num):
 
  list_conv.append(num%2)

  while int(num) != 0:
    num = num / 2
    convierte = int(num%2)
    list_conv.append(convierte)
    

    cadena = ''.join(map(str, list_conv[::-1]))
  print(cadena)
  return list_conv_invertida

list_conv_invertida = list_conv[::-1] 

def  bin_deci(bin):
  equivalencia = []
  for index in range(len(bin)):
     pos_elevar.append(index)
     equivalencia.append(2)
     
     
     new_dec = [x ** y for x, y in zip(equivalencia, pos_elevar)]
     result = [x*y for x, y in zip(bin, new_dec)]

  

  print(result)
  return(print(sum(new_dec)))
  

deci_bin(12577)
bin_deci([1,0,1,1,1])
################################
def to_decimal(n):
    """Función que convierte un número binario en decimal.
    Parámetros:
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n.
    """
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def to_binary(n):
    """Función que convierte un número decimal en binario.
    Parámetros:
        - n: Es un número entero.
    Devuelve:
        El número binario correspondiente a n.
    """
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))

