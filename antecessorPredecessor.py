#Autor: Axl Brandon Rodrigues
'''Programa simples para mostrar o antecessor e o predecessor de um número qualquer'''
from time import sleep

def molde():
    print('=-'*15)


while True:
    try:
        x = int(input('\033[32mDigite um número: \033[m'))
    except ValueError:
        print('\033[31mDigite apenas valores numéricos\033[m')
    else:
        break
sleep(0.8)
molde()
print(f'\033[34mSeu antecessor: {x-1}\nSeu predecessor: {x+1}\033[m')
molde()



