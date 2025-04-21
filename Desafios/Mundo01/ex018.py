from math import sin,cos,tan, radians
num = float(input('Digite um angulo:'))

print('Segue abaixo os valores do seno, cosseno e tangente de {} \n \n Seno: {:.2f} \n Cosseno {:.2f} \n Tangente {:.2f}'.format(num,sin(radians(num)),cos(radians(num)),tan(radians(num))))
