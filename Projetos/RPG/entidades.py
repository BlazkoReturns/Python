import random

class Entidade:
    def __init__(self,nome,vida,forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, alvo, nome):
        dano = (self.forca + (1.1*self.forca if random.randint(1,10) > 7 else 0))
        alvo -= dano
        print(f"{self.nome} bateu {dano} de dano. {nome} esta com {alvo} pontos de vida.")
        return alvo 

    def esta_vivo(self):
        if self.vida > 0:
            return True
        else:
            return False

class Heroi(Entidade):

    def __init__(self, nome, vida, forca):
        super().__init__(nome,vida,forca)
    
    def atacar(self,alvo,nome):
        dano = (self.forca + (1.5*self.forca if random.randint(1,100) <= 25 else 0)) 
        alvo -= dano
        print(f"{self.nome} bateu {dano} de dano. {nome} esta com {alvo} pontos de vida.")  
        return alvo

    def __str__(self):
        return f"{self.nome}: HP - {self.vida}, Força - {self.forca}"

    def to_dict(self):
       return {"nome":self.nome,"vida":self.vida,"forca":self.forca} 
       
class Monstro(Entidade):

    def __init__(self,nome, vida, forca):
        super().__init__(nome,vida,forca)

    def __str__(self):
        return f"{self.nome}: HP - {self.vida}, Força - {self.forca}"

