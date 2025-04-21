d = float(input('Digite a distância da sua viagem: '))
if d <= 200:
    print(f'O valor da sua passagem é de R${d*0.50:.2f}')
else:
    print(f'O valor da sua passagem é de {d*0.45:.2f}')