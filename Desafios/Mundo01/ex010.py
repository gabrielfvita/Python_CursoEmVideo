reais = float(input('Quantos reais voce tem na carteira?'))
dolar = 3.27
conversao = reais/dolar
print('Com R${} voce poderá comprar U${:.2f}'.format(reais,conversao))