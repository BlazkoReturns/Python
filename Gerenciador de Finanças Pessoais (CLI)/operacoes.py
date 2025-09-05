def adicionar_transacao(lista_transacoes, tipo, descricao, valor):
    lista_transacoes.append({"tipo":tipo,"descricao":descricao,"valor":valor})
    return lista_transacoes

def calcular_saldo(lista_transacoes):
    saldo = 0

    for transacao in lista_transacoes:
       if (transacao["tipo"]=="receita"):
          saldo+= transacao["valor"]
       else:
          saldo-= transacao["valor"]

    return saldo

def exibir_extrato(lista_transacoes):
   
   for indice,transacao in enumerate(lista_transacoes):
      print(f"{indice+1}-Tipo: {transacao['tipo']} Descrição: {transacao['descricao']} Valor: {transacao['valor']}")
    
   return print(f"\nSeu saldo é {calcular_saldo(lista_transacoes)}")  
