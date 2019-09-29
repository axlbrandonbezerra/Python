#Autor: Axl Brandon Rodrigues
'''Calcula um desconte de 5% em cima de uma valor qualquer'''

while True:
    try:
        preço = float(input('Digite o preço: R$'))
    except ValueError:
        print('Digite um valor numérico!')
    else:
        break
desconto = preço - (preço * 0.05)
print(f'Preço: R${preço:.2f}\nDesconto: R${desconto:.2f}')
