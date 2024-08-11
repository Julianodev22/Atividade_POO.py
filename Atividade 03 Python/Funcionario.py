from abc import ABC, abstractmethod

class Funcionario(ABC):
    
    def __init__(self, nome, matricula, salarioBase):
        self.__nome = nome
        self.__matricula = matricula
        self.__salarioBase = salarioBase

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getSalarioBase(self):
        return self.__salarioBase

    def setSalarioBase(self, salarioBase):
        self.__salarioBase = salarioBase

    @abstractmethod
    def calcularSalario(self):
        pass

    def __str__(self):
        return f"Nome: {self.__nome}\n Matrícula: {self.__matricula}\n Salário_Base: {self.__salarioBase}\n"

