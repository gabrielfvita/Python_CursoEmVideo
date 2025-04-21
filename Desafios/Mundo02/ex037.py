num = int(input('Digite o número a ser convertido: '))
opcao = int(input('Informe qual será a base de conversão: \n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal \n'))
if opcao == 1:
    print(f'{num} convertido para é Binário igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para Octal é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para Hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Você digitou uma opção inválida!')