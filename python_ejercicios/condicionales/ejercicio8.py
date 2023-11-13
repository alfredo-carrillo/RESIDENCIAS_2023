#Ejercicio 8
#En una determinada empresa, sus empleados son evaluados al final de cada año. 
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir 
#aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir 
#los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre 
#las cifras mencionadas. A continuación se muestra una tabla con los niveles 
#correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
#
#Nivel	Puntuación
#Inaceptable	0.0
#Aceptable	0.4
#Meritorio	0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

puntos_empleado = float(input("introduce tus puntos: "))

if puntos_empleado == 0.0:
    print("has recibido 0.0€ de bonificacion, tu nivel es Inaceptable")
if puntos_empleado == 0.4:
    bonificacion = 2.400
    print("has recibido una bonificacion de : ", str(bonificacion)+"€ y tu nivel es Aceptable")
if puntos_empleado == 0.6 or puntos_empleado == 0.8:
    bonificacion = 2.400 * 2
    print("has recibido una bonificacion de : ", str(bonificacion)+"€ y tu nivel es Meritorio")
#
#bonificacion = 2400
#inaceptable = 0
#aceptable = 0.4
#meritorio = 0.6
#puntos = float(input("Introduce tu puntuación: "))
## Clasifiación por niveles de rendimiento
#if puntos == inaceptable:
#    nivel = "Inaceptable"
#elif puntos == aceptable:
#    nivel = "Aceptable"
#elif puntos >= 0.6:
#    nivel = "Meritorio"
#else:
#    nivel = ""
## Mostrar nivel de rendimiento
#if nivel == "":
#    print("Esta puntuación no es válida")
#else:
#    print("Tu nivel de rendimiento es %s" % nivel)
#    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))