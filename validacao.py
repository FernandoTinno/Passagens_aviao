from exceptions import CapacidadeTotalExcedidaError

capacidade_por_voo = 250

def validar_demanda_voo_passageiro(quantidade_voos, total_passageiros):
    """
    Verifica se a quantidade de passageiros é compatível com a capacidade
    total dos voos. Lança uma exceção se a capacidade for excedida.
    """
    capacidade_maxima = quantidade_voos * capacidade_por_voo

    if total_passageiros > capacidade_maxima:
        raise CapacidadeTotalExcedidaError(total_passageiros, capacidade_maxima, quantidade_voos)
    print("Validação de capacidade OK.")