
#Exercício utilizando enumerate()
pilotos = ["Verstappen", "Perez", "Leclerc", "Sainz", "Hamilton"]
for posicao, piloto in enumerate(pilotos):
    print(f"{posicao+1}º lugar: {piloto}")
print("--------------------------------------------------------\n\n")

#Exercício utilizando zip()
produtos = ["Notebook", "Mouse sem fio", "Teclado Mecânico", "Monitor 4K"]
precos = [5000.00, 150.00, 350.00, 1800.00]    
nPrecoTotal = 0

print("--- Recibo da Compra ---")
for produto, preco in zip(produtos, precos):
    print(f"O produto {produto} custa R$ {preco}")
    nPrecoTotal += preco
print("------------------------")
print(f"Total da compra: R$ {nPrecoTotal}")

#Exercício utilizando .items()
print("--------------------------------------------------------\n\n")
votos = {"Windows": 1200,"Linux": 950,"MacOS": 780,"Outros": 120}
nVotos = 0
cSistema = ""

for sistema, voto in votos.items():
    if  voto >= nVotos:
        nVotos = voto
        cSistema = sistema
print(f"O sistema vencedor foi o {cSistema}!")        