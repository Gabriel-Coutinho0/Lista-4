import random
numeros= random.sample(range(100),10)
maior = menor = numeros[0]
a = 1 

while a < 10:
    if numeros[a] > maior: maior = numeros[a]
    if numeros[a] < menor: menor = numeros[a]
    a = a + 1
print ('Nûmeros', numeros)
print (f'O maior nûmero é: {maior}')
print (f'O menor nûmero é: {menor}')
