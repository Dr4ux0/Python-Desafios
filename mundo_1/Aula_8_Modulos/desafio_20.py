# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import choice

alunos = ['João', 'Maria', 'Paulo', 'Alice']
for i in alunos:
    sorteados = choice(alunos)
    print(sorteados)
# error: os nomes são sorteados mais de uma vez