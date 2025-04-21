nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'A média do aluno é de {media:.2f}')

if media < 5:
    print('O aluno está REPROVADO')
elif media > 5 and media < 6.9:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno está APROVADO!')