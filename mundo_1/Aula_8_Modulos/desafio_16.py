# Desafio 16: Crie um programa que leia um número real qualquer
# pelo teclado e mostre na tela a sua porção inteira.

import math

num = float(input('Digite um numero: '))
inteiro = math.trunc(num)

print(f'A porção inteira de {num} é {inteiro}')
