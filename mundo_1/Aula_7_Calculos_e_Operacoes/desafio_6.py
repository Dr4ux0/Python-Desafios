# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e
# sua raiz quadrada:
import math

n = int(input(': '))

d = n * 2
t = n * 3
r = math.sqrt(n)

print(f'''Numero: {n} 
Dobro: {d}
Triplo: {t}
Raiz: {r}''')