from random import randint

contador = 0

while True:
    jogador = int(input('Digite um valor: '))
    opcao = str(input('Par ou Ímpar? (P/I) ')).upper()

    computador = randint(0,10)
    soma = computador + jogador
    
    while opcao != 'P' and opcao != 'I':
        opcao = str(input('Opção inválida. Par ou Ímpar? (P/I) ')).upper()
    if soma % 2 == 0:
        print('-=' * 30)
        print(f'Você jogou {jogador} e o computador {computador}. O total foi {soma} (PAR)')
        print('-=' * 30)
    else:
        print('-=' * 30)
        print(f'Você jogou {jogador} e o computador {computador}. O total foi {soma} (IMPAR)')
        print('-=' * 30)

    if soma % 2 == 0 and opcao == 'P':
        print('Você VENCEU \nVamos jogar novamente...')
        print('---' * 20)
        contador += 1
    elif soma % 2 != 0 and opcao == 'I':
        print('Você VENCEU \nVamos jogar novamente...')
        print('---' * 20)
        contador += 1
    else:
        print('Você PERDEU!')
        print('-=' * 30)
        break
print(f'GAME OVER! Você venceu {contador} vezes.')