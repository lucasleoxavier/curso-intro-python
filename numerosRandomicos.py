# -*- coding: utf-8 -*-
import random

numero = random.randint(0,10) # gerando um número random de 0 a 10, incluindo 0 e 10
print(numero)

# Usando método choice
lista = [5, 7, 9, 12, 14, 27, 38]
numero = random.choice(lista)
print(numero)