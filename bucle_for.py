#bucle for
#bucle con un numero determinado de iteraciones

#recorriendo una lista
for i in [1,2,3,4,5]:
    print("hola")

for i in [1,2,3,4,5]:
    print(i)

coleccion = [1,2,3,4,5,6]

for i in coleccion:
    print(f"elemento {i} de la coleccion")

#recorriendo un diccionario
#nos va a mostrar solo las claves sin los valores

diccionario = {"pablo":33, "maria":31, "bruno":36}

for i in diccionario:
    print(f"elemento: {i} del diccionario")

#queremos que nos muestre solo el valor del objeto

for i in diccionario:
    print(f"{diccionario[i]}")

#queremos que nos muestre clave y valor del objeto

for i in diccionario:
    print(f"{i} -> {diccionario[i]}")

# {i} nos muestra el valor de la clave
# {diccioanrio[i]} nos muestra los valores

for clave,valor in diccionario.items():
    print(f"{clave}, {valor} años")

#recorriendo cadenas

cadena = "pablo"

for i in cadena:
    print(i)#con salto de linea
print("\n")

for i in cadena:
   print(f"{i}",end=" ")
print("\n")

#for tipo range

for i in range(10):
    print(f"{i}",end=" ")
print("\n")

for i in range(1, 4):
    print(i)
print("\n")

for i in range(2,21,2):
    print(i)
print("\n")

for i in range(20,1,-2):
    print(i)
print("\n")


for i in range(10):
    if i == 5:
        continue
    if i == 7:
        continue
    print(i)
print("\n")

    


    



