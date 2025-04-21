s = float(input('Qual seu salário atual? '))
if s > 1250.00:
    aumento = s + (s * 0.10)
    print(f'O seu novo salário será de {aumento}')
else:
    aumento = s + (s * 0.15)
    print(f'O seu novo salário será de {aumento}')
