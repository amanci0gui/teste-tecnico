use db_teste_intuitive;

SET NAMES utf8mb4;
LOAD DATA INFILE 'C:\\teste-programacao\\Relatorio_cadop.csv' 
INTO TABLE dados_operadoras 
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS 
(
    registro_ans, cnpj, razao_social, nome_fantasia, modalidade, 
    logradouro, numero, complemento, bairro, cidade, uf, cep, 
    ddd, telefone, fax, endereco_eletronico, representante, 
    cargo_representante, regiao_de_comercializacao, data_registro_ans
);

select * from dados_operadoras;

LOAD DATA INFILE 'C:\\teste-programacao\\demonstracoes-contabeis\\1T2023.csv'
INTO TABLE dados_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
    

LOAD DATA INFILE 'C:\\teste-programacao\\demonstracoes-contabeis\\2T2023.csv'
INTO TABLE dados_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
    

LOAD DATA INFILE 'C:\\teste-programacao\\demonstracoes-contabeis\\3T2023.csv'
INTO TABLE dados_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
    

SET NAMES utf8mb4;
LOAD DATA INFILE 'C:\\teste-programacao\\demonstracoes-contabeis\\4T2023.csv'
INTO TABLE dados_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    @data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = STR_TO_DATE(@data, '%d/%m/%Y'),
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
    
LOAD DATA INFILE 'C:\\teste-programacao\\demonstracoes-contabeis\\1T2024.csv'
INTO TABLE dados_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
  
LOAD DATA INFILE 'C:\\teste-programacao\\demonstracoes-contabeis\\2T2024.csv'
INTO TABLE dados_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
    

LOAD DATA INFILE 'C:\\teste-programacao\\demonstracoes-contabeis\\3T2024.csv'
INTO TABLE dados_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
    

LOAD DATA INFILE 'C:\\teste-programacao\\demonstracoes-contabeis\\4T2024.csv'
INTO TABLE dados_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');