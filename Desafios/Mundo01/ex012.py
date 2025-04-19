produto = int(input('Digite o preço do produto:'))
descontar = produto*0.05
desconto = produto-descontar
print('O novo valor do produto com desconto é de R${:.2f}:'.format(desconto))