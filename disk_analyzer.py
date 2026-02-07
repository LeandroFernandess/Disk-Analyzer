import time
import logging
from datetime import timedelta
from generators.main import generate_report, generate_csv_report
from infos.main import get_all_disks, scan_large_files, select_disks


# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def analyzer():
    start_time = time.time()

    print("=" * 80)
    print("ANALISADOR DE DISCOS E ARQUIVOS GRANDES")
    print("=" * 80)
    print()

    # Identifica os discos
    logger.info("Identificando discos no sistema...")
    disks = get_all_disks()

    logger.info(f"{len(disks)} disco(s) encontrado(s)")
    print(f"\n✓ {len(disks)} disco(s) encontrado(s):")
    for disk in disks:
        print(
            f"  • {disk['drive']} - {disk['used_gb']:.2f} GB usado de {disk['total_gb']:.2f} GB ({disk['percent']}%)"
        )

    # Seleção de discos
    selected_disks = select_disks(disks)

    # Pergunta configurações
    print("\n" + "-" * 80)
    print("CONFIGURAÇÕES")
    print("-" * 80)

    # Modo de escaneamento
    print("\nModo de escaneamento:")
    print("  [1] Rápido - Escaneia apenas pastas principais (recomendado)")
    print("  [2] Completo - Escaneia todas as pastas (mais demorado)")

    scan_mode = input("\nEscolha o modo (padrão 1): ").strip()
    scan_mode = scan_mode if scan_mode in ["1", "2"] else "1"

    is_fast_mode = scan_mode == "1"
    mode_name = "RÁPIDO" if is_fast_mode else "COMPLETO"
    logger.info(f"Modo selecionado: {mode_name}")
    print(f"✓ Modo {mode_name} selecionado")

    # Tamanho mínimo baseado no modo
    if is_fast_mode:
        default_min = "1.0"
        print("\n💡 Dica: No modo rápido, recomendamos buscar arquivos >= 1.0 GB")
    else:
        default_min = "0.5"

    min_size = input(
        f"\nTamanho mínimo dos arquivos em GB (padrão {default_min}): "
    ).strip()
    min_size = float(min_size) if min_size else float(default_min)
    logger.info(f"Tamanho mínimo configurado: {min_size} GB")

    max_files = input("Quantidade máxima de arquivos por disco (padrão 50): ").strip()
    max_files = int(max_files) if max_files else 50
    logger.info(f"Máximo de arquivos por disco: {max_files}")

    # Escaneia cada disco
    all_large_files = []

    print("\n" + "=" * 80)
    print("INICIANDO ESCANEAMENTO...")
    print("=" * 80)
    logger.info("Escaneamento iniciado")
    print()

    scan_start_time = time.time()

    for idx, disk in enumerate(selected_disks, 1):
        disk_start = time.time()
        print(f"\n📂 [{idx}/{len(selected_disks)}] Escaneando disco: {disk['drive']}")
        logger.info(
            f"Iniciando escaneamento do disco {disk['drive']} ({disk['mountpoint']})"
        )

        try:
            large_files = scan_large_files(
                disk["mountpoint"], min_size, max_files, is_fast_mode
            )
            all_large_files.extend(large_files)

            disk_elapsed = time.time() - disk_start
            logger.info(
                f"Disco {disk['drive']}: {len(large_files)} arquivo(s) encontrado(s) em {disk_elapsed:.1f}s"
            )
            print(
                f"   ✓ {len(large_files)} arquivo(s) grande(s) encontrado(s) ({disk_elapsed:.1f}s)"
            )
        except Exception as e:
            logger.error(f"Erro ao escanear {disk['drive']}: {e}")
            print(f"   ✗ Erro ao escanear: {e}")

    scan_elapsed = time.time() - scan_start_time
    logger.info(f"Escaneamento concluído em {scan_elapsed:.1f}s")

    # Ordena todos os arquivos
    logger.info("Ordenando arquivos por tamanho...")
    all_large_files.sort(key=lambda x: x["size_bytes"], reverse=True)

    # Limita o total de arquivos no relatório final
    total_limit = max_files * len(selected_disks)
    all_large_files = all_large_files[:total_limit]
    logger.info(
        f"Total de arquivos no relatório: {len(all_large_files)} (limite: {total_limit})"
    )

    print("\n" + "=" * 80)
    print("GERANDO RELATÓRIOS...")
    print("=" * 80)
    logger.info("Iniciando geração de relatórios...")

    # Gera os relatórios
    report_start = time.time()
    generate_report(selected_disks, all_large_files)
    generate_csv_report(all_large_files)
    report_elapsed = time.time() - report_start
    logger.info(f"Relatórios gerados em {report_elapsed:.1f}s")

    # Tempo total
    total_elapsed = time.time() - start_time
    total_time_str = str(timedelta(seconds=int(total_elapsed)))

    print("\n" + "=" * 80)
    print("✓ ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("=" * 80)
    print(f"\n📊 Total de arquivos grandes encontrados: {len(all_large_files)}")

    if all_large_files:
        total_size = sum(f["size_gb"] for f in all_large_files)
        print(f"💾 Tamanho total dos arquivos listados: {total_size:.2f} GB")

    print(f"\n⏱️  Tempo de execução: {total_time_str}")
    print(f"   • Escaneamento: {scan_elapsed:.1f}s")
    print(f"   • Geração de relatórios: {report_elapsed:.1f}s")

    logger.info(f"Execução completa em {total_time_str}")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    try:
        analyzer()
    except KeyboardInterrupt:
        print("\n\n⚠ Operação cancelada pelo usuário.")
        logger.warning("Operação cancelada pelo usuário")
    except Exception as e:
        print(f"\n\n❌ Erro: {e}")
        logger.error(f"Erro durante a execução: {e}", exc_info=True)
        import traceback

        traceback.print_exc()
