import psycopg2
import os

conn = psycopg2.connect(
    dbname="ETL_BR",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    host="localhost",
    port="5432"
)

cursor = conn.cursor()


def load_cnpj(dados: dict, cursor, conn):

    sql = """
    INSERT INTO etl_br (
        cnpj,
        uf,
        cnae_fiscal,
        razao_social,
        nome_fantasia,
        natureza_juridica,
        cnae_fiscal_descricao,
        data_inicio_atividade,
        descricao_situacao_cadastral
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (cnpj) DO NOTHING;
    """

    valores = (
        dados.get("cnpj"),
        dados.get("uf"),
        dados.get("cnae_fiscal"),
        dados.get("razao_social"),
        dados.get("nome_fantasia"),
        dados.get("natureza_juridica"),
        dados.get("cnae_fiscal_descricao"),
        dados.get("data_inicio_atividade"),
        dados.get("descricao_situacao_cadastral")
    )

    cursor.execute(sql, valores)
    conn.commit()

    print("Dados inseridos com sucesso!")
