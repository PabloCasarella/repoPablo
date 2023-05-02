'''Hacer un programa para ingresar el radio de un circulo
y se reporte su area y la longitud de la circunferencia.
formulas:
    area: PI * r**2
    longitud: 2 * PI * r
'''
radio = float(input("introduzca el radio del circulo: "))

area = 3.1416 * (radio**2)
longitud = 2 * 3.1416 * radio

print(f"el area del circulo es: {area:.2f}")
print(f"la longitud del circulo es: {longitud:.2f}")
