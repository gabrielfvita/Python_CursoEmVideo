valor = float(input('Informe o valor da casa: '))
salario = float (input('Informe o seu salário:'))
anos = float(input('Em quantos anos pretende pagar a casa?'))

meses = anos * 12
prestacao = valor / meses

if prestacao > (salario * 0.30):
    print('Seu empréstimo foi negado!')
else:
    print(f'Empréstimo aprovado! O valor da sua prestação mensal é de: R${prestacao:.2f}')