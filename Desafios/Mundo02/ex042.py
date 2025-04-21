l1 = float(input('Digite a medida do primeiro lado: '))
l2 = float(input('Digite a medida do segundo lado: '))
l3 = float(input('Digite a medida do terceiro lado: '))

if l1 == l2 == l3:
    tipo = 'Equilátero'
elif l1 == l2 or l1 == l3 or l2 == l3:
    tipo = 'Isósceles'
else:
    tipo = 'Escaleno'
if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:
    print(f'Você pode formar um triangulo {tipo} com essas medidas!')
else:
    print('Você não pode formar um triângulo com essas medidas.')