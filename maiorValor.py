#Autor: Axl Brandon Rodrigues
'''Programa que mostra qual valor é maior que o outro'''

def maiorMenor(x, y):
    if x > y:
        print(f'O primeiro valor {x} é maior que {y}!')
    elif x < y:
        print(f'O segundo valor {y} é maior {x}!')
    else:
        print(f'O primeiro valor é o mesmo que o segundo! ambos valem {x}')


#programa principal
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
    except ValueError:
        print('Digite apenas valores inteiros!')
    else:
        break
maiorMenor(x, y)



