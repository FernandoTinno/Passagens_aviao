import uuid


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

    
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        self.__id_funcionario = uuid.uuid4()
        self.__cargo = cargo

    @property
    def _id_piloto(self):
        return self.__id_funcionario

    @_id_piloto.setter
    def _id_piloto(self, value):
        self.__id_funcionario = value

    @property
    def _cargo(self):
        return self.__cargo

    @_cargo.setter
    def _cargo(self, value):
        self.__cargo = value
        
    def __repr__(self):
        
        return f'Nome: {self._nome}, Cpf: {self._cpf}, Cargo: {self._cargo}'



    
    

    
        