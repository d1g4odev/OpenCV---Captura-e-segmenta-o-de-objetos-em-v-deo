"""
Testes unitários para as funções utilitárias.
"""
import pytest
import cv2
import numpy as np
from utils import criar_subtrador, aplicar_morfologia


def test_criar_subtrador():
    """Testa a criação de diferentes subtradores de fundo."""
    # Testa criação de cada tipo de subtrador
    algoritmos = ['MOG', 'MOG2', 'GMG', 'KNN']
    for algoritmo in algoritmos:
        subtrador = criar_subtrador(algoritmo)
        assert subtrador is not None
    
    # Testa algoritmo inválido
    with pytest.raises(ValueError):
        criar_subtrador('INVALIDO')


def test_aplicar_morfologia():
    """Testa a aplicação de operações morfológicas."""
    # Cria uma máscara de teste com ruído
    mascara = np.zeros((100, 100), dtype=np.uint8)
    mascara[40:60, 40:60] = 255  # Quadrado central
    mascara[10:15, 10:15] = 255  # Ruído
    
    # Aplica morfologia
    mascara_processada = aplicar_morfologia(mascara)
    
    # Verifica se a máscara processada é binária
    assert np.all(np.logical_or(mascara_processada == 0, mascara_processada == 255))
    
    # Verifica se o ruído foi removido
    assert mascara_processada[10:15, 10:15].sum() == 0
    
    # Verifica se o objeto principal foi preservado
    assert mascara_processada[40:60, 40:60].sum() > 0 