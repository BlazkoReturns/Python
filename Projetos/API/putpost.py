import requests
import json 

url = "http://reqres.in/api/users"
header = {"x-api-key": "reqres-free-v1"}
try:

   while True:
      nome = input("Digite seu nome: \n")
      
      profissao = input("Digite sua profissão: \n")
      
      body = {"name":nome,"job":profissao}
      print(body)
      response = requests.post(url,json=body,headers=header)
   
      if response.status_code == 201:
         dados = response.json()
         print(dados)
      else:
         print(f"Erro ao buscar dados. Código de status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}") 
