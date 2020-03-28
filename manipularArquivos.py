# -*- coding: utf-8 -*-

"""
MODOS DE LEITURA
r - somente leitura;
w - escrita (se o arquivo já existia, será apagado e um novo arquivo vazio será criado)
a - leitura e escrita (conteúdo novo será adicionado ao fim do arquivo)
r+ - leitura e escrita
w+ - escrita (mesmo modo que o w, apaga se já houver arquivo e cria um novo)
a+ - leitura e escrita (abre o arquivo para atualização)
//// o sinal de + permite atualização ////
"""

# Open - abre o arquivo
arquivo = open("arquivoExemplo.txt")

# Read - lê o arquivo inteiro
textoCompleto = arquivo.read()

# Readline - lê uma linha
line = arquivo.readline()

# Readlines - lê o arquivo e o armazena em uma lista
lines = arquivo.readlines()

# Criando um arquivo
newFile = open("novoArquivoCriadoPeloPython.txt", "w")

# Inserindo dados no arquivo
newFile.write("Populando o arquivo")

# Fechando os arquivos após edição
arquivo.close()
newFile.close()