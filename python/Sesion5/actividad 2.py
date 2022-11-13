luz = str(input("Digite la luz del semaforo : "))
peaton = str(input("escribe si hay peaton o no (si/no): "))
if(luz != "verde","amarillo","rojo"):
    print("el valor ingresado es invalido")
if(luz =="verde"):
    if(peaton == "si"):
        print("pare")
    elif(peaton == "no"):
        print("siga")
elif(luz =="amarillo"):
    if(peaton == "si"):
        print("pare")
    elif(peaton =="no"):
        print("precaucion")
else:
    if(luz == "rojo" and peaton == "si")or(peaton == "no") :
        print("pare")
    #else:
        #print("el valor ingresado es invalido")
