"""Pacote de Geradores de Relatórios.

Este pacote fornece funcionalidades para gerar relatórios de
análise de discos em diferentes formatos.
"""

from .main import generate_report, generate_csv_report

__all__ = ['generate_report', 'generate_csv_report']
