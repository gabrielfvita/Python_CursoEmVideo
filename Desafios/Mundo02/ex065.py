maior = 0
menor = 0
contador = 0
soma = 0
resposta = 'S'

while resposta == 'S':
    num = int(input('Informe um valor inteiro: '))
    if contador == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    contador += 1
    resposta = str(input('Deseja incluir outro valor? (S/N)' )).upper()

media = soma / contador

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Média entre todos os números digitados: {media:.2f}')    
print(f'Maior número digitado: {maior}')  
print(f'Menor número digitado: {menor}')  
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')     
