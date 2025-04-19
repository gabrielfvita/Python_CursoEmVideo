from datetime import date

ano = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - ano

if idade <= 9:
    print('Categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')