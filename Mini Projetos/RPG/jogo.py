import mapa
import funcoes
import os 
from entidades import Heroi, Monstro

nome = input("\nDigite o nome de seu heroi:")
heroi = Heroi(nome,100,10,["Maça","Chave Enferrujada"])   

jogo_ativo = True
x = 0
y = 0

while jogo_ativo:
   try:
      os.system('cls')
      
      print(f"\n{mapa.mapa[(x,y)]["descricao"]}\n")
      monstro = mapa.mapa[(x,y)]["monstro"]
      
      if monstro:
         print(f"Existe um {monstro.nome} nesta sala. Tentar sair dela irá iniciar uma luta.\n")
      
      direcao = funcoes.acao_movimento()
      
      if monstro:
         funcoes.batalha(heroi,monstro)

      x += direcao[0]
      y += direcao[1]
     
   except KeyError: #Entra aqui caso escolha uma direção que não esta no mapa.
      print("A direção indicada não leva a lugar nenhum.")
      x -= direcao[0]
      y -= direcao[1]
