# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e
# do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o
# comprimento da hipotenusa.
import math

co = int(input('Cateto Oposto: '))
ca = int(input('Cateto Adjacente: '))

c1 = co ** 2
c2 = ca ** 2

re = c1 ++ c2
ra = math.sqrt(re)

print(f'Os Catetos {c1} e {c2} tem o cumprimento da hipotenusa {ra:.2f}')