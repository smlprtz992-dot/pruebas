saldo = float(input("ingrese su saldo:"))

listcuentas = [saldo]
indexCuentaActiva = 0

op = ""

while op != "7":

    op = 0

while op != "4":
    print("\n---Menu---")
    print("1. consultar saldo")
    print("2. deposito")
    print("3. retiro")
    print("4. salir")

    op = input("elige una opcion:")

    if op == "1":
        print("su saldo es:" , saldo)


    elif op == "2":
        deposito = float(input("Ingrese monto a depositar: "))
        if deposito > 0:
            saldo += deposito
            print(f"Deposito exitoso. Tu saldo es {saldo}")
        else:
            print(f"Monto invalido.")
        

    elif op == "3":
        retiro = float(input("Ingrese valor a retirar: ")) 
        if retiro > saldo:
            print("Saldo insuficiente")
        elif retiro <= 0:
            print("Monto de retiro invalido")
        else:
            saldo -= retiro
            print(f"Retiro exitoso. Nuevo saldo {saldo}")


    elif op == "4":
        print("Gracias por usar nuestro sistema")
    else:
        print("Opcion invalida")




             
                           



 
 
 



