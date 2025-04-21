peso = float(input('Informe o seu peso em KG: \n'))
altura = float(input('Informe a sua altura em Metros: \n'))
imc = peso / (altura**2)

print(f'Seu IMC É de: {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('Peso Ideal')
elif imc > 25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')