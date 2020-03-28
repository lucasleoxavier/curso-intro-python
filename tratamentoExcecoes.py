# -*- coding: utf-8 -*-

# Vamos fazer uma divisão por 0, que quebraria o código
a = 8
b = 0

try: # vai tentar fazer o que tem aqui no bloco
    print(a/b)
except: # e se tudo der errado, executa esse bloco
    print('Error')