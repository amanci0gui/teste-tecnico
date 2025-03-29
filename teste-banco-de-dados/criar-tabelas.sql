create database db_teste_intuitive;

use db_teste_intuitive;

CREATE TABLE dados_contabeis (
	data DATE,
    reg_ans VARCHAR(20),
    cd_conta_contabil VARCHAR(20),
    descricao VARCHAR(255),
    vl_saldo_inicial  DOUBLE,
    vl_saldo_final DOUBLE
);

CREATE TABLE dados_operadoras (
	registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(255),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(50),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    uf VARCHAR(2),
    cep VARCHAR(9),
    ddd VARCHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(70),
    representante VARCHAR(70),
    cargo_representante VARCHAR(255),
    regiao_de_comercializacao VARCHAR(1),
    data_registro_ans DATE
);



