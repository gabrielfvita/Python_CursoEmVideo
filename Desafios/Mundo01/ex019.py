from random import choice
p = str(input('Digite o primeiro aluno'))
s = str(input('Digite o segundo aluno'))
t = str(input('Digite o terceiro aluno'))
q = str(input('Digite o quarto aluno'))

lista = [p, s, t, q]
escolhido = choice(lista)
print(escolhido)