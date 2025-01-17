# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo.
/
from math import sin, cos, tan, radians

# Melhor maneira de importa para ''diminuir o uso de codigo''
# assim não será necessario usar math.sin, math.cos ... apenas sin(), cos()
# ao invesde import math

angulo = float(input('Digite o angulo: '))

sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print(f'O Angulo de {angulo}\nSENO: {sen:.2f}\nCOSSENO: {cos:.2f}\nTANGENTE: {tan:.2f}')
