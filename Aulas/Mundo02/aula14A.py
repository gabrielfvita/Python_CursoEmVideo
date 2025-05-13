n = 1
par = 0
impar = 0
total = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    total += 1
print(f'Você digitou {total} numeros, sendo: {par} numeros pares e {impar} numeros impares!')