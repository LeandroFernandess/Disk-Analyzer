# Módulo Analyzer

Este módulo contém a lógica principal de análise de discos e arquivos grandes do projeto.

## 📋 Descrição

O módulo `analyzer` é responsável por orquestrar todo o processo de análise, incluindo:

- ✅ Identificação de discos disponíveis no sistema
- ✅ Interface de seleção interativa de discos
- ✅ Configuração de parâmetros de busca (modo, tamanho mínimo)
- ✅ Coordenação do escaneamento de arquivos
- ✅ Geração de relatórios finais
- ✅ Métricas de tempo de execução

## 🔧 Arquivo Principal

### `disk_analyzer.py`

Contém a função `analyzer()` que executa o fluxo completo do programa.

## 📚 Funções Principais

### `analyzer() -> None`

Função principal que executa todo o processo de análise.

**Fluxo de Execução:**

1. **Identificação**: Detecta todos os discos montados no sistema
2. **Seleção**: Interface interativa para escolher discos
3. **Configuração**: 
   - Modo de escaneamento (Rápido/Completo)
   - Tamanho mínimo dos arquivos
   - Quantidade máxima de resultados
4. **Escaneamento**: Busca arquivos grandes nos discos selecionados
5. **Geração**: Cria relatórios TXT e CSV
6. **Métricas**: Exibe tempo de execução e estatísticas

**Características:**

- 📊 Feedback em tempo real durante escaneamento
- ⏱️ Métricas detalhadas de performance
- 🔍 Dois modos de escaneamento (Rápido e Completo)
- 🛡️ Tratamento robusto de erros
- 📝 Logging profissional com timestamps

## 🎯 Uso

### Como Módulo

```python
from analyzer import analyzer

# Executa a análise completa
analyzer()
```

### Direto do Arquivo

```python
from analyzer.disk_analyzer import analyzer

analyzer()
```

## 🔄 Integração com Outros Módulos

O módulo `analyzer` integra-se com:

### Módulo `infos`
- `get_all_disks()`: Obtém informações dos discos
- `scan_large_files()`: Escaneia arquivos grandes
- `select_disks()`: Interface de seleção de discos

### Módulo `generators`
- `generate_report()`: Gera relatório TXT
- `generate_csv_report()`: Gera relatório CSV

## 📊 Fluxograma

```
analyzer()
    │
    ├─→ get_all_disks()          [infos]
    │   └─→ Exibe discos encontrados
    │
    ├─→ select_disks()           [infos]
    │   └─→ Usuário seleciona discos
    │
    ├─→ Configuração
    │   ├─→ Modo (Rápido/Completo)
    │   ├─→ Tamanho mínimo (GB)
    │   └─→ Máximo de arquivos
    │
    ├─→ scan_large_files()       [infos]
    │   └─→ Para cada disco selecionado
    │       ├─→ Feedback em tempo real
    │       └─→ Retorna arquivos grandes
    │
    ├─→ Ordenação e filtragem
    │   └─→ Por tamanho (maior primeiro)
    │
    ├─→ generate_report()        [generators]
    │   └─→ Cria relatorio_discos.txt
    │
    ├─→ generate_csv_report()    [generators]
    │   └─→ Cria relatorio_arquivos.csv
    │
    └─→ Exibe estatísticas finais
        ├─→ Total de arquivos encontrados
        ├─→ Tamanho total
        └─→ Tempo de execução
```

## ⚙️ Configurações

### Logging

O módulo utiliza logging configurado com:
- **Nível**: INFO
- **Formato**: `HH:MM:SS - LEVEL - MESSAGE`
- **Saída**: Console

### Modos de Escaneamento

**Modo Rápido (1):**
- Ignora pastas de sistema e usuário
- Recomendado para buscas >= 1.0 GB
- Mais rápido (~1-2 segundos no C:\)

**Modo Completo (2):**
- Escaneia todas as pastas acessíveis
- Mais detalhado
- Mais demorado

## 🛡️ Tratamento de Erros

- **PermissionError**: Ignorado silenciosamente
- **FileNotFoundError**: Ignorado durante escaneamento
- **KeyboardInterrupt**: Mensagem amigável ao usuário
- **Exception geral**: Logged com traceback completo

## 📝 Exemplo Completo

```python
import logging
from analyzer import analyzer

# Configurar logging (opcional, já está configurado)
logging.basicConfig(level=logging.INFO)

# Executar análise
analyzer()

# Saída:
# - relatorio_discos.txt
# - relatorio_arquivos.csv
```

## 🔗 Dependências

- `time`: Métricas de tempo
- `datetime.timedelta`: Formatação de tempo
- `logging`: Sistema de logs
- `infos.main`: Funções de sistema
- `generators.main`: Geradores de relatórios

## 📊 Outputs

Após a execução, são gerados:

1. **relatorio_discos.txt**: Relatório completo formatado
2. **relatorio_arquivos.csv**: Planilha para Excel/Sheets

## 💡 Dicas

1. Execute como administrador para acesso completo
2. Use modo rápido para análises gerais
3. Use modo completo para análise detalhada
4. Ajuste tamanho mínimo conforme necessidade
5. Revise relatórios antes de deletar arquivos

## 🔒 Segurança

- ✅ Apenas leitura (nunca modifica arquivos)
- ✅ Ignora automaticamente pastas de sistema
- ✅ Relatórios são locais e privados
- ⚠️ Não versione os relatórios (.gitignore)
