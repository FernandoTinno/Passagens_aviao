import random
from faker import Faker
from usuario import Passageiro, Piloto, Copiloto, Comissaria 
from validacao import validar_demanda_voo_passageiro 
from assento import Assento
from voo import Voo

def gerar_lista_de_passageiros(quantidade):
    fake = Faker('pt_BR')
    passageiros = []
    cpfs_usados = set()
    nomes_usados = set()

    while len(passageiros) < quantidade:
        nome = fake.name()
        cpf = fake.cpf()
        if cpf not in cpfs_usados and nome not in nomes_usados:
            cpfs_usados.add(cpf)
            nomes_usados.add(nome)
            novo_passageiro = Passageiro(nome, cpf)
            passageiros.append(novo_passageiro)
    return passageiros

def gerar_funcionarios_por_demanda(quantidade_voos):
    nomes_usados = set()
    cpfs_usados = set()
    voos_funcionarios = []
    fake = Faker('pt_BR')

    for _ in range(quantidade_voos):
        grupo_voo = []
        while True:
            nome = fake.name()
            cpf = fake.cpf()
            if nome not in nomes_usados and cpf not in cpfs_usados:
                piloto = Piloto(nome, cpf)
                nomes_usados.add(nome)
                cpfs_usados.add(cpf)
                grupo_voo.append(piloto)
                break
        
        num_copilotos = random.randint(1, 3)
        for _ in range(num_copilotos):
            while True:
                nome = fake.name()
                cpf = fake.cpf()
                if nome not in nomes_usados and cpf not in cpfs_usados:
                    copiloto = Copiloto(nome, cpf)
                    nomes_usados.add(nome)
                    cpfs_usados.add(cpf)
                    grupo_voo.append(copiloto)
                    break

        num_comissarias = random.randint(5, 10)
        for _ in range(num_comissarias):
            while True:
                nome = fake.name()
                cpf = fake.cpf()
                if nome not in nomes_usados and cpf not in cpfs_usados:
                    comissaria = Comissaria(nome, cpf)
                    nomes_usados.add(nome)
                    cpfs_usados.add(cpf)
                    grupo_voo.append(comissaria)
                    break
        
        voos_funcionarios.append(grupo_voo)
    return voos_funcionarios

def gerar_assentos_voos(quantidade_voos):
    assentos_voos = []
    for _ in range(quantidade_voos):
        assento = Assento()
        assento.gerar_assentos()
        assentos_voos.append(assento)
    return assentos_voos

def alocar_passageiros_em_assentos(assentos_voos, passageiros):
    num_voos = len(assentos_voos)
    if num_voos == 0:
        return assentos_voos

    for i, passageiro in enumerate(passageiros):
        indice_voo = i % num_voos
        assentos_voos[indice_voo].ocupar_proximo_assento_livre(passageiro)
        
    return assentos_voos

def gerar_voos(assentos_voos, voos_funcionarios, quantidade_voos):
    voos = []
    cidades = [
        'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Salvador',
        'Curitiba', 'Fortaleza', 'Recife', 'Porto Alegre', 'Manaus'
    ]
    precos_possiveis = [500, 550, 600, 650, 700]
    combinacoes_usadas = set()

    while len(combinacoes_usadas) < quantidade_voos:
        partida = random.choice(cidades)
        destino = random.choice(cidades)
        if partida != destino:
            combinacao = (partida, destino)
            if combinacao not in combinacoes_usadas:
                combinacoes_usadas.add(combinacao)
    
    combinacoes_escolhidas = list(combinacoes_usadas)

    for i in range(quantidade_voos):
        partida, destino = combinacoes_escolhidas[i]
        preco = random.choice(precos_possiveis)
        voo = Voo(
            assento=assentos_voos[i],
            local_partida=partida,
            local_destino=destino,
            qtd_funcionarios=len(voos_funcionarios[i]),
            funcionarios=voos_funcionarios[i],
            preco_passagem=preco
        )
        voos.append(voo)
    return voos

def gerar_voos_completo(quantidade_voos, total_passageiros):
    validar_demanda_voo_passageiro(quantidade_voos, total_passageiros)
    passageiros = gerar_lista_de_passageiros(total_passageiros)
    voos_funcionarios = gerar_funcionarios_por_demanda(quantidade_voos)
    assentos_voos_vazios = gerar_assentos_voos(quantidade_voos)
    assentos_voos_ocupados = alocar_passageiros_em_assentos(assentos_voos_vazios, passageiros)  
    voos = gerar_voos(assentos_voos_ocupados, voos_funcionarios, quantidade_voos)
    
    return voos
