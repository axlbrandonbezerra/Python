#Autor: Axl Brandon Rodrigues
'''Conversor de número decimal para Binário, Hexadecimal e Octadecimal'''
from time import sleep
import os

def binario(x):
    opc = ''
    bina = bin(numInt)
    print(f'{x} == {bina} ')


def hexadecimal(x):
    hexa = hex(numInt)
    print(f'{x} == {hexa} ')


def octadecimal(x):
    octa = oct(numInt)
    print(f'{x} == {octa} ')


def menu(numInt):
    while True:
        sleep(1)
        print('Escolha uma das bases para conversão:')
        print('[ 1 ] converter para BINÁRIO')
        print('[ 2 ] converter para HEXADECIMAL')
        print('[ 3 ] converter para OCTAL')
        print('[999] Para sair')
        while True:
            try:
                opc = int(input('Sua opção: '))
            except ValueError:
                print('Digite apenas valores inteiros!')
            else:
                break
        if opc == 1:
            sleep(.8)
            binario(numInt)
        elif opc == 2:
            sleep(.8)
            hexadecimal(numInt)
        elif opc == 3:
            sleep(.8)
            octadecimal(numInt)
        elif opc == 999:
            break
        else:
            sleep(.8)
            print('Apenas uma das opções acima!')


#programa principal
while True:
    try:
        numInt = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Digite apenas valores inteiros!')
    else:
        break
menu(numInt)



