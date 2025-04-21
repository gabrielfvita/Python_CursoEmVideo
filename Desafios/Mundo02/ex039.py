from datetime import date
ano = int(input('Informe seu ano de nascimento:'))

idade = date.today().year - ano

print(f'Você tem {idade} anos')

if idade < 18:
    restante = 18 - idade
    print(f'Você precisará se alistar ao serviço militar daqui {restante} ano(s)!')
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    ultrapassou = idade - 18
    print(f'Já se passaram {ultrapassou} ano(s) desde o seu ano de alistamento!')