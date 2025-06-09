"""
Configuração do pytest para os testes.
"""
import pytest
import cv2
import numpy as np


@pytest.fixture
def frame_teste():
    """
    Fixture que retorna um frame de teste.
    
    Returns:
        np.ndarray: Frame de teste com um objeto em movimento
    """
    # Cria um frame vazio
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    
    # Adiciona um objeto em movimento (retângulo)
    cv2.rectangle(frame, (200, 200), (400, 400), (0, 255, 0), -1)
    
    return frame


@pytest.fixture
def mascara_teste():
    """
    Fixture que retorna uma máscara de teste.
    
    Returns:
        np.ndarray: Máscara binária de teste
    """
    # Cria uma máscara vazia
    mascara = np.zeros((480, 640), dtype=np.uint8)
    
    # Adiciona um objeto (retângulo)
    cv2.rectangle(mascara, (200, 200), (400, 400), 255, -1)
    
    return mascara 