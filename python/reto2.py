
numero_personas = int(input())      #personas que ingresaron 
acumulador = 0                      #contador de personas que ingresan
salario = 908526
No_valido = False

 # contador de cada etnia
sum_reco = 0                       
sum_afrod = 0
sum_ind = 0
sum_raiz = 0
sum_pal = 0
sum_git = 0

while (acumulador < numero_personas):

    etnia = str(input())
    estrato = int(input())
    ingresos = int(input())

    acumulador += 1

for i in range(1 , numero_personas + 1): 

    if  (etnia =="sin reconocimiento"):
        etnia = 0 
        sum_reco += 1
    elif (etnia == 'afrodescendiente'):
        etnia = 9
        sum_afrod += 1
    elif (etnia == 'indigena'):
        etnia = 10
       
        sum_ind += 1
    elif (etnia == 'raizal'):
        etnia = 11
        
        sum_raiz += 1
    elif (etnia == 'palenquero'):
        etnia = 12
        
        sum_pal += 1
    elif (etnia == 'gitano'):
        etnia = 13
        
        sum_git += 1
    else :
        while (No_valido == True):
            acumulador = -1
            
        
        
    """elif (etnia != "sin reconocimiento" and
         "afrodescendiente" and "indigena" 
         and "raizal"and "palenquero" and "gitano"):
       
        continue"""


        #estratos
for i in range(numero_personas):

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
    else : 
        while (No_valido == True):
            acumulador = -1
            break
    #elif (estrato != 1 and 2 and 3 and 4 and 5 and 6):
       # continue

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


while (puntaje >= 30):
    while (No_valido == False):
        print (numero_personas)
    else :
        print (acumulador - 1)
        break

   
    

print(f"sin reconocimiento {sum_reco}") 
print(f"afrodescendiente {sum_afrod}")
print(f"indigena {sum_ind}")
print(f"raizal {sum_raiz}")
print(f"palenquero {sum_pal}")
print(f"gitano {sum_git}")

    