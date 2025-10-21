import os

def titulo():
    limpar_tela() 
    print("\n****************************************")
    print("*              Mini RPG 1.0            *")
    print("****************************************\n")

def menu_acoes():
    print("1.Avançar Norte")
    print("2.Avançar Oeste")
    print("3.Avançar Sul")
    print("4.Avançar Leste")
    print("5.Ver Status")
    print("6.Salvar Jogo")

def limpar_tela():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear') 
