#Autor: Axl Brandon Rodrigues
'''Programa simples de soma'''

while True:
    try:
        x = int(input('\033[32mDigite um número: \033[m'))
    except ValueError:
        print('\033[31mDigite apenas valores numéricos\033[m')
    else:
        break

while True:
    try:
        y = int(input('\033[32mDigite outro número: \033[m'))
    except ValueError:
        print('\033[31mDigite apenas valores numéricos\033[m')
    else:
        break
s = x + y
print(f'\033[34mA soma de {x} e {y} é {s}\033[m')
