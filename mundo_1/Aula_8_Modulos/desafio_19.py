# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.

from random import choice

alunos = ['Maria', 'João', 'Paulo', 'Mario']
sorteado = choice(alunos)
print(f'O Aluno escolhido foi, {sorteado}')