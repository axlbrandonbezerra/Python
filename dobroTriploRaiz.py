#Autor: Axl Brandon Rodrigues
'''Programa para calcular o dobro,
o triplo e a raíz quadrada de um número qualquer'''
from time import sleep

while True:
    try:
        x = int(input('Digite um número: '))
    except ValueError:
        print('\033[31mDigite apenas valores numéricos\033[m')
    else:
        break
d = x * 2
t = x * 3
r2 = x ** (1/2)
sleep(0.8)
print(f'Dobro: \033[32m{d}\033[m')
sleep(0.8)
print(f'Triplo: \033[36m{t}\033[m')
sleep(0.8)
print(f'Raíz: \033[31m{r2:.2f}\033[m')
