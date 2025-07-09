

class ErroValidacao(Exception):
    """Classe base para erros de validação antes da geração dos voos."""
    pass

class CapacidadeTotalExcedidaError(ErroValidacao):
    """
    Exceção lançada quando o número total de passageiros solicitados
    excede a capacidade total de todos os voos combinados.
    """
    def __init__(self, total_passageiros, capacidade_maxima, quantidade_voos):
        mensagem = (
            f"\nERRO: Capacidade máxima excedida.\n"
            f"  - Passageiros solicitados: {total_passageiros}\n"
            f"  - Capacidade máxima para {quantidade_voos} voo(s): {capacidade_maxima} passageiros.\n"
            f"Por favor, ajuste a quantidade de passageiros ou aumente o número de voos."
        )
        super().__init__(mensagem)