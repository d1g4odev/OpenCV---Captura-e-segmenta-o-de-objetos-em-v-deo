"""
Testes unitários para a classe ProcessadorVideo.
"""
import pytest
import cv2
import numpy as np
from video_processor import ProcessadorVideo


def test_inicializacao_camera():
    """Testa a inicialização do processador com câmera."""
    processador = ProcessadorVideo(
        fonte='camera',
        algoritmo='MOG2'
    )
    assert processador.fonte == 'camera'
    assert processador.algoritmo == 'MOG2'
    assert processador.cap is not None
    assert processador.cap.isOpened()


def test_inicializacao_arquivo():
    """Testa a inicialização do processador com arquivo."""
    # Cria um vídeo de teste
    video_path = 'test_video.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))
    
    # Adiciona alguns frames
    for _ in range(10):
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        out.write(frame)
    out.release()
    
    try:
        processador = ProcessadorVideo(
            fonte='arquivo',
            algoritmo='MOG2',
            arquivo=video_path
        )
        assert processador.fonte == 'arquivo'
        assert processador.algoritmo == 'MOG2'
        assert processador.arquivo == video_path
        assert processador.cap is not None
        assert processador.cap.isOpened()
    finally:
        # Limpa o arquivo de teste
        import os
        if os.path.exists(video_path):
            os.remove(video_path)


def test_inicializacao_arquivo_invalido():
    """Testa a inicialização com arquivo inválido."""
    with pytest.raises(ValueError):
        ProcessadorVideo(
            fonte='arquivo',
            algoritmo='MOG2'
        )


def test_inicializacao_fonte_invalida():
    """Testa a inicialização com fonte inválida."""
    with pytest.raises(ValueError):
        ProcessadorVideo(
            fonte='invalida',
            algoritmo='MOG2'
        ) 