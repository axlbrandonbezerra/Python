#Autor: Axl Brandon Rodrigues
'''Programa simles que mostra se um número é par ou ímpar'''

while True:
    try:
        n1 = int(input('Digite um número: '))
    except:
        print('Digite apenas valores inteiros!')
    else:
        break
if n1 % 2 == 0:
    print(f'{n1} é par!')
else:
    print(f'{n1} é impar!')
