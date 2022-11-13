numero = int(input("ingrese un numero: "))
contador = 2

while (contador <= numero):
    print (contador, end=" ")
    if (contador == 20):
        break

    contador += 2
print("fin del programa")