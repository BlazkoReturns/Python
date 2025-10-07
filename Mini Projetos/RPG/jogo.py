import funcoes
import sys
import time
import mapa
from entidades import Heroi

funcoes.titulo()

jogo_ativo = True
x = 0
y = 0

nome = input("\nDigite o nome de seu heroi:")
heroi = Heroi(nome,100,10) 

while jogo_ativo:
    try:
        descricao = mapa.mapa[(x,y)]["descricao"] 
        bonus = mapa.mapa[(x,y)]["bonus"]
        monstro =  mapa.mapa[(x,y)]["monstro"]
        vitoria = mapa.mapa[(x,y)]["vitoria"]
        
        if vitoria:
           print("Parabéns, você escapou.") 
           time.sleep(3)
           sys.exit() 

        print(f"\n{descricao}\n")
        
        if monstro:
           print(f"Existe um {monstro.nome} nesta sala. Tentar sair dela irá iniciar uma luta.\n")

        if bonus == "cura":
           print("A fonte curativa restaura sua saúde.")
           heroi.vida = 100
        elif bonus == "forca":
           print("Sua força aumenta em 10 pontos.")
           heroi.forca += 10
           mapa.mapa[(x,y)]["bonus"] = ""
        
        
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
        funcoes.limpar_tela() 
        heroi.mostrar_status()
        time.sleep(3)

    if monstro:     
       while heroi.esta_vivo() > 0 or monstro.esta_vivo() > 0:
           monstro.vida -= heroi.forca
           time.sleep(1)
           print(f"Herói bateu {heroi.forca} de dano. Inimigo com {monstro.vida} restante.")
           if not monstro.esta_vivo():
               print("Heroi venceu.")
               mapa.mapa
               mapa.mapa[(x_previo,y_previo)]["monstro"] = None #Monstro Morreu
               time.sleep(3)
               break
           heroi.vida -= monstro.forca
           time.sleep(1)
           print(f"Inimigo bateu {monstro.forca} de dano. Heroi com {heroi.vida} restante.")
           if not heroi.esta_vivo():
               print(f"Inimigo venceu. {heroi.nome} seu esforços serão lembrados.")
               sys.exit()
               break
