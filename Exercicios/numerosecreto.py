import random

nNumeroSecreto = random.randint(1, 100)
nPalpite = 0


while nPalpite != nNumeroSecreto:
   nPalpite = int(input("Qual é o número secreto ?"))
   if nPalpite > nNumeroSecreto:
      print("Numero secreto é menor.")
   else:
      print("Número secreto é maior.")
print(f"Você acertou. O número secreto é {nNumeroSecreto}.")