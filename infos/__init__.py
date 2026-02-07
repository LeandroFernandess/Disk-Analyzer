"""Pacote de Informações do Sistema.

Este pacote fornece funcionalidades para obter informações sobre
discos e escanear arquivos no sistema.
"""

from .main import get_all_disks, scan_large_files, select_disks, get_size_in_gb

__all__ = ['get_all_disks', 'scan_large_files', 'select_disks', 'get_size_in_gb']
