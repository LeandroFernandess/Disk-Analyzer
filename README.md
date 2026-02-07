# Disk Analyzer - Analisador de Discos

Script Python para identificar discos no computador e localizar arquivos grandes que estão ocupando espaço.

## 📋 Funcionalidades

- ✅ Identifica todos os discos no computador
- ✅ Mostra informações de cada disco (tamanho total, usado, livre)
- ✅ Escaneia e lista os arquivos mais pesados
- ✅ Gera relatório em texto (.txt) e planilha (.csv)
- ✅ Permite configurar tamanho mínimo dos arquivos
- ✅ Ignora pastas de sistema do Windows automaticamente

## 🔧 Requisitos

- Python 3.6 ou superior
- Biblioteca `psutil` (para identificar discos)

## 📦 Instalação

1. Instale a dependência necessária:
```bash
pip install psutil
```

## 🚀 Como Usar

1. Execute o script:
```bash
python disk_analyzer.py
```

2. O script irá:
   - Mostrar todos os discos encontrados
   - Perguntar o tamanho mínimo dos arquivos (padrão: 0.5 GB)
   - Perguntar quantos arquivos listar por disco (padrão: 50)
   - Escanear todos os discos
   - Gerar os relatórios

3. Após a execução, você terá dois arquivos:
   - `relatorio_discos.txt` - Relatório completo em texto
   - `relatorio_arquivos.csv` - Planilha para abrir no Excel

## 📊 Exemplo de Saída

```
DISCO 1: C:\
  Ponto de montagem: C:\
  Tamanho total: 476.94 GB
  Espaço usado: 234.56 GB (49%)
  Espaço livre: 242.38 GB

ARQUIVOS MAIS PESADOS:
1. Tamanho: 15.34 GB
   Caminho: C:\Users\Usuario\Videos\video_grande.mp4
   Modificado: 2026-01-15 14:30:22
```

## ⚙️ Configurações

Você pode editar o script para ajustar:
- `min_size_gb`: Tamanho mínimo dos arquivos (linha onde é solicitado)
- `max_files`: Quantidade máxima de arquivos por disco
- Pastas ignoradas (veja lista em `scan_large_files`)

## 🛡️ Segurança

O script:
- Apenas **lê** arquivos, nunca modifica ou deleta
- Ignora automaticamente pastas de sistema do Windows
- Pula arquivos sem permissão de acesso

## 💡 Dicas

1. **Execute como Administrador** para ter acesso completo a todos os arquivos
2. O escaneamento pode demorar dependendo do tamanho dos discos
3. Use o arquivo CSV para ordenar e filtrar no Excel
4. Revise cuidadosamente antes de deletar qualquer arquivo

## 📝 Notas

- Arquivos de sistema do Windows são automaticamente ignorados
- O script pula links simbólicos para evitar loops
- Erros de permissão são ignorados silenciosamente para não interromper o escaneamento
