from datetime import date

maiores = 0
menores = 0

for c in range(1,8):
    nascimento = int(input(f'Informe o ano de nascimento da {c}ª pessoa: '))
    idade = date.today().year - nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'{maiores} pessoas são maiores de idade e {menores} pessoas são menores de idade!')
