# While
i = 1

while i <= 10:
    print(i)
    i += 1 # mesma coisa que i = i + 1

# For
listaInt = [1,2,3,4,5]
listaString = ["Olá","Mundo","!"]
listaMista = [5,"Olá",1.35,True]

for lista in listaInt:
    print(lista)

for lista in listaString:
    print(lista)

for lista in listaMista:
    print(lista)

# For Range
for x in range(10): # Imprime de 0 a 9
    print(x)

for y in range(10, 20): # Imprime de 10 a 19
    print(y)

for z in range(10, 20, 2): # Imprime de 10 a 19, de 2 em 2
    print(z)
