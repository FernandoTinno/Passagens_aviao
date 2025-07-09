import uuid
from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    
class Passageiro(Pessoa):
    
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        
    def __repr__(self):
        return f'Nome: {self._nome}, Cpf: {self._cpf}'

    
class Funcionario(Pessoa, ABC):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.__id_funcionario = uuid.uuid4()

    @property
    def _id_funcionario(self):
        return self.__id_funcionario

    @_id_funcionario.setter
    def _id_funcionario(self, value):
        self.__id_funcionario = value

    @abstractmethod
    def obter_cargo(self):
        pass

    def __repr__(self):
        return f'{self.obter_cargo()}: {self.nome}, CPF: {self.cpf}'


class Piloto(Funcionario):
    def obter_cargo(self):
        return "Piloto"

class Copiloto(Funcionario):
    def obter_cargo(self):
        return "Copiloto"

class Comissaria(Funcionario):
    def obter_cargo(self):
        return "Comissária"  
        



    
    

    
        