#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

vegetariana = "vegetariana"
carnivora = "carnivora"
ingredientes = ['Pimiento', 'tofu', 'Peperoni', 'Jamón', 'Jamon', 'Salomón', 'Salmon']

ques= input("Que tipo de pizza desea ordenar? [ vegetariana ] o [ carnivora ]   ")



if ques == vegetariana:

    print("     ------------- EL MENU VEGETARIANO -------------------\n") 
    print(" Todas las pizzas llevan incluido salsa de tomate y mozarela")

    ingrediente =  input("Solo puedes escoger un ingrediente\n\nPimiento\n tofu\n")

    x = ingredientes.index(ingrediente)

    if ingrediente == ingredientes[x]:

        print("Tu pizza es vegetariana y el ingrediente escogido es", ingrediente)
    else:
        print("escoge un aditamiendo porfavor")
elif ques == carnivora:

    print("     ------------- EL MENU CARNIVORO -------------------\n") 
    print(" Todas las pizzas llevan incluido salsa de tomate y mozarela\n")

    ingrediente =  input("Solo puedes escoger un ingrediente\n\Peperoni\n Jamón\n Salmón\n")
    x = ingredientes.index(ingrediente)

    if ingrediente == ingredientes[x]:

        print("Tu pizza es carnivora y el ingrediente escogido es", ingrediente)
    
