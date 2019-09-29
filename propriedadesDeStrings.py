#Autor: Axl Brandon Rodriges
'''Testando algumas propriedades de String'''

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiusculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
#print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
se = nome.split()
print(f'Seu primeiro nome é {se[0]} e tem {len(se[0])} letras')

