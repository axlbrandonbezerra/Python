#Autor: Axl Brandon Rodrigues
'''Programa simples para calcular a média das notas de um aluno'''

while True:
    try:
        n1 = float(input('Qual foi a sua primeira nota? '))
    except ValueError:
        print('\033[31mDigite apenas valores numéricos\033[m')
    else:
        break

while True:
    try:
        n2 = float(input('Qual foi a sua segunda nota? '))
    except ValueError:
        print('\033[31mDigite apenas valores numéricos\033[m')
    else:
        break
media = (n1 + n2) / 2
print("Nota 1: {}\nNota 2: {}\nMédia: {}" .format(n1, n2, media))
