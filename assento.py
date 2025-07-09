class Assento:
    def __init__(self):
        self.__assentos = {}

    @property
    def _assentos(self):
        return self.__assentos

    @_assentos.setter
    def _assentos(self, value):
        self.__assentos = value


    
    def gerar_assentos(self):
        fileiras = 'ABCDEFGHIJ'
        for letra in fileiras:
            for numero in range(1, 26):
                codigo = f"{letra}{str(numero).zfill(2)}"
                self.__assentos[codigo] = None  

    def ocupar_proximo_assento_livre(self, passageiro):
        for codigo, ocupante in self._assentos.items():
            if ocupante is None:
                self._assentos[codigo] = passageiro
                return True
        return False

    def __repr__(self):
        resultado = ""
        for codigo, passageiro in self._assentos.items():
            if passageiro:
                resultado += f"{codigo} -> {passageiro}\n"
            else:
                resultado += f"{codigo} -> VAZIO\n"
        return resultado         
            
            
