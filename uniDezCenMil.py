#Autor: Axl Brandon Rodrigues
'''Mostra a unidade, dezena, centena e milhar de um número qualquer'''

while True:
    try:
        número = int(input('Digite um número: '))
    except ValueError:
        print('Digite apenas valores inteiros!')
    else:
        break
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')


