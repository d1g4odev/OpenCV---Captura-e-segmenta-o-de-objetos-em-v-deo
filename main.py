"""
Ponto de entrada da aplicação de segmentação de objetos em movimento.
"""
import argparse
import sys
from video_processor import ProcessadorVideo


def parse_args():
    """
    Processa os argumentos da linha de comando.

    Returns:
        Namespace contendo os argumentos processados
    """
    parser = argparse.ArgumentParser(
        description='Segmentação de objetos em movimento usando OpenCV'
    )
    
    parser.add_argument(
        '--fonte',
        type=str,
        choices=['camera', 'arquivo'],
        required=True,
        help='Fonte do vídeo (camera ou arquivo)'
    )
    
    parser.add_argument(
        '--algoritmo',
        type=str,
        choices=['MOG', 'MOG2', 'GMG', 'KNN'],
        required=True,
        help='Algoritmo de segmentação'
    )
    
    parser.add_argument(
        '--arquivo',
        type=str,
        help='Caminho do arquivo de vídeo (necessário apenas se fonte=arquivo)'
    )
    
    parser.add_argument(
        '--history',
        type=int,
        default=500,
        help='Tamanho do histórico para o algoritmo (padrão: 500)'
    )
    
    parser.add_argument(
        '--detect_shadows',
        type=bool,
        default=True,
        help='Detectar sombras (padrão: True)'
    )
    
    return parser.parse_args()


def main():
    """
    Função principal da aplicação.
    """
    print("Iniciando aplicação...")
    args = parse_args()
    print(f"Argumentos recebidos: {args}")
    
    try:
        print("Criando processador de vídeo...")
        # Cria e inicializa o processador de vídeo
        processador = ProcessadorVideo(
            fonte=args.fonte,
            algoritmo=args.algoritmo,
            arquivo=args.arquivo,
            history=args.history,
            detect_shadows=args.detect_shadows
        )
        
        print("Iniciando processamento...")
        # Inicia o processamento
        processador.processar()
        
    except Exception as e:
        print(f"Erro: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main()) 