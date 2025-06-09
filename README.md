# Segmentação de Objetos em Movimento

Este projeto implementa um sistema de segmentação de objetos em movimento utilizando diferentes algoritmos de subtração de fundo disponíveis na biblioteca OpenCV.

## Requisitos

- Python 3.8 ou superior
- OpenCV 4.8.0 ou superior
- NumPy 1.24.0 ou superior
- Pytest 7.4.0 ou superior

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/d1g4odev/OpenCV---Captura-e-segmenta-o-de-objetos-em-v-deo.git
cd OpenCV---Captura-e-segmenta-o-de-objetos-em-v-deo
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o script de setup para baixar o vídeo de teste:
```bash
python setup.py
```

## Uso

Execute o programa principal com:

```bash
python main.py --fonte [camera|arquivo] --algoritmo [MOG|MOG2|GMG|KNN] --arquivo [caminho_do_video]
```

### Parâmetros

- `--fonte`: Fonte do vídeo (camera ou arquivo)
- `--algoritmo`: Algoritmo de segmentação (MOG, MOG2, GMG, KNN)
- `--arquivo`: Caminho do arquivo de vídeo (opcional, necessário apenas se fonte=arquivo)
- `--history`: Tamanho do histórico para o algoritmo (padrão: 500)
- `--detect_shadows`: Detectar sombras (True/False, padrão: True)

### Exemplos

1. Usando a webcam com MOG2:
```bash
python main.py --fonte camera --algoritmo MOG2
```

2. Processando o vídeo de teste com KNN:
```bash
python main.py --fonte arquivo --algoritmo KNN --arquivo video_teste.avi
```

## Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação
- `video_processor.py`: Implementação do processador de vídeo
- `utils.py`: Funções utilitárias
- `setup.py`: Script de configuração do projeto
- `tests/`: Diretório contendo testes unitários

## Testes

Execute os testes unitários com:

```bash
pytest tests/
```

## Contribuição

Este projeto foi desenvolvido como base para um artigo científico seguindo o padrão SBC. Contribuições são bem-vindas através de pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. 