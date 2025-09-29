import funcoes
import time
import mapa
from entidades import Heroi

funcoes.titulo()

jogo_ativo = True
x = 0
y = 0

nome = input("\nDigite o nome de seu heroi:")
heroi = Heroi(nome,100,10,["Maça","Chave Enferrujada"]) 

while jogo_ativo:
    try:
        print(f"\n{mapa.mapa[(x,y)]["descricao"]}\n")
        monstro =  mapa.mapa[(x,y)]["monstro"]        
        if monstro:
           print(f"Existe um {monstro.nome} nesta sala. Tentar sair dela irá iniciar uma luta.\n")
    except KeyError: #Entra aqui caso escolha uma direção que não esta no mapa.
        print("A direção indicada não leva a lugar nenhum.")
        x = x_previo
        y = y_previo     
        continue
 
    funcoes.menu_acoes()
    comando = int(input("Qual ação deseja realizar ?\n"))
    
    x_previo = x
    y_previo = y
 
    if comando == 1:  
        y+=1
    elif comando == 2:
        x+=1
    elif comando == 3:
        y-=1
    elif comando == 4:
        x-=1
    elif comando == 5:
        status()
    else:
        itens()
             
    if monstro:     
       while heroi.vida > 0 or monstro.vida > 0:
           monstro.vida -= heroi.forca
           time.sleep(1)
           print(f"Herói bateu {heroi.forca} de dano. Inimigo com {monstro.vida} restante.")
           if monstro.vida <= 0:
               print("Heroi venceu.")
               time.sleep(3)
               break
           heroi.vida -= monstro.forca
           time.sleep(1)
           print(f"Inimigo bateu {monstro.forca} de dano. Heroi com {heroi.vida} restante.")
           if heroi.vida <= 0:
               print(f"Inimigo venceu. {heroi.nome} seu esforços serão lembrados.")
               break
  
       
