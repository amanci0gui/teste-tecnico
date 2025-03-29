from fastapi import FastAPI, Query
import pandas as pd
from unidecode import unidecode

app = FastAPI()

def carregar_dados(caminho_csv: str):
    """Carrega os dados do CSV em um DataFrame."""
    return pd.read_csv(caminho_csv, dtype=str, delimiter=";", encoding='utf-8').fillna("")

df = carregar_dados("Relatorio_cadop.csv")

# Definir a rota de busca
@app.get("/buscar")
def buscar(cidade: str = None, uf: str = None, query: str = None):
    resultado = df
    
    # Normalizar as entradas para ignorar acentuação e maiúsculas/minúsculas
    if cidade:
        cidade_normalizada = unidecode(cidade).lower()
        resultado = resultado[resultado['Cidade'].apply(lambda x: cidade_normalizada in unidecode(x).lower())]
        
    if uf:
        uf_normalizado = unidecode(uf).lower()
        resultado = resultado[resultado['UF'].apply(lambda x: uf_normalizado in unidecode(x).lower())]
        
    if query:
        query_normalizado = unidecode(query).lower()
        resultado = resultado[resultado['Nome_Fantasia'].apply(lambda x: query_normalizado in unidecode(x).lower())]

    return resultado.to_dict(orient="records")