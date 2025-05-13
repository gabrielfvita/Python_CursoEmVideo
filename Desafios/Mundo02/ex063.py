num = int(input('Quantos elementos da sequência de fibonacci deseja visualizar? '))
cont = 3
termo_anterior = 1
termo_atual = 1
linha = '1 -> 1'

if num == 1:
    linha = '1'
elif num == 2:
    linha = '1 -> 1'
else:
    while cont <= num:
        fibonacci_atual = termo_atual + termo_anterior
        termo_anterior = termo_atual
        termo_atual = fibonacci_atual
        linha += f' -> {fibonacci_atual}'
        cont += 1
print(linha)