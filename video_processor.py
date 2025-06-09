"""
Módulo contendo a classe principal para processamento de vídeo.
"""
from typing import Optional, Tuple
import cv2
import numpy as np
from utils import criar_subtrador, criar_janelas, processar_frame


class ProcessadorVideo:
    """
    Classe responsável pelo processamento de vídeo e segmentação de objetos em movimento.
    """
    
    def __init__(
        self,
        fonte: str,
        algoritmo: str,
        arquivo: Optional[str] = None,
        history: int = 500,
        detect_shadows: bool = True
    ):
        """
        Inicializa o processador de vídeo.

        Args:
            fonte: Fonte do vídeo ('camera' ou 'arquivo')
            algoritmo: Algoritmo de segmentação ('MOG', 'MOG2', 'GMG', 'KNN')
            arquivo: Caminho do arquivo de vídeo (necessário apenas se fonte='arquivo')
            history: Tamanho do histórico para o algoritmo
            detect_shadows: Se deve detectar sombras
        """
        print(f"[DEBUG] Fonte: {fonte}, Algoritmo: {algoritmo}, Arquivo: {arquivo}")
        self.fonte = fonte
        self.algoritmo = algoritmo
        self.arquivo = arquivo
        self.history = history
        self.detect_shadows = detect_shadows
        
        # Inicializa a captura de vídeo
        if fonte == 'camera':
            self.cap = cv2.VideoCapture(0)
        else:
            if not arquivo:
                raise ValueError("Caminho do arquivo de vídeo é necessário quando fonte='arquivo'")
            self.cap = cv2.VideoCapture(arquivo)
        print(f"[DEBUG] self.cap.isOpened(): {self.cap.isOpened()}")
        
        if not self.cap.isOpened():
            raise RuntimeError("Não foi possível abrir a fonte de vídeo")
        
        # Cria o subtrador de fundo
        self.subtrador = criar_subtrador(algoritmo, history, detect_shadows)
        
        # Cria as janelas de exibição
        self.janelas = criar_janelas()
    
    def processar(self) -> None:
        """
        Processa o vídeo em tempo real, exibindo os resultados.
        """
        try:
            while True:
                ret, frame = self.cap.read()
                print(f"[DEBUG] Frame lido: {ret}")
                if not ret:
                    print("[DEBUG] Fim do vídeo, reiniciando...")
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue
                
                # Processa o frame
                background, mascara, frame_segmentado = processar_frame(frame, self.subtrador)
                
                # Exibe os resultados
                cv2.imshow(self.janelas[0], frame)
                cv2.imshow(self.janelas[1], background)
                cv2.imshow(self.janelas[2], mascara)
                cv2.imshow(self.janelas[3], frame_segmentado)
                
                # Verifica se o usuário pressionou 'q' para sair
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            # Libera os recursos
            self.cap.release()
            cv2.destroyAllWindows()
    
    def __del__(self):
        """
        Destrutor da classe, garante que os recursos sejam liberados.
        """
        if hasattr(self, 'cap'):
            self.cap.release()
        cv2.destroyAllWindows() 