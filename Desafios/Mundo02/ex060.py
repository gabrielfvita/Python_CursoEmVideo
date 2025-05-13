num = int(input('Digite um número: '))
atual = num
fatorial = f'{atual}'
resultado = 1

while atual != 1:
    resultado = resultado * atual
    atual -= 1
    fatorial += f' x {atual}'
print(f'{num}! = {fatorial} = {resultado} ')