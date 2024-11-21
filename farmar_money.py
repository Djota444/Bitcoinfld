import requests

def pegar_cotacao(moeda):
    url = f"https://api.exchangerate.host/latest?base={moeda}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        return dados["rates"]
    except Exception as e:
        print(f"Erro ao pegar cotação para {moeda}: {e}")
        return None

def exibir_cotacao(moeda):
    print(f"\n=== Cotações para {moeda.upper()} ===")
    taxas = pegar_cotacao(moeda)
    if taxas:
        print(f"Dólar (USD): {taxas.get('USD', 'N/A')}")
        print(f"Real (BRL): {taxas.get('BRL', 'N/A')}")
        print(f"Libra (GBP): {taxas.get('GBP', 'N/A')}")
    else:
        print("Não foi possível obter as cotações.")

def main():
    print("Escolha uma moeda base para pegar as cotações:")
    print("1. Dólar (USD)")
    print("2. Real (BRL)")
    print("3. Libra (GBP)")
    
    escolha = input("Digite o número da moeda desejada: ").strip()
    
    if escolha == "1":
        exibir_cotacao("USD")
    elif escolha == "2":
        exibir_cotacao("BRL")
    elif escolha == "3":
        exibir_cotacao("GBP")
    else:
        print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
