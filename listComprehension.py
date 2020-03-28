x = [1, 2, 3, 4, 5]
y = []
z=[]

# variavel = [valor_a_adicionar laço condição]

# exemplo sem condição
y = [i**2 for i in x]

print(x)
print(y)

# exemplo com condição
z = [i for i in x if i % 2 != 0]

print(x)
print(z)