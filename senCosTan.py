#Autor: Axl Brandon Rodrigues
'''Mostra o Seno, Cosseno e Tangente de um ângulo qualquer'''
from math import radians, sin, cos, tan

while True:
    try:
        ang = float(input('Digite um ângulo: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'Seno: {sen:.2f}\nCosseno: {cos:.2f}\nTangente: {tan:.2f}')
