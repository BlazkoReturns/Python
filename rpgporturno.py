import random
import time

nVidaHeroi = 100
nVidaInimigo = 80

while nVidaHeroi > 0 or nVidaInimigo > 0:
    nDano = random.randint(10,20)
    nVidaInimigo -= nDano
    time.sleep(1)
    print(f"Herói bateu {nDano} de dano. Inimigo com {nVidaInimigo} restante.")
    if nVidaInimigo <= 0:
        print("Heroi venceu.")
        break
    nDano = random.randint(5,15)
    nVidaHeroi -= nDano
    time.sleep(1)
    print(f"Inimigo bateu {nDano} de dano. Heroi com {nVidaHeroi} restante.")
    if nVidaHeroi <= 0:
        print("Inimigo venceu.")
        break

