from utils import gerar_voos_completo, animar_carregamento
from relatório import exibir_relatorio


if __name__ == "__main__":
    
    animar_carregamento("Iniciando o sistema de geração de voos", 2.5)
    print("\n")
    animar_carregamento("Gerando relatório", 2.5)
    print("\n")
relatorio_de_voo = gerar_voos_completo()
exibir_relatorio(relatorio_de_voo)