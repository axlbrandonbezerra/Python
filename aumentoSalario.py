#Autor: Axl Brandon Rodrigues
'''Calcula o aumento de 15% em cima de um salário qualquer'''

while True:
    try:
        salario = float(input('Digite seu salário: R$'))
    except:
        print('Digite um valor numérico!')
    else:
        break
aumento = salario + (salario * 0.15)
print(f'Seu salário antigo é de R${salario:.2f}\nSeu salário novo é de R${aumento:.2f}')
