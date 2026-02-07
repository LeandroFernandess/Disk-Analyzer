"""Disk Analyzer - Ponto de Entrada Principal.

Este é o ponto de entrada principal para executar o Analisador de Discos.
Execute este script para iniciar a análise de discos e arquivos grandes.

Usage:
    $ python main.py
"""

import logging
import traceback

from analyzer.disk_analyzer import analyzer


# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Ponto de entrada principal do programa.

    Esta função é chamada quando o script é executado diretamente.
    Ela inicia o processo completo de análise de discos, incluindo:
    - Identificação de discos disponíveis
    - Seleção interativa pelo usuário
    - Escaneamento de arquivos grandes
    - Geração de relatórios TXT e CSV

    Raises:
        KeyboardInterrupt: Se o usuário cancelar com Ctrl+C
        Exception: Qualquer erro durante a execução

    Returns:
        None

    Example:
        Execute diretamente via terminal:
        >>> python main.py

    Note:
        Para melhor desempenho e acesso completo, execute como
        administrador no Windows ou com sudo no Linux/macOS.
    """
    try:
        analyzer()
    except KeyboardInterrupt:
        print("\n\n⚠ Operação cancelada pelo usuário.")
        logger.warning("Operação cancelada pelo usuário")
    except Exception as e:
        print(f"\n\n❌ Erro: {e}")
        logger.error(f"Erro durante a execução: {e}", exc_info=True)
        traceback.print_exc()


if __name__ == "__main__":
    main()
