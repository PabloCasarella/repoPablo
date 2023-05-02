'''Las tuplas son otro tipo de cdoleccion muy parecidas las listas
pero com la diferencia de que son inmutables, son mas rapidas
consumen menos recursos y son mas rapidas a la hora de
acceder a ellas'''

tupla = (4,"hola",6.78,[1,2,3],5)

print(tupla)

print(tupla[1])

print(tupla.index("hola"))

print(tupla.count(5))

print(len(tupla))

#transformar tupla en lista

lista = list(tupla)
print(lista)

#transformar lista en tupla

tupla2 = tuple(lista)

print(tupla2)




