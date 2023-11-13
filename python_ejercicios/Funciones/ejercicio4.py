
def calcula_factura(cantidad, iva=21):
    # iva  = iva/100
#     # total_fac =  (cantidad*iva) + cantidad

    #return total_fac
    return cantidad + cantidad*iva/100
print(calcula_factura(1525, 16))
print(calcula_factura(1525))