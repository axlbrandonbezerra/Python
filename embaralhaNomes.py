#Autor: Axl Brandon Rodrigues
'''Embaralha uma lista de quatro nomes e dispõe em uma ordem aleatória'''
from random import shuffle

n1 = str(input('Digite o nome do 1°: '))
n2 = str(input('Digite o nome do 2°: '))
n3 = str(input('Digite o nome do 3°: '))
n4 = str(input('Digite o nome do 4°: '))
lista = [n1, n2, n3, n4]
embaralhar = shuffle(lista)
print('A ordem de apresentação será:')
print(lista)

