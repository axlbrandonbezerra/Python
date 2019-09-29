#Autor: Axl Brandon Rodrigues
'''Programa que calcula quanto o usuário irá gastar em passagem em uma viagem.
se a distância percorrida for menor ou igual a 200km, o preço da passagem será 50% do valor da distância,
se for maior, será de 45% do valor da distância'''

while True:
    try:
        x = float(input('Qual a distância da sua viagem? '))
    except:
        print('Digite apenas valores numéricos!')
    else:
        break
print(f'Você está prestes a começar uma viagem de {x}Km.')
if x <= 200.0:
    preço = 0.50 * x
else:
    preço = 0.45 * x
print(f'E o preço da sua passagem será de R${preço}!')
