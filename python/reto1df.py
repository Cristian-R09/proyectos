
etnia = str(input())
if (etnia != 'sin reconocimiento'and etnia !='afrodecendiente'and etnia !='indigena'and etnia !='palenquero'and 
etnia !='gitano'): 
    print("presenta un error")
ingresos = (input())

salario = 908526
puntaje = 0

if (etnia == 'sin reconocimiento'):
     puntaje 
elif (etnia == 'afrodecendiente'):
    puntaje += 9 
elif (etnia == 'indigena'):
    puntaje += 10
elif (etnia == 'raizal'):
    puntaje += 11
elif (etnia == 'palenquero'):
    puntaje += 12
elif (etnia == 'gitano'):
    puntaje += 13


#else :

   # print("presenta un error")
    

estrato  = int(input())
if (estrato == 1):
    puntaje += 15
elif (estrato == 2):
    puntaje += 13
elif (estrato == 3):
    puntaje += 11
elif (estrato == 4):
    puntaje += 7
elif (estrato == 5):
    puntaje += 0
elif (estrato == 6):
    puntaje += 0

print(puntaje)
#else:
    #print("presenta un error")


if (ingresos < salario):
    puntaje += 20  
elif ((ingresos >= salario) and (ingresos < 2*salario) ):
    puntaje += 14
elif ((ingresos >= 2*salario) and (ingresos < 4*salario) ):
    puntaje += 12
elif ((ingresos >= 4*salario) and (ingresos < 5*salario)):
    puntaje += 9
elif (ingresos >= 5*salario):
    puntaje += 0
print(puntaje)
#resultado = int(etnia) + estrato + puntaje
if (puntaje >= 30):
    print("El candidato continua en el proceso de seleccion")
else:
    print("El candidato no continua en el proceso de seleccion")


