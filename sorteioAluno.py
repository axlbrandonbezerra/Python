#Autor: Axl Brandon Rodrigues
'''Sorteia um aluno qualquer de uma amostra de 4 alunos'''
from random import choice

a1 = str(input('Qual o nome do primeiro aluno? '))
a2 = str(input('Qual o nome do segundo aluno? '))
a3 = str(input('Qual o nome do terceiro aluno? '))
a4 = str(input('Qual o nome do quarto aluno? '))
lista = [a1, a2, a3, a4]
r = choice(lista)
print('O aluno escolhido foi: {}' .format(r))
