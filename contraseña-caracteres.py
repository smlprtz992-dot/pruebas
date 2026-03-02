contraseña_almacenada = ("12345")

contraseña_digitada = input("ingrese una contraseña de 5 digitos: ")

array1 = list (contraseña_almacenada)
array2 = list (contraseña_digitada)

len(array1) == len(array2)

cont = 0

for i in range(len(array1)):
    print("comparando el digito", array1[i] , "con el digito" , array2[i])
    if array1[i] == array2[i]:
        cont += 1
        print("el digito" , array1[i] , "es correcto")
        print("la cantidad de digitos correctos es:" , cont)


if cont == len(array1) :
    print("contraseña correcta, acceso concedido")
else :

    print("contraseña incorrecta acceso denegado")        

