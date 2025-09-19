import mapa
import funcoes
from entidades import Heroi, Monstro

nome = input("Digite o nome de seu heroi:")
heroi = Heroi(nome,100,10,["Maça","Chave Enferrujada"])   

jogo_ativo = True
x = 0
y = 0

while jogo_ativo:
   try:
      print(mapa.mapa[(x,y)]["descricao"])
      monstro = mapa.mapa[(x,y)]["monstro"]
      if monstro:
         print(f"Existe um {monstro.nome} nesta sala. Tentar sair dela irá iniciar uma luta.")

      direcao = funcoes.acao_movimento()
      x += direcao[0]
      y += direcao[1]
      
   except KeyError:
      print("A direção indicada não leva a lugar nenhum.")
      x -= direcao[0]
      y -= direcao[1]
