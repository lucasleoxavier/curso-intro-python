def dobro(i):
    return i*2

valor = [1, 2, 3, 4, 5, 6]
valorDobrado = map(dobro, valor)

for v in valorDobrado:
    print(v)
