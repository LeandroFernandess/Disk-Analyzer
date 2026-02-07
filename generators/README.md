# Módulo Generators

Este módulo contém funções para gerar relatórios de análise em diferentes formatos.

## Funções Principais

### `generate_report(disks, all_large_files, output_file) -> None`
Gera relatório detalhado em formato texto (.txt).

**Características:**
- Formatação legível para humanos
- Informações completas dos discos
- Lista ordenada dos arquivos grandes
- Data e hora da análise

### `generate_csv_report(all_large_files, output_file) -> None`
Gera relatório em formato CSV para análise em planilhas.

**Características:**
- Compatível com Excel e Google Sheets
- Colunas: Tamanho (GB), Caminho, Data de Modificação
- Fácil ordenação e filtragem
- Codificação UTF-8

## Uso

```python
from generators import generate_report, generate_csv_report

# Gerar relatório TXT
generate_report(disks, files, 'meu_relatorio.txt')

# Gerar relatório CSV
generate_csv_report(files, 'meu_relatorio.csv')
```

## Formato dos Relatórios

### TXT
```
================================================================================
RELATÓRIO DE ANÁLISE DE DISCOS
Data: 2026-02-07 19:16:22
================================================================================

DISCO 1: C:\
  Tamanho total: 110.08 GB
  Espaço usado: 85.20 GB (77.4%)
  ...
```

### CSV
```csv
Tamanho (GB),Caminho,Data de Modificação
6.37,C:\hiberfil.sys,2026-02-07 15:30:22
4.50,C:\pagefile.sys,2026-02-07 18:45:10
```
