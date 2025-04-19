n1 = int(input('Diga um valor'))
n2 = int(input('Diga outro valor'))
soma = n1+n2
multip = n1*n2
div = n1/n2
divinteira = n1//n2
expoente = n1**n2
print('A soma é: {}, a multiplicaçao é: {} e a divisao é: {:.3f}'.format(soma,multip,div), end= " >>> ")
print('A divisao inteira é: {} e a exponenciacao é: {}'.format(divinteira,expoente))