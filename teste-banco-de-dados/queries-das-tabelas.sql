use db_teste_intuitive;

SELECT o.registro_ans, o.razao_social, SUM(dc.vl_saldo_final) AS total_despesas
FROM dados_contabeis dc
JOIN dados_operadoras o ON dc.reg_ans = o.registro_ans
WHERE dc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
  AND dc.data BETWEEN '2023-01-01' AND '2023-03-31'
GROUP BY o.registro_ans
ORDER BY total_despesas DESC
LIMIT 10;


SELECT 
    o.razao_social,
    o.registro_ans,
    SUM(d.vl_saldo_final) AS total_despesas
FROM 
    dados_contabeis d
JOIN 
    dados_operadoras o ON d.reg_ans = o.registro_ans
WHERE 
    d.descricao LIKE '%EVENTOS%' -- A descrição pode ter variações
    AND d.data BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND CURDATE() -- Últimos 12 meses
GROUP BY 
    o.registro_ans
ORDER BY 
    total_despesas DESC
LIMIT 10;


