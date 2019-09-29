#Autor: Axl Brandon Rodrigues
'''Programa que procura uma letra em uma frase e mostra quantas vezes a letra se repete,
a primeira posição em que a letra aparece e a ultima posição que a letra aparece'''

frase = str(input('Digite uma frase: ')).strip().upper()
print(frase.count('A'))
print(frase.find('A')+1)
print(frase.rfind('A')+1)

