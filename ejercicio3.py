'''para estimar el peso de un niño en situaciones de emergencias pediatricas,
se utiliza la siguiente formula: peso en kilogramos = 3*edad+7

Dada la edad de un niño en años, diseñe un algoritmo que determine el peso
estimado del niño.
'''
#datos de entrada
edad = int(input("ingresa la edad del niño"))

#procesos
k = 3*edad+7

#salida de datos
print("el peso estimado del niño es de: ",k)
    
