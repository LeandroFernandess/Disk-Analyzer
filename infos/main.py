"""Módulo de Informações do Sistema.

Este módulo fornece funções para obter informações sobre discos,
escanear arquivos grandes e interagir com o usuário.

Funções principais:
    get_all_disks(): Obtém lista de todos os discos disponíveis
    scan_large_files(): Escaneia diretórios em busca de arquivos grandes
    select_disks(): Interface para seleção de discos pelo usuário
    get_size_in_gb(): Converte bytes para gigabytes
"""

import os
import logging
from datetime import datetime
from typing import List, Dict, Any

import psutil


# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def get_size_in_gb(size_bytes: int) -> float:
    """Converte bytes para gigabytes.

    Args:
        size_bytes: Tamanho em bytes

    Returns:
        Tamanho em gigabytes (GB)

    Example:
        >>> get_size_in_gb(1073741824)
        1.0
    """
    return size_bytes / (1024**3)


def get_all_disks() -> List[Dict[str, Any]]:
    """Identifica todos os discos montados no sistema.

    Obtém informações detalhadas sobre cada disco/partição disponível,
    incluindo espaço total, usado, livre e percentual de utilização.

    Returns:
        Lista de dicionários contendo informações dos discos:
        - drive: Letra/identificador do disco (ex: 'C:\\')
        - mountpoint: Ponto de montagem
        - fstype: Sistema de arquivos (NTFS, FAT32, etc)
        - total_gb: Tamanho total em GB
        - used_gb: Espaço usado em GB
        - free_gb: Espaço livre em GB
        - percent: Percentual de uso

    Note:
        Discos sem permissão de acesso são ignorados silenciosamente.
    """
    disks = []
    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disks.append(
                {
                    "drive": partition.device,
                    "mountpoint": partition.mountpoint,
                    "fstype": partition.fstype,
                    "total_gb": get_size_in_gb(usage.total),
                    "used_gb": get_size_in_gb(usage.used),
                    "free_gb": get_size_in_gb(usage.free),
                    "percent": usage.percent,
                }
            )
        except PermissionError:
            continue

    return disks


def scan_large_files(
    path: str, min_size_gb: float = 0.1, max_files: int = 100, fast_mode: bool = False
) -> List[Dict[str, Any]]:
    """Escaneia um diretório recursivamente em busca de arquivos grandes.

    Percorre toda a estrutura de diretórios a partir do caminho especificado,
    identificando arquivos que excedem o tamanho mínimo definido. Ignora
    automaticamente pastas de sistema e temporárias.

    Args:
        path: Caminho raiz para iniciar o escaneamento
        min_size_gb: Tamanho mínimo em GB para considerar (padrão: 0.1)
        max_files: Quantidade máxima de arquivos a retornar (padrão: 100)
        fast_mode: Se True, ignora pastas de usuário para acelerar (padrão: False)

    Returns:
        Lista de dicionários com informações dos arquivos encontrados:
        - path: Caminho completo do arquivo
        - size_gb: Tamanho em GB
        - size_bytes: Tamanho em bytes
        - modified: Data de modificação (formato: YYYY-MM-DD HH:MM:SS)

    Note:
        - Arquivos >= 5GB são reportados imediatamente no log
        - Progresso é exibido a cada 100 pastas ou 5000 arquivos
        - Pastas de sistema são automaticamente ignoradas
        - Links simbólicos são pulados para evitar loops
        - Erros de permissão são tratados silenciosamente

    Example:
        >>> files = scan_large_files('C:\\\\', min_size_gb=1.0, max_files=50)
        >>> print(f"Encontrados {len(files)} arquivos grandes")
    """
    large_files = []
    min_size_bytes = min_size_gb * (1024**3)

    # Contadores de progresso
    files_scanned = 0
    dirs_scanned = 0
    large_files_found = 0
    errors_count = 0
    last_log = 0

    mode = "RÁPIDO" if fast_mode else "COMPLETO"
    logger.info(f"Iniciando escaneamento {mode} de {path}")

    try:
        for root, dirs, files in os.walk(path):
            # Lista base de pastas ignoradas
            ignored_folders = [
                "system volume information",
                "$recycle.bin",
                "windows",
                "program files",
                "program files (x86)",
                "programdata",
                "$windows.~bt",
                "$windows.~ws",
                "windowsapps",
                "winsxs",
                "appdata",
                ".git",
                ".svn",
                "node_modules",
                "__pycache__",
                ".cache",
                ".npm",
                ".nuget",
                "temp",
                "tmp",
                ".vs",
                ".vscode-server",
                "packages",
                "obj",
                "bin",
            ]

            # No modo rápido, ignora ainda mais pastas
            if fast_mode:
                ignored_folders.extend(
                    [
                        "documents",
                        "desktop",
                        "downloads",
                        "pictures",
                        "music",
                        "videos",
                        "onedrive",
                        "dropbox",
                        "google drive",
                        "icloud",
                        ".minecraft",
                        "steamapps",
                        "%localappdata%",
                        "%appdata%",
                    ]
                )

            # Ignora pastas de sistema sensíveis e pastas comuns grandes
            dirs[:] = [d for d in dirs if d.lower() not in ignored_folders]

            dirs_scanned += 1

            # Mostra progresso a cada 100 pastas ou 5000 arquivos
            if dirs_scanned % 100 == 0 or (files_scanned - last_log) >= 5000:
                logger.info(
                    f"   Progresso: {dirs_scanned} pastas | {files_scanned} arquivos | {large_files_found} grandes encontrados"
                )
                last_log = files_scanned

            for file in files:
                files_scanned += 1

                try:
                    file_path = os.path.join(root, file)

                    # Pula arquivos de sistema e links simbólicos
                    if os.path.islink(file_path):
                        continue

                    size = os.path.getsize(file_path)

                    if size >= min_size_bytes:
                        large_files.append(
                            {
                                "path": file_path,
                                "size_gb": get_size_in_gb(size),
                                "size_bytes": size,
                                "modified": datetime.fromtimestamp(
                                    os.path.getmtime(file_path)
                                ).strftime("%Y-%m-%d %H:%M:%S"),
                            }
                        )
                        large_files_found += 1

                        # Log imediato para arquivos muito grandes (>= 5GB)
                        if get_size_in_gb(size) >= 5.0:
                            logger.info(
                                f"   → Arquivo grande encontrado: {get_size_in_gb(size):.2f} GB - {file}"
                            )

                except (PermissionError, FileNotFoundError, OSError) as e:
                    errors_count += 1
                    continue

    except (PermissionError, OSError) as e:
        logger.error(f"Erro ao acessar {path}: {e}")

    # Log final do escaneamento
    logger.info(
        f"Escaneamento concluído: {files_scanned} arquivos em {dirs_scanned} pastas"
    )
    logger.info(f"   • Arquivos grandes encontrados: {large_files_found}")
    if errors_count > 0:
        logger.warning(f"   • Arquivos sem permissão/erro: {errors_count}")

    # Ordena por tamanho (maior primeiro) e limita a quantidade
    large_files.sort(key=lambda x: x["size_bytes"], reverse=True)
    return large_files[:max_files]


def select_disks(disks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Interface interativa para seleção de discos pelo usuário.

    Exibe lista formatada de discos disponíveis e permite que o usuário
    selecione quais discos deseja escanear, seja individualmente ou todos.

    Args:
        disks: Lista de discos obtida por get_all_disks()

    Returns:
        Lista de discos selecionados pelo usuário

    Raises:
        ValueError: Se a entrada do usuário for inválida

    Note:
        - Digite '0' para selecionar todos os discos
        - Digite números separados por vírgula (ex: 1,2,3)
        - A função valida se os índices são válidos
        - Entradas inválidas solicitam nova tentativa

    Example:
        >>> disks = get_all_disks()
        >>> selected = select_disks(disks)  # Usuário digita: 1,2
        >>> print(f"{len(selected)} discos selecionados")
    """
    print("\n" + "=" * 80)
    print("SELEÇÃO DE DISCOS")
    print("=" * 80)
    print("\nDiscos disponíveis:\n")

    for i, disk in enumerate(disks, 1):
        print(f"  [{i}] {disk['drive']} - {disk['fstype']}")
        print(
            f"      Total: {disk['total_gb']:.2f} GB | "
            f"Usado: {disk['used_gb']:.2f} GB ({disk['percent']}%) | "
            f"Livre: {disk['free_gb']:.2f} GB"
        )

    print(f"\n  [0] Todos os discos")
    print("\n" + "-" * 80)

    while True:
        try:
            selection = input(
                "\nSelecione o(s) disco(s) para escanear (ex: 1,2 ou 0 para todos): "
            ).strip()

            if not selection:
                logger.warning("Nenhuma seleção feita. Usando todos os discos.")
                return disks

            if selection == "0":
                logger.info(f"Todos os {len(disks)} discos foram selecionados")
                return disks

            # Parse da seleção
            selected_indices = [int(x.strip()) for x in selection.split(",")]

            # Valida os índices
            if any(idx < 1 or idx > len(disks) for idx in selected_indices):
                print(f"❌ Erro: Digite números entre 1 e {len(disks)}")
                continue

            selected_disks = [disks[idx - 1] for idx in selected_indices]
            logger.info(
                f"{len(selected_disks)} disco(s) selecionado(s): {', '.join([d['drive'] for d in selected_disks])}"
            )
            return selected_disks

        except ValueError:
            print("❌ Erro: Digite números separados por vírgula (ex: 1,2)")
        except Exception as e:
            logger.error(f"Erro na seleção: {e}")
            print("❌ Entrada inválida. Tente novamente.")
