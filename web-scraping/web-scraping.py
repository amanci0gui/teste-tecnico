from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import re
import os
from urllib.parse import urljoin, urlparse
import zipfile
from typing import List, Dict

# Configurações globais (podem ser movidas para um arquivo separado)
CONFIG = {
    "retry": {
        "total": 3,
        "status_forcelist": [500, 502, 503, 504],
        "backoff_factor": 1
    },
    "headers": {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Encoding': 'gzip, deflate'
    },
    "timeouts": {
        "page_request": 10,
        "file_download": 60
    }
}

def create_http_session(config: Dict) -> requests.Session:
    """Cria e configura sessão HTTP com política de retentativas"""
    session = requests.Session()
    retry = Retry(**config["retry"])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    return session

def fetch_page_content(session: requests.Session, url: str) -> BeautifulSoup:
    """Obtém e parseia o conteúdo HTML da página"""
    try:
        response = session.get(url, headers=CONFIG["headers"], timeout=CONFIG["timeouts"]["page_request"])
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Falha ao obter página: {str(e)}")

def extract_pdf_links(soup: BeautifulSoup, base_url: str) -> List[str]:
    """Extrai links de PDFs de acordo com o padrão especificado"""
    anexo_pattern = re.compile(r'Anexo[\s_-]*I+', re.IGNORECASE)
    pdf_links = []
    
    for anchor in soup.find_all('a'): #Pega cada link de cada <a> na página
        href = anchor.get('href', '')
        full_url = urljoin(base_url, href)
        
        if full_url.lower().endswith('.pdf') and anexo_pattern.search(full_url): #verifica se é um arquivo que segue o regex e é um pdf
            pdf_links.append(full_url)
    
    return pdf_links

def download_pdf(session: requests.Session, url: str, output_dir: str = ".") -> str:
    """Faz download de um arquivo PDF com verificação de integridade"""
    filename = os.path.join(output_dir, os.path.basename(urlparse(url).path))
    
    try:
        with session.get(url, stream=True, timeout=CONFIG["timeouts"]["file_download"]) as response:
            response.raise_for_status()
            
            file_size = int(response.headers.get('Content-Length', 0))
            downloaded = 0
            
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
            
            if file_size > 0 and downloaded != file_size:
                raise IOError(f"Download incompleto: {downloaded}/{file_size} bytes")
                
        return filename
    
    except Exception as e:
        if os.path.exists(filename):
            os.remove(filename)
        raise RuntimeError(f"Falha no download de {url}: {str(e)}")

def create_zip_archive(files: List[str], zip_name: str) -> None:
    """Cria arquivo ZIP com os arquivos baixados"""
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for file in files:
                zipf.write(file, os.path.basename(file))
        print(f"Arquivo {zip_name} criado com {len(files)} arquivos")
    except Exception as e:
        raise RuntimeError(f"Falha ao criar ZIP: {str(e)}")

def main():
    try:
        # 1. Configuração inicial
        session = create_http_session(CONFIG)
        
        # 2. Obter conteúdo da página
        soup = fetch_page_content(session, 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
        
        # 3. Extrair links relevantes
        pdf_urls = extract_pdf_links(soup, 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
        
        if not pdf_urls:
            raise RuntimeError("Nenhum link de PDF encontrado")
        
        # 4. Fazer downloads
        downloaded_files = []
        for url in pdf_urls:
            try:
                file_path = download_pdf(session, url)
                downloaded_files.append(file_path)
                print(f"Download concluído: {os.path.basename(file_path)}")
            except RuntimeError as e:
                print(f"Erro: {str(e)}")
                continue
        
        # 5. Compactar resultados
        if downloaded_files:
            create_zip_archive(downloaded_files, "Anexos_ANS.zip")
        
        # 6. Limpeza opcional
        for file in downloaded_files:
            os.remove(file)
            
    except Exception as e:
        print(f"Erro no processo principal: {str(e)}")
    finally:
        session.close()

if __name__ == "__main__":
    main()