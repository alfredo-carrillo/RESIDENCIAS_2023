def apply_discount(price, discount):
 
    return price - price * discount / 100
    
def apply_IVA(price, percentage):
  
    return price + price * percentage / 100

def price_basket(basket, function):

    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total

print('El precio de la compra tras aplicar los descuentos es: ', price_basket({2563:20, 500:10, 100:1}, apply_discount))
print('El precio de la compra tras aplicar el IVA es: ', price_basket({5896:20, 500:10, 100:1}, apply_IVA))