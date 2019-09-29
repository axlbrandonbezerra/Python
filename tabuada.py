#Autor: Axl Brandon Rodrigues
'''Tabuada simples'''

while True:
    try:
        num = int(input('Digite um número: '))
    except ValueError:
        print('Digite apenas valores inteiros!')
    else:
        break
x = 1
print('=' * 12)
while x <= 10:
    print(f'{num} * {x} = {num*x}')
    x = x + 1
print('=' * 12)
