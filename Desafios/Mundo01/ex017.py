from math import hypot
catop = float(input('Qual a medida do cateto oposto?'))
catadj = float(input('Qual a medida do cateto adjacente?'))
hip = hypot(catop,catadj)
print('A medida da hipotenusa é de {:.2f}'.format(hip))