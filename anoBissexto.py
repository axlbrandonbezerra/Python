#Autor: Axl Brandon Rodrigues
'''Mostra se o ano digitado é bissexto ou não'''

while True:
    try:
        ano = int(input('Digite um ano: '))
    except:
        print('Digite apenas valores inteiros!')
    else:
        break
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é ano bissexto!')
