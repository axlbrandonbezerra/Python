#Autor: Axl Brandon Rodrigues
'''Programa que recebe 3 valores e mosra qual é o maior e menor número.'''
from time import sleep

while True:
    try:
        x = int(input('Primeiro número: '))
    except ValueError:
        print('Digite apenas valores inteiros!')
    else:
        break

while True:
    try:
        y = int(input('Segundo número: '))
    except:
        print('Digite apenas valores inteiros!')
    else:
        break
while True:
    try:
        z = int(input('Terceiro número: '))
    except:
        print('Digite apenas valores inteiros!')
    else:
        break
if x > y and x > z:
    maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
if x < y and x < z:
    menor = x
if y < x and y < z:
    menor = y
if z < y and z < x:
    menor = z
sleep(2)
print(f'{maior} é o maior núemro!')
print(f'{menor} é o menor número!')
