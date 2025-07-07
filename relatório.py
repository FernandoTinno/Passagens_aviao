import random
import time
def exibir_relatorio(voos):
    print('Aqui está o relatório de Voos:\n')
    time.sleep(1)
    for i, voo in enumerate(voos, 1):
        print(f"===== VOO {i} =====")
        print(f"ID: {voo.id_voo}")
        print(f"Origem: {voo._local_partida}")
        print(f"Destino: {voo._local_destino}")
        print(f"Preço da Passagem: R${voo._preco_passagem},00")
        print(f"Quantidade de Funcionários: {voo._numero_funcionarios}")
        print("Funcionários do Voo:\n")
        for funcionario in voo._funcionarios:
            print(f"  - Nome: {funcionario._nome}")
            print(f"    CPF: {funcionario._cpf}")
            print(f"    Cargo: {funcionario._cargo}")

        print("\n10 assentos e seus respectivos passageiros:\n")

        assentos = voo._info_assento._assentos
        ocupados = [codigo for codigo, passageiro in assentos.items() if passageiro]
        selecionados = random.sample(ocupados, 10)

        for codigo in selecionados:
            passageiro = assentos[codigo]
            print(f"{codigo} -> Nome: {passageiro._nome}, Cpf: {passageiro._cpf}")
        
        print("\n" + "=" * 40 + "\n")
        time.sleep(2)  
