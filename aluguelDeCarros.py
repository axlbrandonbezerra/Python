#Autor: Axl Brandon Rodrigues
'''Calcula o custo de aluguel de carro por km rodados'''

while True:
    try:
        dias = int(input('Qual a quantidade de dias alugados? '))
    except ValueError:
        print('Digite apenas valores inteiros!')
    else:
        break

while True:
    try:
        kmr = float(input('Quantos Km rodados? '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break

custototal = (60 * dias) + (0.15 * kmr)
print(f'O total a pagar é R${custototal:.2f}')