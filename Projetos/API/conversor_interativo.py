import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        taxas = dados['rates']
        data_da_cotacao = dados['date']
        
        cotacao_real = taxas['BRL']
        cotacao_euro = taxas['EUR']
        
        print(f"--- Cotaçoes do dia {data_da_cotacao} ---")
        print(f"Dólar para Real Brasileiro (BRL): R$ {cotacao_real:.2f}")
        print(f"Dólar para Euro (EUR): E {cotacao_euro:.2f}")
        
    else:
        print(f"Erro ao buscar dados. Código de status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}")

while True:
   dolars = int(input("Qual quantia em dolars quer converter ?"))
   moeda = input("Deseja converter para qual moeda ?").upper()
   cotacao_moeda = taxas[moeda]
   conversao = dolars*cotacao_moeda
   print(f" US$ {dolars:.2f} equivalem a {conversao:.2f} {moeda}")
