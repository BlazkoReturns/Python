import os

def titulo():
    print("\n****************************************")
    print("*              Mini RPG 1.0            *")
    print("****************************************\n")

def menu_acoes():
    print("\n1.Avançar Norte")
    print("2.Avançar Oeste")
    print("3.Avançar Sul")
    print("4.Avançar Leste\n")
    print("5.Ver Status")

def limpar_tela():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear') 
