soma = 0
contador = 0
while True:
    n = int(input('Digite um numero inteiro: (999 para parar) '))
    if n == 999:
        break
    else:
        soma += n
        contador += 1
print(f'A soma dos {contador} números é igual a: {soma}!')