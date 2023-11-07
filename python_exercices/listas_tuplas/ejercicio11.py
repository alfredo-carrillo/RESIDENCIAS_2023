#Ejercicio 11
#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

#producto escalar
#v1.v2= (u1*v1)+(u2*v2)+(u3*v3)
#=3(–1)+5(3)+2(0)=−3+15+0=12.
#

a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 