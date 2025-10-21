import requests
import os
import textwrap

url = "https://liturgia.up.railway.app/v2/"

try:
   os.system('cls')
   response = requests.get(url)
   
   if response.status_code == 200:
      
      dados = response.json()
      data = dados["data"]
      liturgia = dados["liturgia"]
      leituras = dados["leituras"]
      primeira_leitura = leituras["primeiraLeitura"] 
      salmos = leituras["salmo"]
      segunda_leitura = leituras["segundaLeitura"]
      evangelhos = leituras["evangelho"]

      print(f"{data}")
      print(f"{liturgia}")

      for leitura in primeira_leitura:
         print(f"\n{leitura["referencia"]}")
         print(f"{leitura["titulo"]}\n")

         leitura_formatada = textwrap.wrap(leitura["texto"], width=120)
         for linha in leitura_formatada:
            print(linha)
      
      for salmo in salmos:
         print(f"\n{salmo["referencia"]}")
         print(f"{salmo["refrao"]}\n")
         print(f"{salmo["texto"]}")
      
      for leitura in leituras["segundaLeitura"]:
         print(f"\n{leitura["referencia"]}")
         print(f"{leitura["titulo"]}\n")

         segunda_leitura_formatada = textwrap.wrap(leitura["texto"], width=120)
         for linha in segunda_leitura_formatada:
            print(linha)
      for evangelho in evangelhos:
         print(f"\n{evangelho["referencia"]}")
         print(f"{evangelho["titulo"]}\n")
         evangelho_formatado = textwrap.wrap(evangelho["texto"], width=120)
         for linha in evangelho_formatado:
            print(linha)
 

   else:
      print(f"Erro ao buscar dados. Código de status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}") 
