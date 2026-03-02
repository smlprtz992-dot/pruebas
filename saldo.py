saldo = float(input("ingrese su saldo:"))
listcuentas = [saldo]
indexCuentaActiva = 0

op = ""

while op != "7":
    print("\n---Menu---")
    print("1. consultar saldo")
    print("2. deposito")
    print("3. retiro")
    print("4. nueva cuenta")
    print("5. listar cuenta")
    print("6. seleccionar cuenta")
    print("7. salir")
    
    try :
         
        print("cuenta activa:",(indexCuentaActiva + 1))
        op = input("elige una opcion:")
        if op == "1":
            print(f"su saldo es:{indexCuentaActiva + 1}: {listcuentas[indexCuentaActiva]}")

        elif op == "2" :
            dep = float(input("cuanto deseas depositar"))
            if dep <0 :
                print("datos invalidos, no se pueden depositar cantidades negativas")
            else :
                listcuentas[indexCuentaActiva] = listcuentas[indexCuentaActiva] + dep
                print(f"su saldo es:{listcuentas[indexCuentaActiva]}")
        elif op == "3" :
            retirar = float|(input("cuanto deseas retirar: "))
            descuento = retirar * 0.004
            if(retirar + descuento)>listcuentas[indexCuentaActiva] :
                print("saldo de cuenta insuficiente")
            
            else : 
                listcuentas[indexCuentaActiva] = listcuentas[indexCuentaActiva] - retirar - descuento
                print(f"descuento del 4x1000 = ${descuento}")
                print(f"su nuevo saldo es: {listcuentas[indexCuentaActiva]}")
        
        elif op == "4":
         nuevaCuenta = float(input("digite el saldo de la nueva cuenta:{nueva cuenta}"))
        
        elif op == "5" :
            print("listado de cuenta: ")
            for i in range(len(listcuentas)):
                print(f"cuenta{i + 1}: {listcuentas[i]}")
        
        elif op == "6":
            cuentaSeleccionada = int(input("digite el numero de la cuenta a seleccionar: "))

            if cuentaSeleccionada <1 or cuentaSeleccionada >1 (listcuentas): print("numero de cuenta invalido")
            else:
                indexCuentaActiva = nuevaCuenta -1
                print(f"cuenta{cuentaSeleccionada} seleccionada exitosamente")
        
        elif op == "7":
            print("saliendo,gracias por usar nuestros servicios")

    except:
        print("el dato ingresado no es valido")


       




             
                           



 
 
 



