mais_barato_valor = 10000000000
mais_barato_nome = ' '
total = 0
produtos_mais_mil = 0
contador = 1

while True:
    print(f'------ Produto {contador} ------')
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Informe o preço do produto: '))

    contador += 1
    total += preco
    if preco > 1000:
        produtos_mais_mil += 1
    if preco < mais_barato_valor:
        mais_barato_valor = preco
        mais_barato_nome = nome
    
    continuar = str(input('Deseja continuar? (S/N) ')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Opção inválida. Deseja continuar? (S/N) ')).upper()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Total gasto = R${total:.2f}')
print(f'Total de produtos que custam mais de R$1000: {produtos_mais_mil}')
print(f'Produto mais barato: {mais_barato_nome} (R${mais_barato_valor:.2f})')