import uuid


class Voo:
    def __init__(self,assento, local_partida, local_destino,qtd_funcionarios, funcionarios, preco_passagem):
        self._id_voo = uuid.uuid4() 
        self.__numero_assentos = 250
        self.__info_assento = assento           
        self.__local_partida = local_partida                 
        self.__local_destino = local_destino                  
        self.__numero_funcionarios = qtd_funcionarios 
        self.__funcionarios = funcionarios
        self.__preco_passagem = preco_passagem

    @property
    def id_voo(self):
        return self._id_voo

    @id_voo.setter
    def id_voo(self, value):
        self._id_voo = value

    @property
    def _numero_assentos(self):
        return self.__numero_assentos

    @_numero_assentos.setter
    def _numero_assentos(self, value):
        self.__numero_assentos = value

    @property
    def _info_assento(self):
        return self.__info_assento

    @_info_assento.setter
    def _info_assento(self, value):
        self.__info_assento = value

    @property
    def _local_partida(self):
        return self.__local_partida

    @_local_partida.setter
    def _local_partida(self, value):
        self.__local_partida = value

    @property
    def _local_destino(self):
        return self.__local_destino

    @_local_destino.setter
    def _local_destino(self, value):
        self.__local_destino = value

    @property
    def _numero_funcionarios(self):
        return self.__numero_funcionarios

    @_numero_funcionarios.setter
    def _numero_funcionarios(self, value):
        self.__numero_funcionarios = value

    @property
    def _funcionarios(self):
        return self.__funcionarios

    @_funcionarios.setter
    def _funcionarios(self, value):
        self.__funcionarios = value

    @property
    def _preco_passagem(self):
        return self.__preco_passagem

    @_preco_passagem.setter
    def _preco_passagem(self, value):
        self.__preco_passagem = value


    


   

        

