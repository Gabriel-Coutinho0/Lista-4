from random import randint
lista1 = []
lista2 = []
lista3 = []
for x in range(10):
    x = randint(1,100)
    lista1.append(x)
    lista3.append(x)
    x = randint(1,100)
    lista2.append(x)
    lista3.append(x)
print('Os nûmeros da lista 1 são: ',lista1)
print('Os nûmeros da lista 2 são: ',lista2)
print('Os nûmeros da lista 3 são: ',lista3)
