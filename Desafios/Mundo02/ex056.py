soma = 0
maior_idade = 0
nome_maisvelho = ''
mulheres_menos_20 = 0

for c in range(1,5):
    print(f'----- PESSOA {c} -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): '))

    soma += idade

    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_maisvelho = nome
    if sexo == 'F'and idade < 20:
        mulheres_menos_20 += 1

media = soma/4

print(f'Média das idades: {media:.2f} anos')
print(f'Homem mais velho: {nome_maisvelho} ({maior_idade} anos)')
print(f'Quantidade de mulheres abaixo de 20 anos: {mulheres_menos_20}')