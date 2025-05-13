valor1 = float(input('Digite o primeiro número: '))
valor2 = float(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    opcao = int(input('Escolha a opção desejada: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa \n'))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma de {valor1} + {valor2} = {soma:.2f}')
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print(f'A multiplicação de {valor1} x {valor2} = {multiplicacao:.2f}')
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
            print(f'O maior valor entre {valor1} e {valor2} é: {maior}')
        elif valor2 > valor1:
            maior = valor2
            print(f'O maior valor entre {valor1} e {valor2} é: {maior}')
        else:
            print(f'Não há um valor maior entre {valor1} e {valor2}. Ambos são iguais!')
    elif opcao == 4:
        valor1 = float(input('Informe o primeiro novo numero: '))
        valor2 = float(input('Informe o segundo novo numero: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Você digitou uma opção inválida. Tente novamente')