etnia = str(input())
if (etnia != 'sin reconocimiento'and etnia !='afrodescendiente'and etnia !='indigena'and etnia !='palenquero'and 
etnia !='gitano'and etnia != 'raizal'): 
    print("presenta un error")
    quit()
estrato = int(input())
ingresos = int(input())
salario = 908526

if (etnia == 'sin_reconocimiento') or (etnia == 'sin reconocimiento'):
    etnia = 0   
elif (etnia == 'afrodescendiente'):
    etnia = 9
elif (etnia == 'indigena'):
    etnia = 10
elif (etnia == 'raizal'):
    etnia = 11
elif (etnia == 'palenquero'):
    etnia = 12
elif (etnia == 'gitano'):
    etnia = 13



if (estrato == 1):
    estrato = 15
elif (estrato == 2):
    estrato = 13
elif (estrato == 3):
    estrato = 11
elif (estrato == 4):
    estrato = 7
elif (estrato == 5):
    estrato = 0
elif (estrato == 6):
    estrato = 0
else:
    print("presenta un error")


if (ingresos < salario):
    ingresos = 20
elif ((ingresos >= salario) and (ingresos < 2*salario)):
    ingresos = 14
elif ((ingresos >= 2*salario) and (ingresos < 4*salario)):
    ingresos = 12
elif ((ingresos >= 4*salario) and (ingresos < 5*salario)):
    ingresos = 9
elif (ingresos >= 5*salario):
    ingresos = 0

puntaje = int(etnia) + estrato + ingresos
if (puntaje >= 30):
    print("El candidato continua en el proceso de seleccion")
else:
    print("El candidato no continua en el proceso de seleccion")
