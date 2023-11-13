print("Cual es tu peso en kg?")
peso = input()

print("Cuál es tu altura, en metros ?")
altura = input()


imc = round(float(peso) / float(altura)**2, 2)

print("Tu índice de masa corporal es <imc>", str(imc) + "<imc>" )



