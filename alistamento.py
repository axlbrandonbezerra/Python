#Autor: Axl Brandon Rodrigues
'''Programa para analisar se uma pessoa tem idade suficiente para se alistar o exército.'''
from time import sleep
from datetime import date

atual = date.today().year
while True:
    try:
        nasc = int(input('Ano de nascimento: '))
    except ValueError:
        print('Digite apenas valores inteiros!')
    else:
        break
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
sleep(2)
ano_alistamento = (atual - 18) - nasc
no = nasc - (atual - 18)
if idade == 18:
    print('Você já pode se alistar!')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {ano_alistamento} anos!')
    print(f'Seu alistamento foi em {atual - ano_alistamento}')
else:
    print(f'Ainda faltam {no} anos para o alistamento!')
    print(f'Seu alistamento será em {atual + no}.')
