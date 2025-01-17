# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada

numero = int(input('Numero: '))
for i in range(1, 10):
    numero * i
    result = numero * i
    print(f'{numero} * {i} = {result}')