import requests
import os
import textwrap

def impressao_formatada(elementos={},refrao=False):
   for elemento in elementos:
      print(f"\n{elemento["referencia"]}")
      print(f"{elemento["refrao"] if refrao else elemento["titulo"]}\n") 
  
      elemento_formatado = textwrap.wrap(elemento["texto"], width=120)
      for linha in elemento_formatado:
          print(f"{linha}")
try:
   os.system('cls')
   
   response = requests.get("https://liturgia.up.railway.app/v2/",timeout=5)
   response.raise_for_status()
   dados = response.json()

   print(f"{dados["data"]}")
   print(f"{dados["liturgia"]}")
   
   impressao_formatada(dados["leituras"]["primeiraLeitura"])
   impressao_formatada(dados["leituras"]["salmo"],True)
   impressao_formatada(dados["leituras"]["segundaLeitura"])
   impressao_formatada(dados["leituras"]["evangelho"])

except requests.exceptions.HTTPError as erro_http:
    print(f"Erro de conexão: {erro_http}")
    print(f"Código de Status: {erro_http.response.status_code}")

except requests.exceptions.Timeout:
    print("A requisição demorou muito (TimeOut) e foi cancelada.")

except requests.exceptions.ConnectionError:
   print("Erro de conexão. Verifique sua conexão com a internet.")

except request.exceptions.RequestException as erro:
   print(f"Ocorreu um erro inesperado: {erro}")
