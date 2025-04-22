frase = str(input('Digite a frase: '))

tras = ''
frente = ''

for c in range(0, len(frase)):
    if frase[c] != ' ':
        frente += frase[c]

for c in range(len(frase), 0, -1):
    if frase[c-1] != ' ':
        tras += frase[c-1]

if frente == tras:
    print(f'A frase "{frase}" é um palindromo')
else:
    print(f'A frase "{frase}" NÃO é um palindromo')