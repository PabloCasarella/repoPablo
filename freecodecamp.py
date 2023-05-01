width = 15
height = 12.0
print(height / 3)

x = 10
y = 2
print(x/y)

sval = '123'

sval = int(sval)

print(type(sval))

print(sval + 1)

x = 0

if x < 2:
    print('small')
elif x < 10:
    print('medium')
else:
    print('large')
print('all done')

astr = 'hello bob'
try:
    istr = int(astr)
except:
    istr = -1
print('first',istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('second',istr)

zork = 0

print('before',zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork,thing)
print('after',zork)


'''Promedio'''

cont = 0
suma = 0
print('before',cont,suma)
for value in [9,41,12,3,74,15]:
    cont += 1
    suma = suma + value
    print(cont,suma,value)
print('after',cont,suma,suma/cont)


print('before')
for value in [9,41,12,3,74,15]:
    if value > 20:
        print('Large number',value)
print('after')


found = False
print('before',found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found, value)
print('after',found)


largest = -1
print('before',largest)

for num in [9,41,12,3,74,15]:
    if num > largest:
        largest = num
    print(largest, num)
print('after',largest,num)



menor = None
print('Before')

for num in [9,41,12,3,74,15]:
    if menor == None:
        menor = num
    elif num < menor:
        menor = num
    print(menor, num)
print('after', menor)


for letra in 'banana':
    print(letra)

for letra in range(len('banana')):
    print(letra)

apellido = ' casarella '
print(apellido.strip())




