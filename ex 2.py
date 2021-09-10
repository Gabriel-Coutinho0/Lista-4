import random
numeros = random.sample(range(100),20)
par = []
impar = []

for x in numeros:
    if x %2 == 0:
        par.append(x)
    else:
        impar.append(x)
print ('Os numeros são: ',numeros)
print ('Os numeros pares são: ',par)
print ('Os numeros impares são: ',impar)  
