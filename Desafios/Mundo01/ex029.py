vel = float(input('Digite a velocidade do seu carro: '))
if vel > 80.0:
    print('Você está acima do limite e foi multado! O valor da multa é de: R${:.2f}'.format((vel-80)*7.0))
else:
    print('Você estava dentro do limite, pode prosseguir!')