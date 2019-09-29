#Autor: Axl Brandon Rodrigues
'''Programa simples de ajuste de salário:
se o salário for abaixo de R$1250,00, o salário receberá 15% de aumento.
se o salário for acima de R$1250,00, o salário receberá 10% de aumento.'''

while True:
    try:
        salario = float(input('Qual é o salário do funcionário? '))
    except:
        print('Digite apenas valores numéricos!')
    else:
        break
if salario <= 1250.0:
    ajuste = salario + (salario * 0.15)
else:
    ajuste = salario + (salario * 0.10)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${ajuste:.2f} agora!')
