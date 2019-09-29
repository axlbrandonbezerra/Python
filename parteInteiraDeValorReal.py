#Autor: Axl Brandon Rodrigues
'''Mostra a parte inteira de um número real'''
from math import trunc

while True:
    try:
        num = float(input('Digite um número: '))
    except ValueError:
        print('Digite apenas valores numéricos')
    else:
        break

print(f'O número {num} tem a parte inteira {trunc(num)}')
