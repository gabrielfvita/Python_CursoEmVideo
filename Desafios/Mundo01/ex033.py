n1 = int(input('Digite o primeiro numero'))
n2 = int(input('Digite o segundo numero'))
n3 = int(input('Digite o terceiro numero'))

# Verificando o menor número
if n1<n2 and n1<n3:
    print(f'O menor número é o {n1}')
if n2<n1 and n2<n3:
    print(f'O menor número é o {n2}')
if n3<n1 and n3<n2:
    print(f'O menor número é o {n3}')

# Verificando o maior número
if n1>n2 and n1>n3:
    print(f'O maior número é o {n1}')
if n2>n1 and n2>n3:
    print(f'O maior número é o {n2}')
if n3>n1 and n3>n2:
    print(f'O maior número é o {n3}')