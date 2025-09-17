import random

class Heroi:

    nome = ""
    vida = 100
    forca = 5
    inventario = {"elmo":"","corpo":"","luvas":"","botas":"","esquerda":"","direita":"Espada Enferrujada"}

    def __init__(self, nome):
        self.nome = nome
        
    def atacar(self, alvo):
        alvo -= (self.forca + (1.1*self.forca if random.randint(1,10) > 9 else 0))
        return alvo,"Crítico" 

    def esta_vivo(self):
        if self.vida > 0:
            return True
        else:
            return False