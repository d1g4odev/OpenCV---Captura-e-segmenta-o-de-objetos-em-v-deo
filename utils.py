"""
Módulo contendo funções utilitárias para processamento de vídeo e segmentação.
"""
from typing import Tuple, Optional
import cv2
import numpy as np


def criar_subtrador(algoritmo: str, history: int = 500, detect_shadows: bool = True) -> cv2.BackgroundSubtractor:
    """
    Cria um objeto subtrador de fundo baseado no algoritmo especificado.

    Args:
        algoritmo: Nome do algoritmo ('MOG', 'MOG2', 'GMG', 'KNN')
        history: Tamanho do histórico para o algoritmo
        detect_shadows: Se deve detectar sombras

    Returns:
        Objeto subtrador de fundo

    Raises:
        ValueError: Se o algoritmo especificado não for suportado
    """
    algoritmos = {
        'MOG': cv2.bgsegm.createBackgroundSubtractorMOG,
        'MOG2': cv2.createBackgroundSubtractorMOG2,
        'GMG': cv2.bgsegm.createBackgroundSubtractorGMG,
        'KNN': cv2.createBackgroundSubtractorKNN
    }

    if algoritmo not in algoritmos:
        raise ValueError(f"Algoritmo '{algoritmo}' não suportado. Use um dos seguintes: {list(algoritmos.keys())}")

    if algoritmo == 'MOG':
        return algoritmos[algoritmo](history=history)
    elif algoritmo == 'MOG2':
        return algoritmos[algoritmo](history=history, detectShadows=detect_shadows)
    elif algoritmo == 'GMG':
        return algoritmos[algoritmo](initializationFrames=history)
    else:  # KNN
        return algoritmos[algoritmo](history=history, detectShadows=detect_shadows)


def aplicar_morfologia(mascara: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    """
    Aplica operações morfológicas para melhorar a máscara binária.

    Args:
        mascara: Máscara binária de entrada
        kernel_size: Tamanho do kernel para operações morfológicas

    Returns:
        Máscara binária processada
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    
    # Aplica abertura para remover ruídos
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
    
    # Aplica fechamento para preencher buracos
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
    
    return mascara


def criar_janelas() -> Tuple[str, str, str, str]:
    """
    Cria as janelas para exibição dos resultados.

    Returns:
        Tupla com os nomes das janelas
    """
    janelas = (
        'Vídeo Original',
        'Background Estimado',
        'Máscara Binária',
        'Vídeo Segmentado'
    )
    
    for janela in janelas:
        cv2.namedWindow(janela, cv2.WINDOW_NORMAL)
    
    return janelas


def processar_frame(frame: np.ndarray, subtrador: cv2.BackgroundSubtractor) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Processa um frame do vídeo aplicando a subtração de fundo.

    Args:
        frame: Frame do vídeo
        subtrador: Objeto subtrador de fundo

    Returns:
        Tupla contendo (background, máscara, frame_segmentado)
    """
    # Aplica a subtração de fundo
    mascara = subtrador.apply(frame)
    
    # Obtém o background estimado
    background = subtrador.getBackgroundImage()
    
    # Aplica operações morfológicas na máscara
    mascara = aplicar_morfologia(mascara)
    
    # Cria o frame segmentado
    frame_segmentado = cv2.bitwise_and(frame, frame, mask=mascara)
    
    return background, mascara, frame_segmentado 