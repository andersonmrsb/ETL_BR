from extract import extract_cnpj
from transform import transform_data
from connect_DB import load_cnpj, cursor, conn

def main():

    while True:

        cnpj = input("Digite o CNPJ: ")

        dados = extract_cnpj(cnpj)

        if not dados:
            print("CNPJ não encontrado.")
            continue  # Volta para o início do loop para solicitar outro CNPJ

        df = transform_data(dados)

        print("\n=== EMPRESA ENCONTRADA ===\n")

        print(df.to_string(index=False))
        processed_data = df.iloc[0].to_dict()  # Converte a primeira linha do DataFrame em dicionário

    load_cnpj(processed_data, cursor, conn)

