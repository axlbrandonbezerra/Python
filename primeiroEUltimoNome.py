#Autor: Axl Brandon Rodrigues
'''Mostra o seu primeiro nome e seu ultimo nome'''

nome = str(input('Digite seu nome completo: ')).strip().split()
u = len(nome)-1
print('Prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[u]}')

