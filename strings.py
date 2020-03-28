# -*- coding: utf-8 -*-

var1 = "Olá"
var2 = "Mundo"

# Concatenação
frase1 = var1 + " " + var2
print(frase1)

# Mostrar tamanho de uma string
palavraLonga = "Pneumoultramicroscópicosilicovulcanoconiótico"
print(len(palavraLonga))

# Navegando pelo índice de uma string
nome = "Lucas Xavier"
print(nome[6]) # vai mostrar o 'X', índice começa do 0

# Imprimindo parte de uma string
print(nome[2:10]) # vai imprimir 'cas Xavi'

# Deixar em caixa baixa
tortaLimao = "TORTA DE LIMÃO"
print(tortaLimao.lower())

# Deixar em caixa alta
pizza = "Pizza de Marguerita"
print(pizza.upper())

# Remove caracteres especiais e espaços no início e no fim da string
texto1 = " Testando o método string() do Python\n"
print("Antes do strip() =>"+texto1)
print("Depois do strip() =>"+texto1.strip())

# Converte uma string em uma lista, dividindo os itens pelo que for passado no método
texto2 = "O Chamado de Cthulhu"
stringToList = texto2.split(" ") # aliás, aqui é case sensitive
print(stringToList)

# Buscar uma substring
texto3 = "A Cor de Caiu do Céu"
search = texto3.find("Caiu")
print(search)   # se não encontrar nada, retorna -1

# Substituir partes de uma string
texto4 = "O rato roeu a roupa do Rei de Roma"
novoTexto4 = texto4.replace("Rei","Príncipe")
print("Antigo=> "+texto4)
print("Novo=> "+novoTexto4)