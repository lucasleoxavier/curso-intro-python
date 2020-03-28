"""
1 - Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.
"""
idade = int(input("Digite sua idade\n"))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
"""
2 - Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva
aprovado, senão escreva reprovado.   
"""
nota01 = int(input("Digite a primeira nota\n"))
nota02 = int(input("Digite a segunda nota\n"))
media = (nota01+nota02)/2
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
"""
3 - Escreva um programa que resolva uma equação de segundo grau.   
"""
a = int(input("Digite o valor de A\n"))
b = int(input("Digite o valor de B\n"))
c = int(input("Digite o valor de C\n"))
delta = (b**2)-(4*a*c)
x1 = (-b + delta**(1/2))/(2*a)
x2 = (-b - delta**(1/2))/(2*a)

print('Valor de A: %d\nValor de B: %d\nValor de C: %d\nValor de Delta: %d\nX1: %d\nX2: %d' % (a, b, c, delta, x1, x2))
"""
4 - Escreva um programa que ordene uma lista numérica com três elementos.   
"""
lista = [7, 2, 9]
print(lista)
lista.sort()
print(lista)
"""
5 - Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
"""
v1 = int(input("Digite o primeiro valor\n"))
v2= int(input("Digite o segundo valor\n"))
simbolo = input("Selecione o símbolo=>\n+   adição\n-   subtração\n/   divisão\n*   multiplicação\n")
if simbolo == '+':
    print(v1+v2)
elif simbolo == '-':
    print(v1-v2)
elif simbolo == '/':
    print(v1/v2)
elif simbolo == '*':
    print(v1*v2)