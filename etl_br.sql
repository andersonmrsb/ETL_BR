CREATE TABLE etl_br(
cnpj VARCHAR (14) PRIMARY KEY,
uf CHAR(2) CHECK (uf ~ '^[A-Z]{2}$'),
cnae_fiscal INTEGER,
razao_social TEXT,
nome_fantasia text,
natureza_juridica TEXT,
cnae_fiscal_descricao TEXT,
data_inicio_atividade DATE,
descricao_situacao_cadastral TEXT
);

