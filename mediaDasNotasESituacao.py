#Autor: Axl Brandon Rodrigues
'''Recebe as duas notas de um aluno, calcula sua média
e também informa se o aluno foi aprovado, em recuperação ou reprovado'''
from time import sleep

def situação(media):
    if media < 5.0:
        print('Aluno foi REPROVADO!')
    elif media >= 5 and media <= 6.9:
        print('Aluno em RECUPERAÇÃO!')
    else:
        print('Aluno foi APROVADO!')


#programa principal
while True:
    try:
        n1 = float(input('Digite sua 1° nota: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break

while True:
    try:
        n2 = float(input('Digite sua 2° nota: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break

media = (n1 + n2) / 2
print(f'N1: {n1}\nN2: {n2}\nMEDIA: {media}')
print('PROCESSANDO...\n')
sleep(2)
situação(media)




