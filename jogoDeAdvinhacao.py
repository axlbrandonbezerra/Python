#Autor: Axl Brandon Rodrigues
'''Jogo de advinhação
-----------------------
Gera um número aleatório de 0 a 5,
o usuário tenta acertar o número gerado'''
from random import randint
from time import sleep

x = randint(0, 5)
while True:
    try:
        re = int(input('Em que número eu pensei? '))
    except ValueError:
        print('Digite apenas valores inteiros!')
    else:
        break
print('-' * 15)
print('PROCESSANDO...')
print('-' * 15)
sleep(2)
if re == x:
    print(f'Você acertou! pensei no número {x} mesmo')
else:
    print(f'Errou! eu pensei em {x}, não em {re}')
