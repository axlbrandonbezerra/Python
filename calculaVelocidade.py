#Autor: Axl Brandon Rodrigues
'''Programa que calcula a velocidade de um carro e aplica uma multa de 7 reais por quilometro
acima do limite de velocidade que é de 80km/h'''
from time import sleep

while True:
    try:
        v = float(input('Qual a velocidade atual do carro? '))
    except:
        print('Digite apenas valores numéricos!')
    else:
        break
print('=' * 15)
print('PROCESSANDO...')
print('=' * 15)
sleep(1)
if v > 80.0:
    multa = 7.0 * (v - 80.0)
    print(f'''MULTADO! Você excedeu o limite permitido que é de 80Km/h.
Você deverá pagar uma multa de R${multa:.2f}''')
else:
    print('Velocidade dentro do limite permitido. Tenha um bom dia! Dirija com segurança.')
