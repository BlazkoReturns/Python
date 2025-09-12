import os
from classes import Transacao

def adicionar_transacao(lista_transacoes, tipo, descricao, valor):
    nova_transacao = Transacao(tipo,descricao,valor)
    lista_transacoes.append(nova_transacao)

def calcular_saldo(lista_transacoes):
    saldo = 0.0
    for transacao in lista_transacoes:
        if transacao.tipo == 'receita':
            saldo += transacao.valor
        elif transacao.tipo == 'despesa':
            saldo -= transacao.valor
    return saldo

def exibir_extrato(lista_transacoes):
    print("\n--- EXTRATO DETALHADO ---")
    if not lista_transacoes:
        print("Nenhuma transação registrada.")
        return

    for indice, transacao in enumerate(lista_transacoes, start=1):
        valor_formatado = f"R$ {transacao.valor:.2f}"
        print(f"{indice}. Tipo: {transacao.tipo:<8} | Descrição: {transacao.descricao:<20} | Valor: {valor_formatado}")

def salvar_transacoes(lista_transacoes, nome_arquivo="transacoes.csv"):
    with open(nome_arquivo, 'w') as f:
        for transacao in lista_transacoes:
            f.write(f"{transacao.tipo},{transacao.descricao},{transacao.valor}\n")

def carregar_transacoes(nome_arquivo="transacoes.csv"):
    lista_transacoes = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    campos = linha.split(",")
                    if len(campos) == 3:
                        lista_transacoes.append(Transacao(campos[0],campos[1],float(campos[2])))
    return lista_transacoes