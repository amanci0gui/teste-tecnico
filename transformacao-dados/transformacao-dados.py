import pandas as pd
import requests
import tabula
import os 
import zipfile


def pdf_para_dataframe(url):
    # Faz download do PDF a partir da URL
    response = requests.get(url)
    with open("temporario.pdf", "wb") as f:
        f.write(response.content)

    # Usa a lib tabula para extrair as tabelas do arquivo
    tabelas = tabula.read_pdf("temporario.pdf", pages='3-181', encoding='ISO-8859-1', multiple_tables=True)
    dataframe_combinado = pd.DataFrame()

    # Definindo as colunas esperadas
    colunas_esperadas = ['PROCEDIMENTO', 'RN (alteração)', 'VIGÊNCIA', 'SEG. ODONTOLÓGICA', 'SEG.AMBULATORIAL', 'HCO', 'HSO', 'REF', 'PAC', 'DUT', 'SUBGRUPO', 'GRUPO', 'CAPITULO']

    for tabela in tabelas:
        df = tabela.copy()

        # Verifica o número de colunas e ajusta se necessário
        if len(df.columns) != len(colunas_esperadas):
            # print(f"Warning: Número de colunas diferente de 13. Detectadas {len(df.columns)} colunas.")
            if len(df.columns) > len(colunas_esperadas):
                df = df.iloc[:, :len(colunas_esperadas)]  # Mantém apenas as 13 primeiras colunas
            elif len(df.columns) < len(colunas_esperadas):
                # Caso tenha menos de 13 colunas, podemos adicionar colunas vazias para evitar erro
                missing_columns = len(colunas_esperadas) - len(df.columns)
                for i in range(missing_columns):
                    df[f'COLUNA_ADICIONAL_{i+1}'] = ''
        
        # Renomeia as colunas corretamente
        df.columns = colunas_esperadas
        dataframe_combinado = pd.concat([dataframe_combinado, df], ignore_index=True)
    
    dataframe_combinado = dataframe_combinado.fillna('') #substitui os NaaN por espaços em branco
    dataframe_combinado = dataframe_combinado.applymap(lambda x: x.strip() if isinstance(x, str) else x) #se for uma string ele remove os espaços em branco

    for col in dataframe_combinado.select_dtypes(include=['object']).columns:
        dataframe_combinado[col] = dataframe_combinado[col].str.replace(r'\bOD\b', 'Seg. Odontológica', regex=True)
        dataframe_combinado[col] = dataframe_combinado[col].str.replace(r'\bAMB\b', 'Seg. Ambulatorial', regex=True)


    return dataframe_combinado


def dataframe_para_csv(dataframe_final):
    csv_filename = "dados_extraidos.csv"
    # Salva o CSV usando o delimitador ";" e a codificação "utf-8-sig" (para melhor compatibilidade com caracteres especiais)
    dataframe_final.to_csv(csv_filename, index=False, encoding="utf-8-sig", sep=';')
    return csv_filename

def compacta_csv(csv_filename, zip_filename):
    # Cria um arquivo ZIP e adiciona o CSV nele
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename)
        
if __name__ == '__main__':
    url_pdf = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
    
    # Converte o PDF para DataFrame
    dataframe_final = pdf_para_dataframe(url_pdf)
    
    # Salva o DataFrame como CSV
    csv_filename = dataframe_para_csv(dataframe_final)
    
    # Exclui o arquivo PDF temporário
    if os.path.exists("temporario.pdf"):
        os.remove("temporario.pdf")
    
    # Compacta o arquivo CSV em um ZIP
    zip_filename = "Teste_GuilhermeAmancio.zip"
    compacta_csv(csv_filename, zip_filename)

    if os.path.exists("dados_extraidos.csv"):
        os.remove("dados_extraidos.csv")
    
    print("Processo concluído com sucesso!")
