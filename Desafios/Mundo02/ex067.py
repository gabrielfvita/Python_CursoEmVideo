while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('=-' * 15)
        print('Programa encerrado. Volte sempre!')
        break
    else:
        print('=-' * 15)
        for i in range(1,11):
            print(f'{n} x {i} = {n*i}')
        print('=-' * 15)