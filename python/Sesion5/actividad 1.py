luz = str(input("Digite la luz del semaforo : "))

'''la forma mas facil de formular condiciones es a travez de afirmaciones que debemos
verificar en nuestra estructura '''

if(luz =="verde"):
    print("siga")
else:
    if(luz =="amarilla"):
        print("precaucion")
    elif (luz =="rojo"):
        print("pare")
    else:
        print("la palabra digitada no es valida")