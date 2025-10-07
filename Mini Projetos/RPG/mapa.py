from entidades import Monstro

monstros_disponiveis = {
    "Goblin": Monstro("Goblin Ladrão",50,5),   
    "Cavaleiro Sombrio": Monstro("Cavaleiro Sombrio",100,10)
}

mapa = {(0, 0):
         {"descricao": "Você está na entrada da masmorra. Uma tocha ilumina as paredes úmidas.",
          "monstro": None,
          "saidas": {"Norte"},
          "bonus":"nenhum",
          "vitoria":False},
        (0, 1): {
          "descricao": "Você está em um corredor estreito. Existem portas a sua esquerda e direita.",
          "monstro": monstros_disponiveis["Goblin"],
          "saidas": {"Sul","Leste","Oeste"},
          "bonus":"nenhum",
          "vitoria":False},
        (1, 1): {
          "descricao": "Você entra em uma cela. Existe um fonte curativa nesta sala.",
          "monstro": None,
          "saidas": {"Oeste"},
          "bonus":"cura",
          "vitoria":False},
        (-1,1): {
          "descricao": "Você entra em uma sala com uma janela da qual entra o sol. Esta visão lhe concede força.",
          "monstro": None,
          "saidas": {"Leste"},
          "bonus": "forca",
          "vitoria":False},
        (0,2): {
          "descricao": "Você entra em uma sala com um grande tapete vermelho. A próxima sala aparente reservar um grande openete.",
          "monstro": None,
          "saidas": {"Sul","Norte"},
          "bonus": "",
          "vitoria":True},
        (0,3): {
          "descricao": "Você entra em uma sala com um grande trono.",
          "monstro": monstros_disponiveis["Cavaleiro Sombrio"],
          "saidas": {"Norte"},
          "bonus": "nenhum",
          "vitoria":True},
       (0,4): {
          "descricao": "Você encontrou a saída desta masmorra.",
          "monstro": None,
          "saidas": {""},
          "bonus": "",
          "vitoria":True}
}
