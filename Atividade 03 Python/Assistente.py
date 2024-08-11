from Funcionario import Funcionario

class Assistente(Funcionario):

    def __init__(self, nome, matricula, salarioBase):
        super().setMatricula(matricula)
        super().setNome(nome)
        super().setSalarioBase(salarioBase)

    def calcularSalario(self):
        return super().getSalarioBase()

    def __str__(self):
        return f"Salário atualizado do Assistente: R$ {self.calcularSalario():,.2f}\n"