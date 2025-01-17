# Crie um programa que leia o nome completo de uma pessoa:
nome = str(input('Nome: '))
# O nome com todas as letras maiúsculas
print(nome.upper())
# O nome com todas minúsculas
print(nome.lower())
# Quantas letras ao todo (sem considerar espaços)
print(len(nome) - nome.count(' '))
# Quantas letras tem o primeiro nome:
dividido = nome.split()
print(len(dividido[0]))