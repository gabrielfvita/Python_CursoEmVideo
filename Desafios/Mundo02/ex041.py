from datetime import date

ano = int(input('Informe o ano de nascimento do atleta:'))
idade = date.today().year - ano

print(f'O Atleta tem {idade} anos.')
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')