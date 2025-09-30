import os

def titulo():
    print("\n****************************************")
    print("*              Mini RPG 1.0            *")
    print("****************************************\n")

def menu_acoes():
    print("1.Avançar Norte")
    print("2.Avançar Leste")
    print("3.Avançar Sul")
    print("4.Avançar Oeste\n")
    print("5.Ver Status")
    print("6.Ver Itens")
    print("7.Abrir bau\n")

def limpar_tela():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear') 
