preco = float(input('Digite o valor do produto:'))
print('Selecione a sua condição de pagamento:')
print(' 1 - Ä Vista (Dinheiro/Cheque) \n 2 - Ä Vista (Cartão) \n 3 - 2x no Cartão \n 4 - 3x ou mais no Cartão')
pagamento = int(input())

if pagamento == 1:
    preco = preco * 0.90
elif pagamento == 2:
    preco = preco * 0.95
elif pagamento == 3:
    preco = preco
elif pagamento == 4:
    preco = preco * 1.20
else:
    print('Você não digitou uma opção válida')

print(f'O valor final do produto é de: R$ {preco:.2f}')