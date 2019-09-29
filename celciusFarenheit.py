#Autor: Axl Brandon Rodrigues
'''Conversor de Celcius para Farenheit'''

while True:
    try:
        c = float(input('Digite uma temperatura em °C: '))
    except ValueError:
        print('Digite apenas valores numéricos')
    else:
        break
f = (c * 9/5) + 32
print(f'A temperatura {c:.1f}°C é igual a {f:.1f}°F')
