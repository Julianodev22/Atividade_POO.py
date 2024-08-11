from Funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self, nome, matricula, salarioBase):
        super().setMatricula(matricula)
        super().setNome(nome)
        super().setSalarioBase(salarioBase)

    def calcularSalario(self):
        return 2 * super().getSalarioBase()

    def __str__(self):
        return f"Salário atualizado do Gerente: R$ {self.calcularSalario():,.2f}\n"