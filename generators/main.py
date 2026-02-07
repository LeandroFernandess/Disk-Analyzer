"""Módulo Gerador de Relatórios.

Este módulo contém funções para gerar relatórios de análise de discos
em diferentes formatos (TXT e CSV).

Funções:
    generate_report(): Gera relatório detalhado em formato texto
    generate_csv_report(): Gera relatório em formato CSV para Excel
"""

import csv
from datetime import datetime
from typing import List, Dict, Any


def generate_report(
    disks: List[Dict[str, Any]], 
    all_large_files: List[Dict[str, Any]], 
    output_file: str = "relatorio_discos.txt"
) -> None:
    """Gera relatório detalhado de análise em formato texto.
    
    Cria um arquivo de texto formatado contendo informações sobre
    os discos analisados e lista dos arquivos grandes encontrados.
    
    Args:
        disks: Lista de discos analisados
        all_large_files: Lista de arquivos grandes encontrados
        output_file: Nome do arquivo de saída (padrão: 'relatorio_discos.txt')
        
    Returns:
        None
        
    Note:
        O arquivo é salvo com codificação UTF-8 no diretório atual.
        O relatório inclui:
        - Data e hora da análise
        - Informações detalhadas de cada disco
        - Lista ordenada dos arquivos mais pesados
    """

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("RELATÓRIO DE ANÁLISE DE DISCOS\n")
        f.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")

        # Informações dos discos
        f.write(f"TOTAL DE DISCOS ENCONTRADOS: {len(disks)}\n\n")

        for i, disk in enumerate(disks, 1):
            f.write(f"\n{'─' * 80}\n")
            f.write(f"DISCO {i}: {disk['drive']}\n")
            f.write(f"{'─' * 80}\n")
            f.write(f"  Ponto de montagem: {disk['mountpoint']}\n")
            f.write(f"  Sistema de arquivos: {disk['fstype']}\n")
            f.write(f"  Tamanho total: {disk['total_gb']:.2f} GB\n")
            f.write(f"  Espaço usado: {disk['used_gb']:.2f} GB ({disk['percent']}%)\n")
            f.write(f"  Espaço livre: {disk['free_gb']:.2f} GB\n")

        # Arquivos grandes
        f.write("\n\n")
        f.write("=" * 80 + "\n")
        f.write("ARQUIVOS MAIS PESADOS ENCONTRADOS\n")
        f.write("=" * 80 + "\n\n")

        if all_large_files:
            for i, file in enumerate(all_large_files, 1):
                f.write(f"\n{i}. Tamanho: {file['size_gb']:.2f} GB\n")
                f.write(f"   Caminho: {file['path']}\n")
                f.write(f"   Modificado: {file['modified']}\n")
        else:
            f.write("Nenhum arquivo grande encontrado.\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("FIM DO RELATÓRIO\n")
        f.write("=" * 80 + "\n")

    print(f"\nRelatório salvo em: {output_file}")


def generate_csv_report(
    all_large_files: List[Dict[str, Any]], 
    output_file: str = "relatorio_arquivos.csv"
) -> None:
    """Gera relatório em formato CSV para análise em planilhas.
    
    Cria arquivo CSV compatível com Excel e outras ferramentas de planilha,
    contendo lista de arquivos grandes com tamanho e informações.
    
    Args:
        all_large_files: Lista de arquivos grandes encontrados
        output_file: Nome do arquivo CSV (padrão: 'relatorio_arquivos.csv')
        
    Returns:
        None
        
    Note:
        - O arquivo é salvo com codificação UTF-8
        - Colunas: Tamanho (GB), Caminho, Data de Modificação
        - Formato CSV padrão compatível com Excel
        - Pode ser aberto em Excel, Google Sheets, LibreOffice, etc
    """

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Tamanho (GB)", "Caminho", "Data de Modificação"])

        for file in all_large_files:
            writer.writerow([f"{file['size_gb']:.2f}", file["path"], file["modified"]])

    print(f"Relatório CSV salvo em: {output_file}")
