# -*- coding: utf-8 -*-

frutas = ["laranja","morango","limão"]
print(frutas)

numeros = [5,7,12,35,67]
print(numeros)

mista = [True, 7.94, "Texto", 52]
print(mista)

#Imprimindo um item pelo índice
print(frutas[2]) #vai imprimir o último item

#Usando um laço for
for item in frutas:
    print(item)

#Ver tamanho da lista
tamanho = len(frutas)
print(tamanho)

#Adicionar elemento na lista
frutas.append("tangerina")
print(frutas)

#Verificar se existe um elemento na lista
if 11 in numeros: # VALOR in LISTA => "limão" in frutas --- retorna true
    print('Existe')
else:
    print('Não existe')

#Removendo elementos da lista
del numeros[2]
print (numeros)

del frutas[:] # apaga a lista inteira
print (frutas)

del mista[1:3] # apaga começando pela posição 1, indo até o terceiro item (esse segundo número segue a partir do 1, invés de 0 a n)
print(mista)

"""
ORDENANDO LISTAS
"""

#Sort - sort alterar a lista original, sorted precisa passar o valor novo pra mesma variavel ou uma variavel nova
lista01 = [25,74,169,684,18,594,21,43,11,456,98,72,2,55,37,91,421]
lista01.sort()
print(lista01)
    # ao passar o reverse como true, ele ordena de modo descrescente
lista01 = [25,74,169,684,18,594,21,43,11,456,98,72,2,55,37,91,421]
lista01.sort(reverse=True)
print(lista01)

#Reverse - ele espelha a lista
lista01.reverse()
print(lista01)