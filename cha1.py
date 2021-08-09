#  Monte um sistema financeiro onde você tem que inserir o cadastro de novos funcionários, 
# a cada 3 funcionários inseridos, o salário de todos eles sobem 5%
# valor, de maneira incremental. Quando o sistema perceber que você inseriu 10 funcionários, 
# pausar o programa, e printar todos os funcionários, e sortear um funcionário
# para que esse seja premiado e receba o valor de 10% do seu salário de bônus.

import random

class Cadastro:
    def __init__(self):
        self._funcionarios = []

    @property
    def funcionarios(self):
        return self._funcionarios

    def add_funcionario(self, funcionario):
        self._funcionarios.append(funcionario)

    def analise(self):
        if len(self._funcionarios) == 10:
            return True

        if len(self._funcionarios) % 3 == 0:
            for funcionario in self.funcionarios:
                funcionario.salario = funcionario.salario + (funcionario.salario * 5 / 100)


class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        self._salario = value


def main():
    cadastro = Cadastro()

    while not cadastro.analise():
        nome_funcionario = input('Digite o nome do funcionário: ')
        salario_funcionario = float(input('Digite o salário do funcionário: '))
        funcionario = Funcionario(nome_funcionario, salario_funcionario)
        cadastro.add_funcionario(funcionario)

    print('---------------------------------')
    for funcionario in cadastro.funcionarios:
        print(f'Funcionario: {funcionario.nome}\nSalário: {funcionario.salario}')
    print('---------------------------------\n')

    sorteado = cadastro.funcionarios[random.randint(0,9)]
    salario_sorteado = sorteado.salario + (sorteado.salario * 10 / 100)
    sorteado.salario = salario_sorteado

    print('---------------------------------')
    print(f'O sorteado foi: {sorteado.nome}\nSeu salário aumentou para: {salario_sorteado}')
    print('---------------------------------')

    print('---------------------------------')
    for funcionario in cadastro.funcionarios:
        print(f'Funcionario: {funcionario.nome}\nSalário: {funcionario.salario}')
    print('---------------------------------')

if __name__ == '__main__':
    main()
