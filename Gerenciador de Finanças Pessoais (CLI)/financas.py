import operacoes

NOME_ARQUIVO = "transacoes.csv"
transacoes = operacoes.carregar_transacoes(NOME_ARQUIVO)

while True:
    print("\n--- GERENCIADOR DE FINANÇAS ---")
    print("1. Adicionar Transação")
    print("2. Ver Extrato e Saldo")
    print("3. Sair")

    try:
        opcao = int(input("\nSelecione a opção desejada: "))

        if opcao == 1:
            print("\n--- Nova Transação ---")
            tipo_input = input("Digite o tipo (1 para Receita, 2 para Despesa): ")
            
            if tipo_input == '1':
                tipo = 'receita'
            elif tipo_input == '2':
                tipo = 'despesa'
            else:
                print("Tipo inválido. Operação cancelada.")
                continue

            descricao = input("Descreva a transação: ")
            valor_str = input("Informe o valor da transação: ").replace(",", ".")
            valor = float(valor_str)

            operacoes.adicionar_transacao(transacoes, tipo, descricao, valor)
            print(">>> Transação adicionada com sucesso! <<<")

        elif opcao == 2:
            operacoes.exibir_extrato(transacoes)
            saldo_atual = operacoes.calcular_saldo(transacoes)
            print("---------------------------------")
            print(f"SALDO ATUAL: R$ {saldo_atual:.2f}")
            print("---------------------------------")
            
        elif opcao == 3:
            operacoes.salvar_transacoes(transacoes, NOME_ARQUIVO)
            print("Dados salvos. Saindo do programa. Até logo!")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma das opções do menu.")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")