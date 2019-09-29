#Autor: Axl Brandon Rodrigues
'''Explorando propriedades'''

algo = input('Digite algo: ')
print('\033[31mO tipo primitivo desse valor é ', type(algo))
print('\033[32mÉ alfanumérico? ', algo.isalnum())
print('\033[33mÉ alfabético? ', algo.isalpha())
print('\033[34mÉ decimal? ', algo.isdecimal())
print('\033[35mÉ digito? ', algo.isdigit())
print('\033[36mÉ identificador? ', algo.isidentifier())
print('\033[37mÉ minusculoo? ', algo.islower())
print('\033[36mÉ numérico? ', algo.isnumeric())
print('\033[31mÉ printável? ', algo.isprintable())
print('\033[32mÉ espaço? ', algo.isspace())
print('\033[33mÉ um título? ', algo.istitle())
print('\033[34mÉ maiusculo? ', algo.isupper())

