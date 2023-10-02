#Ejercicio 7
#Escribir un programa que pregunte el correo electrónico del 
#usuario en la consola y muestre por pantalla otro correo 
#electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.


correo= input("Introduce tu correo porfavor : ")
sub_cadena = "@"

correo.find(sub_cadena)
index = correo.index(sub_cadena)

sus = "@ceu.es"

print(index)
data = correo[index:]
print(data)

new_mail = correo.replace(data, "@ceu.es")

print(new_mail)

#correo_nuevo = replace(correo.find("@":), 'asd')




#sample_string = "This is a sample string"

#char_to_replace = {'s': 'X',
#                   'a': 'Y',
#                   'i': 'Z'}
#
## Iterate over all key-value pairs in dictionary
#for key, value in char_to_replace.items():
#    # Replace key character with value character in string
#    sample_string = sample_string.replace(key, value)
#
#print(sample_string)