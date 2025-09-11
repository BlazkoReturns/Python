import os

def adicionar_transacao(lista_transacoes, tipo, descricao, valor):
    lista_transacoes.append({"tipo":tipo,"descricao":descricao,"valor":valor})
    return lista_transacoes

def calcular_saldo(lista_transacoes):
    saldo = 0

    for transacao in lista_transacoes:
       if (transacao["tipo"]=="Receita"):
          saldo+= transacao["valor"]
       else:
          saldo-= transacao["valor"]

    return saldo

def exibir_extrato(lista_transacoes):
   
   for indice,transacao in enumerate(lista_transacoes):
      print(f"{indice+1}-Tipo: {transacao['tipo']} Descrição: {transacao['descricao']} Valor: {transacao['valor']}")
    
   return print(f"\nSeu saldo é {calcular_saldo(lista_transacoes)}")

def salvar_transacoes(lista_transacoes):
   with open('lista_transacoes.csv', 'w') as f:
      for transacao in lista_transacoes:
         f.write(f"{transacao['tipo']},{transacao['descricao']},{transacao['valor']}\n")

def carregar_transacoes():
   lista_transacoes = []
   if os.path.exists("lista_transacoes.csv"):
      with open("lista_transacoes.csv","r") as f:
         for linha in f:
            linha = linha.strip()
            linha = linha.split(",")
            for campo in linha:
               lista_transacoes.append({"Tipo":campo[0],"Descricao":campo[1],"Valor":campo[2]})
   return lista_transacoes
