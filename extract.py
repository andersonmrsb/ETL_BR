import requests

def extract_cnpj(cnpj: str) -> dict | None:
    
    # Função para consultar a BrasilAPI e retornar os dados de um CNPJ.
    # Parâmetros:
    #cnpj (str): Número do CNPJ (somente dígitos, com 14 caracteres).
    # Retorno:
    #dict: Dados do CNPJ em formato JSON, se encontrado.
    #None: Caso haja erro ou CNPJ inválido.
    
    
    # URL da API com o CNPJ
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    
    try:
        # Faz a requisição GET com timeout de 10 segundos
        response = requests.get(url, timeout=10)
        
        # Trata erros específicos
        if response.status_code == 404:
            print(f"CNPJ {cnpj} não encontrado.")
            return None
        elif response.status_code == 500:
            print(f"CNPJ {cnpj} inválido.")
            return None
        
        # Se houver outro erro HTTP, dispara exceção
        response.raise_for_status()
        
        # Confere se a resposta é JSON
        if response.headers.get("Content-Type", "").startswith("application/json"):
            return response.json()
        else:
            print("Resposta não está em formato JSON.")
            print(response.text)
            return None
    
    # Tratamento de exceções
    except requests.exceptions.Timeout:
        print(f"Timeout ao consultar o CNPJ {cnpj}.")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao consultar {cnpj}: {e}")
        return None


