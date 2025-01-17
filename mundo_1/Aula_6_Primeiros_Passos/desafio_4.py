# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

n = input('Digite Algo: ')

if n and n.isnumeric():
    valor = 'Numero'
    i = 'O'
else:
    valor = 'String'
    i = 'A'
    tipo = 'Palavra'
    tamanho = len(n)

print(f'{i} {tipo} é {valor}, e contem {tamanho} de tamanho')

# nao consegui implementar a logica de se for numero