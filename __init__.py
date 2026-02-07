"""Disk Analyzer - Analisador de Discos e Arquivos Grandes.

Um analisador profissional de discos para identificar e listar arquivos
grandes que ocupam espaço significativo no sistema.

Módulos:
    main: Ponto de entrada principal
    disk_analyzer: Função principal de análise
    infos: Funções de sistema e escaneamento
    generators: Geradores de relatórios

Usage:
    Como script:
        $ python main.py

    Como módulo:
        >>> from main import main
        >>> main()

    Importando funções específicas:
        >>> from disk_analyzer import analyzer
        >>> analyzer()

Author: Leandro Fernandes
Version: 1.0.0
Date: 2026-02-07
"""

__version__ = "1.0.0"
__author__ = "Leandro Fernandes"
__license__ = "MIT"

# Exportações principais
from analyzer.disk_analyzer import analyzer
from main import main

__all__ = ["main", "analyzer", "__version__", "__author__", "__license__"]
