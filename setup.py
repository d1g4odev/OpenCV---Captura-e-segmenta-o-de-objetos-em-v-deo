"""
Script de setup para o projeto de segmentação de objetos em movimento.
"""
import os
import urllib.request
import sys

def download_video_teste():
    """
    Baixa o vídeo de teste do OpenCV.
    """
    # URL do vídeo de exemplo
    url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/vtest.avi"
    
    # Nome do arquivo local
    filename = "video_teste.avi"
    
    # Verifica se o vídeo já existe
    if os.path.exists(filename):
        print(f"Vídeo de teste já existe: {filename}")
        return
    
    print(f"Baixando vídeo de teste...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Vídeo baixado com sucesso: {filename}")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {str(e)}")
        sys.exit(1)

def setup():
    """
    Executa o setup do projeto.
    """
    print("Iniciando setup do projeto...")
    
    # Cria diretório para vídeos se não existir
    if not os.path.exists("videos"):
        os.makedirs("videos")
    
    # Baixa o vídeo de teste
    download_video_teste()
    
    print("Setup concluído com sucesso!")

if __name__ == "__main__":
    setup() 