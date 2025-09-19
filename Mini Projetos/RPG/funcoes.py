def titulo():
    print("\n****************************************")
    print("*              Mini RPG 1.0            *")
    print("****************************************\n")

def acao_movimento():
    print("1.Norte")
    print("2.Leste")
    print("3.Sul")
    print("4.Oeste")
    direcao = int(input("Qual direção deseja avançar ?"))
    
    if direcao == 1:
        x = 0
        y = 1
    elif direcao == 2:
        x = 1
        y = 0
    elif direcao == 3:
        x = 0
        y = -1
    else:
        x = -1
        y = 0

    return x,y