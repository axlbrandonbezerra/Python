#Autor: Axl Brandon Rodrigues
'''Progrma simples para analisar se um triângulo pode ser formado ou não'''

print('-=' * 30)
print('Analisador de triangulos')
print('-=' * 30)
while True:
    try:
        a = float(input('Digite o primeiro segmento: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break

while True:
    try:
        b = float(input('Digite o segundo segmento: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break

while True:
    try:
        c = float(input('Digite o terceiro segmento: '))
    except ValueError:
        print('Digite apenas valores numéricos!')
    else:
        break
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
