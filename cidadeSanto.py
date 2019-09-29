#Autor: Axl Brandon Rodrigues
'''Programa que retorna verdadeiro se o nome da cidade começar com "Santo" '''

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')

