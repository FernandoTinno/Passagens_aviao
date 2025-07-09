from utils import gerar_voos_completo
from relatorio import exibir_relatorio
from exceptions import CapacidadeTotalExcedidaError
import sys
import time

if __name__ == "__main__":

    quantidade_de_voos = 10
    total_de_passageiros = 2500

    try:
        print("Iniciando o sistema de geração de voos")
        time.sleep(1.5)

        relatorio_de_voo = gerar_voos_completo(quantidade_de_voos, total_de_passageiros)

        print("\nGerando relatório")
        time.sleep(1.5)
        print("\n")
        exibir_relatorio(relatorio_de_voo)

    except CapacidadeTotalExcedidaError as e:
        print(f"\n{e}")
        print("O programa será encerrado.")
        sys.exit(1)
