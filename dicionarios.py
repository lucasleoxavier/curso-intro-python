# -*- coding: utf-8 -*-

# Dicionário sempre se declara entre chaves
user = {"nome": "Lucas", "idade": 27, "sexo": "M"}

print(user['idade']) # imprimindo pela chave
print(user) # imprimindo tudo
for key in user:
    print(user[key]) # imprimindo em um laço

# Retornando de outra forma os itens do dicionário
for k in user.items(): # converte o dicionario pra uma tupla
    print(k)

# Retornando apenas valores
for val in user.values():
    print(val)