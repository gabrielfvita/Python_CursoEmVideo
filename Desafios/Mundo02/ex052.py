num = int(input('Digite um número:'))
total = 0 

for c in range(1,num +1):
    if num % c == 0:
        print(f'\033[33m {c}')
        total += 1
    else:
        print(f'\033[031m {c}')
print(f'\033[mO número {num} foi dividido {total} vezes')
if total == 2:
    print('Logo, ele é PRIMO!')
else:
    print('Logo, ele NÃO é primo!')