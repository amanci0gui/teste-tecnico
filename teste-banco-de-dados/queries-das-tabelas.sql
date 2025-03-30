USE db_teste_intuitive;

SELECT 
	o.registro_ans, 
    o.razao_social, 
    dc.descricao, 
    SUM(dc.vl_saldo_final) AS total_despesas
FROM 
	dados_contabeis dc
JOIN 
	dados_operadoras o ON dc.reg_ans = o.registro_ans
WHERE 
	dc.descricao LIKE '%EVENTOS/ SINISTROS%'
	AND dc.data BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 MONTH) AND CURDATE() 
GROUP BY 
	o.registro_ans, dc.descricao, o.razao_social
ORDER BY 
	total_despesas DESC
LIMIT 10;



SELECT 
    o.razao_social,
    o.registro_ans,
    d.descricao,
    SUM(d.vl_saldo_final) AS total_despesas
FROM 
    dados_contabeis d
JOIN 
    dados_operadoras o ON d.reg_ans = o.registro_ans
WHERE 
    d.descricao LIKE '%EVENTOS/ SINISTROS%' 
    AND d.data BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND CURDATE() 
GROUP BY 
    o.registro_ans, d.descricao, o.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;


