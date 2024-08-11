from Funcionario import Funcionario

class Vendedor(Funcionario):

    def __init__(self, nome, matricula, salarioBase, comissao):
        super().setMatricula(matricula)
        super().setNome(nome)
        super().setSalarioBase(salarioBase)
        self.__comissao = comissao

    def calcularSalario(self):
        return ((super().getSalarioBase() * self.__comissao) / 100) + super().getSalarioBase()

    def __str__(self):
        return f"Salário atualizado do Vendedor: R$ {self.calcularSalario():,.2f}\n"