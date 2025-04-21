valor = float(input('Informe o valor da casa: '))
salario = float (input('Informe o seu salário: '))
anos = int(input('Em quantos anos pretende pagar a casa?'))

meses = anos * 12
prestacao = valor / meses

print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}')
if prestacao > (salario * 0.30):
    print('Empréstimo NEGADO!')
else:
    print(f'Empréstimo APROVADO!')