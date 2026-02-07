from datetime import datetime


def generate_report(disks, all_large_files, output_file="relatorio_discos.txt"):
    """Gera um relatório detalhado em arquivo de texto"""

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


def generate_csv_report(all_large_files, output_file="relatorio_arquivos.csv"):
    """Gera um relatório CSV para fácil manipulação"""
    import csv

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Tamanho (GB)", "Caminho", "Data de Modificação"])

        for file in all_large_files:
            writer.writerow([f"{file['size_gb']:.2f}", file["path"], file["modified"]])

    print(f"Relatório CSV salvo em: {output_file}")
