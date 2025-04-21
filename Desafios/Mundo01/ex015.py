dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Qual foi a quilometragem percorrida com o veículo? '))
valor = (dias*60)+(km*0.15)
print('O valor a ser pago pelo periodo de {} dias e de {} km percorridos é de R${:.2f}'.format(dias,km,valor))