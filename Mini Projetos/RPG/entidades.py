import random

class Heroi:

    def __init__(self, nome, vida, forca, inventario):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.inventario = inventario
    def atacar(self, alvo):
        alvo -= (self.forca + (1.1*self.forca if random.randint(1,10) > 9 else 0))
        return alvo 

    def esta_vivo(self):
        if self.vida > 0:
            return True
        else:
            return False
        
    def mostrar_status(self):
        print(f"{self.nome} está com {self.vida} pontos de vida. Possui {self.forca} de força.")
        print(f"Possui os seguinte itens no inventátio: {", ".join(self.inventario)}")

class Monstro:

    def __init__(self,nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, alvo):
        alvo -= (self.forca + (1.1*self.forca if random.randint(1,10) > 9 else 0))
        return alvo 

    def esta_vivo(self):
        if self.vida > 0:
            return True
        else:
            return False 
        

        