#Autor: Axl Brandon Rodrigues
'''Programa simples que mostra quantos dolares você pode cambiar'''

while True:
    try:
        reais = float(input('Quanto dinheiro você tem na sua carteira? '))
    except ValueError:
        print('Digite apenas valores reais!')
    else:
        break
dolares = reais / 3.27 #cotação atual do dolar
print(f'Você pode comprar US${dolares:.2f} com R${reais:.2f}')
