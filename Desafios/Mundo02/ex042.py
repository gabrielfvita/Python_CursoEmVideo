l1 = float(input('Digite a medida do primeiro lado:'))
l2 = float(input('Digite a medida do segundo lado:'))
l3 = float(input('Digite a medida do terceiro lado:'))
if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1 and l1 == l2 and l2 == l3:
    print('Você pode formar um triangulo Equilátero com essas medidas!')
elif (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1 and l1 == l2 or l1 == l3 or l2 == l3:
    print('Você pode formar um triangulo Isósceles com essas medidas!')
elif (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1 and l1 != l2 and l2 != l3:
    print('Você pode formar um triangulo Escaleno com essas medidas!')
else:
    print('Você não pode formar um triângulo com essas medidas.')