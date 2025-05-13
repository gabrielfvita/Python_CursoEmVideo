contador = 1
maior18 = 0
homens = 0
mulheres_menos_vinteanos = 0

while True:
    print(f'--------- Pessoa {contador} ---------')
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo: (M/F)')).upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Opção inválida. Informe o sexo: (M/F)')).upper()

    contador += 1

    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_vinteanos += 1
    
    continuar = str(input('Deseja continuar? (S/N) ')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Opção inválida. Deseja continuar? (S/N) ')).upper()

    if continuar == 'N':
        break

print('------ FIM DO PROGRAMA ------')
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo, temos {homens} homens cadastrados')
print(f'E temos {mulheres_menos_vinteanos} mulheres com menos de 20 anos.')