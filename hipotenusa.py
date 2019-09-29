#Autor: Axl Brandon Rodrigues
'''Calcula o comprimento da hipotenusa'''
from math import hypot

while True:
    try:
        co = float(input('Digite o comprimento do Cateto Oposto: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break
while True:
    try:
        ca = float(input('Digite o comprimento do Cateto Adjacente: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break
print(f'O comprimento da Hipotenusa é {hypot(co, ca):.2f}')
