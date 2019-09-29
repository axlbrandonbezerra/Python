#Autor: Axl Brandon Rodrigues
'''Calcula a área e quantos litros de tinta serão usados para pintar a parede'''

while True:
    try:
        a = float(input('Digite a altura de uma parede em metros: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break
while True:
    try:
        l = float(input('Digite a largura da parede em metros: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break
area = l * a
pintar = area / 2
print(f'A sua parede tem dimensão de {l}x{a}\nÁrea: {area}m²\nPintar: {pintar:.2f} Litros')
