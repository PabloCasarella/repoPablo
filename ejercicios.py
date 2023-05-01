def imprimir(x):
    if x > 0:
        print(x)
        imprimir(x-1)

imprimir(6)
print()

def imprimir2(x):
    if x > 0:
        print(x)
        imprimir(x -1)

imprimir2(10)
