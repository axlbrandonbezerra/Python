#Autor: Axl Brandon Rodrigues
'''Programa que calcula o financiamento de uma casa baseado no salário do usuário.'''

while True:
    try:
        casa = float(input('Qual o valor da casa? '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break

while True:
    try:
        salario = float(input('Quanto é o seu salário? '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break

while True:
    try:
        prestações = int(input('Em quantas prestações você quer pagar? '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break
valor = casa / (prestações *12)
print(f'Para pagar uma casa de R${casa} em {prestações} a prestação será de R${valor}')
if valor <= 0.30 * salario:
    print('Emprestimo Concedido!')
else:
    print('Emprestimo Negado!')
