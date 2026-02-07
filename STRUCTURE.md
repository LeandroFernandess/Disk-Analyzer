# Estrutura do Projeto Disk Analyzer

Este documento descreve a estrutura completa do projeto e a organização dos módulos.

## 📁 Estrutura de Diretórios

```
cleaner/                                 # Raiz do projeto
│
├── 📄 main.py                           # ⭐ Ponto de entrada principal
├── 📄 __init__.py                       # Exportações do pacote raiz
│
├── 📁 analyzer/                         # 🔍 Módulo de análise de discos
│   ├── 📄 __init__.py                   # Exportações do módulo
│   ├── 📄 disk_analyzer.py              # Função principal analyzer()
│   └── 📄 README.md                     # Documentação do módulo
│
├── 📁 infos/                            # 📊 Módulo de informações do sistema
│   ├── 📄 __init__.py                   # Exportações do módulo
│   ├── 📄 main.py                       # Funções de disco e escaneamento
│   └── 📄 README.md                     # Documentação do módulo
│
├── 📁 generators/                       # 📝 Módulo de geração de relatórios
│   ├── 📄 __init__.py                   # Exportações do módulo
│   ├── 📄 main.py                       # Geradores TXT e CSV
│   └── 📄 README.md                     # Documentação do módulo
│
├── 📄 requirements.txt                  # Dependências do projeto
├── 📄 .gitignore                        # Arquivos ignorados pelo Git
├── 📄 .editorconfig                     # Padronização de editores
│
├── 📄 README.md                         # 📚 Documentação principal
├── 📄 CONTRIBUTING.md                   # Guia de contribuição
├── 📄 CHANGELOG.md                      # Histórico de versões
├── 📄 STRUCTURE.md                      # Este arquivo
├── 📄 LICENSE                           # Licença MIT
│
├── 📄 setup.py                          # Configuração de instalação (setuptools)
├── 📄 pyproject.toml                    # Configuração moderna (PEP 518)
│
├── 📁 venv/                             # 🔒 Ambiente virtual (não versionado)
├── 📁 __pycache__/                      # 🔒 Cache Python (não versionado)
│
└── 📄 relatorio_*.txt/*.csv             # 🔒 Relatórios gerados (não versionados)
```

## 🎯 Módulos e Responsabilidades

### 1. `main.py` - Ponto de Entrada
**Responsabilidade:** Inicializar o programa e tratar exceções
```python
from main import main
main()  # Executa o analisador
```

### 2. `analyzer/` - Orquestrador
**Responsabilidade:** Coordenar todo o fluxo de análise
```python
from analyzer import analyzer
analyzer()  # Executa análise completa
```

**Funções:**
- `analyzer()`: Orquestra identificação, seleção, escaneamento e relatórios

### 3. `infos/` - Informações do Sistema
**Responsabilidade:** Obter dados de discos e escanear arquivos
```python
from infos import get_all_disks, scan_large_files, select_disks
```

**Funções:**
- `get_all_disks()`: Lista discos do sistema
- `scan_large_files()`: Busca arquivos grandes
- `select_disks()`: Interface de seleção
- `get_size_in_gb()`: Converte bytes para GB

### 4. `generators/` - Geração de Relatórios
**Responsabilidade:** Criar relatórios em diferentes formatos
```python
from generators import generate_report, generate_csv_report
```

**Funções:**
- `generate_report()`: Gera relatório TXT
- `generate_csv_report()`: Gera relatório CSV

## 🔄 Fluxo de Dados

```
┌─────────────────────────────────────────────────────────┐
│                       main.py                           │
│                  (Ponto de entrada)                     │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                 analyzer/disk_analyzer.py               │
│              (Orquestrador do processo)                 │
└──────────┬──────────────────────────────┬───────────────┘
           │                              │
           ▼                              ▼
┌──────────────────────┐      ┌──────────────────────────┐
│   infos/main.py      │      │  generators/main.py      │
│                      │      │                          │
│ • get_all_disks()    │      │ • generate_report()      │
│ • scan_large_files() │      │ • generate_csv_report()  │
│ • select_disks()     │      │                          │
└──────────────────────┘      └──────────────────────────┘
           │                              │
           ▼                              ▼
     [Dados dos                    [Relatórios
      discos e                      TXT e CSV]
      arquivos]
```

## 📦 Dependências entre Módulos

```
main.py
  └─→ analyzer.disk_analyzer
        ├─→ infos.main
        │     └─→ psutil (externa)
        └─→ generators.main
```

## 🔐 Arquivos Não Versionados

Protegidos pelo `.gitignore`:

```
venv/                    # Ambiente virtual
__pycache__/             # Cache Python
*.pyc                    # Bytecode compilado
relatorio_*.txt          # Relatórios sensíveis
relatorio_*.csv          # Relatórios sensíveis
*.log                    # Arquivos de log
```

## 📚 Documentação Disponível

| Arquivo | Descrição |
|---------|-----------|
| `README.md` | Documentação principal do projeto |
| `analyzer/README.md` | Detalhes do módulo analyzer |
| `infos/README.md` | Detalhes do módulo infos |
| `generators/README.md` | Detalhes do módulo generators |
| `CONTRIBUTING.md` | Guia para contribuidores |
| `CHANGELOG.md` | Histórico de versões |
| `STRUCTURE.md` | Este arquivo - estrutura do projeto |
| `LICENSE` | Licença MIT |

## 🧪 Convenções de Código

### Imports
```python
# Ordem: stdlib → externos → internos
import time
import logging
from datetime import timedelta

import psutil

from infos import get_all_disks
from generators import generate_report
```

### Naming Conventions
- **Módulos**: `snake_case` (ex: `disk_analyzer`)
- **Funções**: `snake_case` (ex: `get_all_disks`)
- **Classes**: `PascalCase` (não usado neste projeto)
- **Constantes**: `UPPER_CASE` (não usado neste projeto)
- **Variáveis privadas**: `_leading_underscore`

### Docstrings
```python
def function_name(param: type) -> return_type:
    """Breve descrição da função.
    
    Descrição detalhada se necessário.
    
    Args:
        param: Descrição do parâmetro
        
    Returns:
        Descrição do retorno
        
    Raises:
        Exception: Quando ocorre
        
    Example:
        >>> function_name(value)
        result
    """
```

## 🎨 Padrões Seguidos

- ✅ **PEP 8**: Estilo de código Python
- ✅ **PEP 257**: Docstrings
- ✅ **PEP 484**: Type hints
- ✅ **PEP 518**: pyproject.toml
- ✅ **Black**: Formatação de código (88 chars)
- ✅ **isort**: Organização de imports

## 🚀 Comandos Úteis

```bash
# Executar o programa
python main.py

# Instalar dependências
pip install -r requirements.txt

# Instalar em modo desenvolvimento
pip install -e .

# Executar após instalação
disk-analyzer

# Limpar cache
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
```

## 🔧 Configuração de Desenvolvimento

### VS Code Settings (recomendado)

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.rulers": [88],
  "[python]": {
    "editor.tabSize": 4
  }
}
```

### EditorConfig

Já configurado em `.editorconfig`:
- Indentação: 4 espaços (Python)
- Charset: UTF-8
- Line ending: LF
- Trim trailing whitespace

## 📊 Estatísticas do Projeto

- **Linguagem**: Python 3.6+
- **Linhas de código**: ~1000 (aproximado)
- **Módulos**: 3 (analyzer, infos, generators)
- **Funções públicas**: 6
- **Dependências externas**: 1 (psutil)
- **Cobertura de documentação**: 100%

## 🔗 Links Úteis

- [Documentação Python](https://docs.python.org/3/)
- [PEP 8 - Style Guide](https://pep8.org/)
- [psutil Documentation](https://psutil.readthedocs.io/)
- [Black Formatter](https://black.readthedocs.io/)

---

**Última atualização:** 2026-02-07
**Versão do projeto:** 1.0.0
