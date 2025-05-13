num = 0
contador = 0
soma = 0

while num != 999:
    num = int(input('Informe um valor: '))
    if num == 999:
        break
    else:
        contador += 1
        soma += num

print(f'Você digitou {contador} numeros. \nA soma entre todos eles é: {soma}')