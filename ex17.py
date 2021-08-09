# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

def main():
    alunos = []

    for i in range(1,5):
        aluno = input('Digite o nome do aluno: ')
        alunos.append(aluno)

    print(f'{alunos[random.randint(0,3)]} irá escrever no quadro!')

if __name__ == '__main__':
    main()