import requests
import textwrap

url = "https://icanhazdadjoke.com/search"
headers = {"Accept":"application/json"}

try:

   while True:
      tema = input("Digite o tema da piada que quer ouvir. Digitar sair irá finalizar o programa.\n")
      
      if tema == "sair":
         break
 
      limite = int(input("Quantas piadas sobre este tema gostaria de ver?\n"))
      
      params = {"term":tema,"limit":limite}
      
      response = requests.get(url,headers=headers,params=params)
   
      if response.status_code == 200:
         dados = response.json()
         for index,piada in enumerate(dados["results"]):
            print(f"{index}. {piada["joke"]}\n")  		 
      else:
         print(f"Erro ao buscar dados. Código de status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}") 
