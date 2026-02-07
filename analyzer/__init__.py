"""Módulo Analyzer - Análise de Discos.

Este módulo contém a função principal de análise de discos e arquivos grandes.
É responsável por orquestrar todo o fluxo de análise, desde a identificação
dos discos até a geração de relatórios.

Funções principais:
    analyzer(): Executa o fluxo completo de análise de discos

Exemplo:
    >>> from analyzer import analyzer
    >>> analyzer()
"""

from .disk_analyzer import analyzer

__all__ = ['analyzer']
