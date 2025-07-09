import random
import time

def exibir_relatorio(voos):
    print("Aqui está o relatório de Voos:\n")
    time.sleep(1)

    for i, voo in enumerate(voos, 1):
        print(f"====== VOO {i} ======")
        print(f"ID: {voo.id_voo}")
        print(f"Origem: {voo._local_partida}")
        print(f"Destino: {voo._local_destino}")
        print(f"Preço da Passagem: R${voo._preco_passagem},00")
        print(f"Quantidade de Funcionários: {voo._numero_funcionarios}")

        print("\nFuncionários do Voo:")
        for funcionario in voo._funcionarios:
            print(f"  - Nome: {funcionario._nome}")
            print(f"    CPF:  {funcionario._cpf}")
            print(f"    Cargo: {funcionario.obter_cargo()}")

        print("\nAmostra de assentos e seus respectivos passageiros:\n")

        assentos_do_voo = voo._info_assento._assentos
        ocupados = [codigo for codigo, passageiro in assentos_do_voo.items() if passageiro]

        if not ocupados:
            print(f"  No voo numero {i}, todos os assentos estão vazios.")
        else:
            todos_os_codigos = list(assentos_do_voo.keys())
            codigos_selecionados = random.sample(todos_os_codigos, 10)

            for codigo in codigos_selecionados:
                passageiro = assentos_do_voo[codigo]
                if passageiro:
                    print(f"  {codigo} -> Nome: {passageiro._nome}, Cpf: {passageiro._cpf}")
                else:
                    print(f"  {codigo} -> VAZIO")

        print("\n" + "-=" * 20 + "\n")
        time.sleep(2)
