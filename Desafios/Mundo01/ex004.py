teclado = input('Digite algo para obter informaçoes: ')

tipo = type(teclado)

print('O tipo primitivo da palavra digitada é: {}'.format(tipo))
print('Só tem espaços?', teclado.isspace())
print('É um número?', teclado.isnumeric())
print('É alfabético?', teclado.isalpha())
print('É alfanumérico?', teclado.isalnum())
print('Contem apenas letras maiusculas?', teclado.isupper())
print('Contem apenas letras minusculas?', teclado.islower())
print('Está capitalizada?', teclado.istitle())

