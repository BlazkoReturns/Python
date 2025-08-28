nSaldo = 1000

while True:
   
   nOpcao = 0
   nTransacao = 0
   
   print("1.Depositar")
   print("2.Sacar")
   print("3.Saldo")
   print("4.Sair")
   
   try:
      nOpcao = int(input("Escolha a opção:"))
      if nOpcao == 1:
         nTransacao = int(input("Informe o valor depositado:"))
         nSaldo += nTransacao
         print(f"Saldo após deposito: {nSaldo}")
      elif nOpcao == 2:
         nTransacao = int(input("Informe o valor sacado:"))
         nSaldo -= nTransacao
         print(f"Saldo após o saque: {nSaldo}")
      elif nOpcao == 3:
         print(f"Saldo após o saque: {nSaldo}")
      elif nOpcao == 4:
         break
      else:
          print("Digite uma opçao válida.") 
   except ValueError:
      print("Digite números apenas.")
      
       


