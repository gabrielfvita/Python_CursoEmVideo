soma = 0 
for c in range(1,501,2): # Impar
    if c % 3 == 0 : # Multiplo de 3
        soma += c
print(f'A soma é: {soma}')