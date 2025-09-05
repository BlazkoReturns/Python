import operacoes

transacoes = [
    {'tipo': 'receita', 'descricao': 'Salário', 'valor': 5000.00},
    {'tipo': 'despesa', 'descricao': 'Aluguel', 'valor': 1500.00},
    {'tipo': 'despesa', 'descricao': 'Internet', 'valor': 120.00}
]

while True:
    print("1.Adicionar Transação (Receita/Despesa)")
    print("2.Ver Extrato")
    print("3.Sair")

    try:
       nOpcao = int(input("\nSelecione a opção desejada:"))
       if nOpcao == 1:
           print("1.Receita")
           print("2.Despesa")
           nOpcao = int(input("Selecione a opção desejada:"))
           cDescricao = input("Descreva a transação:")
           nValor = float(input("Informe o valor da transação:").replace(",","."))
           
           transacoes = operacoes.adicionar_transacao(transacoes,"Receita" if nOpcao == 1 else "Despesa",cDescricao,nValor)
           print("Transação concluida.")
       elif nOpcao == 2:
           operacoes.exibir_extrato(transacoes)
       else:
           break    
    except ValueError:
        print("Digite uma das opções oferecidas.\n")