import random
from faker import Faker
from usuario import Passageiro, Funcionario
from assento import Assento
from voo import Voo
import time
import sys

def gerar_lista_de_passageiros(quantidade = 2500):
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


def dividir_passageiros_em_grupos(passageiros, tamanho_grupo=250):
    grupos_passageiros = [passageiros[i:i + tamanho_grupo] for i in range(0, len(passageiros), tamanho_grupo)]
    return grupos_passageiros


def gerar_funcionarios_por_demanda():
    nomes_usados = set()
    cpfs_usados = set()
    voos_funcionarios = []
    fake = Faker('pt_BR')

    for _ in range(10):  
        grupo_voo = []

        
        while True:
            nome = fake.name()
            cpf = fake.cpf()
            if nome not in nomes_usados and cpf not in cpfs_usados:
                piloto = Funcionario(nome, cpf, 'Piloto')
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
                    copiloto = Funcionario(nome, cpf, 'Copiloto')
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
                    comissaria = Funcionario(nome, cpf, 'Comissária')
                    nomes_usados.add(nome)
                    cpfs_usados.add(cpf)
                    grupo_voo.append(comissaria)
                    break

        voos_funcionarios.append(grupo_voo)

    return voos_funcionarios


def gerar_assentos_voos():
    assentos_voos = []
    for _ in range(10):
        assento = Assento()
        assento.gerar_assentos()  
        assentos_voos.append(assento)
    return assentos_voos


def alocar_passageiros_em_assentos(assentos_voos, grupos_passageiros):
    for i in range(10):
        assentos_voos[i].alocar_passageiros(grupos_passageiros[i])
    return assentos_voos


def gerar_voos(assentos_voos, voos_funcionarios):
    voos = []
    cidades = [
        'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Salvador',
        'Curitiba', 'Fortaleza', 'Recife', 'Porto Alegre', 'Manaus'
    ]

    precos_possiveis = [500, 550, 600, 650, 700]
    combinacoes_usadas = set()

    
    while len(combinacoes_usadas) < 10:
        partida = random.choice(cidades)
        destino = random.choice(cidades)

        if partida != destino:
            combinacao = (partida, destino)
            if combinacao not in combinacoes_usadas:
                combinacoes_usadas.add(combinacao)

    combinacoes_escolhidas = list(combinacoes_usadas)

    for i in range(10):
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


def gerar_voos_completo():
    passageiros = gerar_lista_de_passageiros()
    grupos_passageiros = dividir_passageiros_em_grupos(passageiros)
    funcionarios_voos = gerar_funcionarios_por_demanda()
    assentos_voos = gerar_assentos_voos()
    assentos_voos = alocar_passageiros_em_assentos(assentos_voos, grupos_passageiros)
    voos = gerar_voos(assentos_voos, funcionarios_voos)
    
    return voos




def animar_carregamento(mensagem, duracao):
    fim = time.time() + duracao
    pontos = ["", ".", "..", "..."]

    while time.time() < fim:
        for p in pontos:
            sys.stdout.write(f"\r{mensagem}{p}   ")  # sobrescreve a linha
            sys.stdout.flush()
            time.sleep(0.5)
