from entidades import Monstro

monstros_disponiveis = {
    "Goblin": Monstro("Goblin Ladrão",50,5),  
    "Esqueleto": Monstro("Esqueleto Guerreiro",65,7),  
    "Orc": Monstro("Orc Bruto",80,9),
    "Troll": Monstro("Troll da Caverna",100,8),
    "Cavaleiro Sombrio": Monstro("Cavaleiro Sombrio",100,10)
}

mapa = {(0, 0):
         {"descricao": "Você está na entrada da masmorra. Uma tocha ilumina as paredes úmidas. Há um corredor ao norte.",
          "monstro": None,
          "saidas": {"norte": (0, 1)}},
        (0, 1): {
          "descricao": "Você está em um corredor estreito. Um Goblin feio te encara! Existem portas a sua esquerda e direita.",
          "monstro": monstros_disponiveis["Goblin"],
          "saidas": {"sul": (0, 0), "leste": (1, 1)}},
        (1, 1): {
          "descricao": "Você entra em uma cela. Existe um cadáver pendurado através de um lençol. Não há saidas nesta cela.",
          "monstro": None,
          "saidas": {"oeste": (0, 1)},
          "vitoria": True
}}