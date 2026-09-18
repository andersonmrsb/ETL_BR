import pandas as pd


def transform_data(data: dict) -> pd.DataFrame:
    #Função para transformar os dados extraídos da API em um DataFrame limpo.
    #Parâmetros:
    #dados (dict): Dicionário retornado pela BrasilAPI.
    #Retorno:
    #pd.DataFrame: Dados tratados e prontos para carga no banco.
    
    # Cria DataFrame com os dados recebidos
    df = pd.DataFrame([data])

    df = df.fillna("Não se aplica")  # Preenche valores nulos com string vazia
    df = df.replace("", "Não se aplica")  # Substitui strings vazias por "Não se aplica"
    # Normaliza o CNPJ para sempre ter 14 dígitos
    df["cnpj"] = df["cnpj"].str.zfill(14)
    
    # Converte a data para formato datetime
    df["data_inicio_atividade"] = pd.to_datetime(
        df["data_inicio_atividade"], 
        errors="coerce"
    )
    
    # Remove duplicados pelo CNPJ
    df = df.drop_duplicates(subset=["cnpj"])
    
    # Seleciona apenas as colunas que interessam para o banco
    df = df[[
        "cnpj",
        "uf",
        "cnae_fiscal",
        "razao_social",
        "nome_fantasia",
        "natureza_juridica",
        "cnae_fiscal_descricao",
        "data_inicio_atividade",
        "descricao_situacao_cadastral"
    ]]
    
    return df