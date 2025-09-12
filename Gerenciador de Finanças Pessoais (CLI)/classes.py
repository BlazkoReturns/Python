class Transacao:
    def __init__(self, tipo, descricao, valor):
        print("Objeto Transacao está sendo criado...")
        
        self.tipo = tipo
        self.descricao = descricao
        self.valor = valor

    def exibir_detalhes(self):
        print(f"  Tipo: {self.tipo.capitalize():<8} | Descrição: {self.descricao:<20} | Valor: R$ {self.valor:.2f}")