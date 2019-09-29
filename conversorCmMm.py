#Autor: Axl Brandon Rodrigues
'''Conversor de metros para centimetros e milimetros '''

while True:
    try:
        m = float(input('Digite um valor em metros: '))
    except ValueError:
        print('Digite apenas valores inteiros!')
    else:
        break
c = m * 100
mili = m * 1000
print(f'{m} metros, equivale a {c} centímetros e {mili} milímetros')
