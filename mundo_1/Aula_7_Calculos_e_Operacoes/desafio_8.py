# Escreva um programa que leia um valor em metros e o exiba convertido em
# centímetros e milímetros

m = float(input('Metro: '))
c = m / 100
mi = m / 1000

print(f'{m} em cm: {c}, em milimetro: {mi}')