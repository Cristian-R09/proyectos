numero = 0
acumulador = 0
numeros_digitados = 0

while (numero != -1):
    acumulador += numero
    numeros_digitados += 1
    numero = int(input(f"digite un numero, lleva {numeros_digitados} numeros digitados :"))
promedio = 0
if ((numeros_digitados-1)!= 0):
    promedio = acumulador / (numeros_digitados-1)

print(f"el promedio de los numeros digitados es {promedio}")
