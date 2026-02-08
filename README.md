# 🧹 Disk Analyzer - Analisador de Discos

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Script Python profissional para identificar discos no computador e localizar arquivos grandes que estão ocupando espaço, facilitando a limpeza e otimização do armazenamento.

## 📑 Índice

- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Documentação da API](#-documentação-da-api)
- [Exemplos](#-exemplos)
- [Configurações](#-configurações)
- [Segurança](#-segurança)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

> 📖 Para detalhes completos da estrutura e arquitetura, veja [STRUCTURE.md](STRUCTURE.md)

## ✨ Características

### Funcionalidades Principais

- ✅ **Detecção Automática de Discos** - Identifica todos os discos e partições do sistema
- ✅ **Dois Modos de Escaneamento**
  - 🚀 **Modo Rápido**: Escaneia apenas pastas principais (recomendado)
  - 🔍 **Modo Completo**: Escaneia todas as pastas do sistema
- ✅ **Seleção Flexível** - Escolha discos específicos ou escaneie todos
- ✅ **Relatórios Múltiplos** - Gera saída em TXT (legível) e CSV (Excel)
- ✅ **Feedback em Tempo Real** - Progresso detalhado durante escaneamento
- ✅ **Logging Profissional** - Sistema de logs com timestamps
- ✅ **Métricas de Performance** - Tempo de execução detalhado por etapa

### Segurança e Inteligência

- 🛡️ **Somente Leitura** - Nunca modifica ou deleta arquivos
- 🧠 **Filtros Inteligentes** - Ignora automaticamente:
  - Pastas de sistema do Windows (System32, Program Files, etc)
  - Pastas temporárias e cache
  - Diretórios de desenvolvimento (node_modules, .git, __pycache__)
- ⚡ **Otimizado** - Pula arquivos sem permissão sem interromper
- 🎯 **Alertas Inteligentes** - Notifica imediatamente arquivos >= 5GB

## 🔧 Requisitos

### Requisitos de Sistema

- **Python**: 3.6 ou superior
- **Sistema Operacional**: Windows, Linux, macOS
- **Permissões**: Recomendado executar como administrador para acesso completo

### Dependências

```txt
psutil>=5.9.0
```

## 📦 Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/LeandroFernandess/Disk-Analyzer.git
cd cleaner
```

### 2. Crie um Ambiente Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

## 🚀 Uso

### Execução Básica

```bash
python main.py
```

Ou diretamente pelo módulo:

```bash
python disk_analyzer.py
```

### Fluxo de Uso

1. **Visualização de Discos**
   ```
   ✓ 4 disco(s) encontrado(s):
     • C:\ - 85.20 GB usado de 110.08 GB (77.4%)
     • D:\ - 28.96 GB usado de 931.50 GB (3.1%)
   ```

2. **Seleção de Discos**
   - Digite `0` para todos os discos
   - Digite números separados por vírgula: `1,2,3`
   - Exemplo: `1` para escanear apenas C:\

3. **Escolha do Modo**
   - `1` para Modo Rápido (recomendado)
   - `2` para Modo Completo

4. **Configuração de Parâmetros**
   - Tamanho mínimo (GB): quanto menor, mais arquivos
   - Quantidade máxima por disco: limite de resultados

5. **Aguarde o Escaneamento**
   ```
   19:16:21 - INFO - Progresso: 500 pastas | 3450 arquivos | 2 grandes encontrados
   ```

6. **Analise os Relatórios**
   - `relatorio_discos.txt` - Relatório completo formatado
   - `relatorio_arquivos.csv` - Para análise no Excel

## 📁 Estrutura do Projeto

```
cleaner/
│
├── main.py                    # ⭐ Ponto de entrada principal
├── __init__.py                # Exportações do pacote raiz
│
├── analyzer/                  # 🔍 Módulo de análise
│   ├── __init__.py
│   ├── disk_analyzer.py       # Função principal de análise
│   └── README.md              # Documentação do módulo
│
├── infos/                     # 📊 Módulo de informações do sistema
│   ├── __init__.py
│   ├── main.py                # Funções de disco e escaneamento
│   └── README.md              # Documentação do módulo
│
├── generators/                # 📝 Módulo de geração de relatórios  
│   ├── __init__.py
│   ├── main.py                # Geradores TXT e CSV
│   └── README.md              # Documentação do módulo
│
├── requirements.txt           # Dependências do projeto
├── .gitignore                 # Arquivos ignorados pelo Git
├── README.md                  # Esta documentação
├── LICENSE                    # Licença MIT
├── CONTRIBUTING.md            # Guia de contribuição
├── CHANGELOG.md               # Histórico de versões
├── setup.py                   # Configuração de instalação
├── pyproject.toml             # Configuração moderna
├── .editorconfig              # Padronização de editores
│
└── venv/                      # Ambiente virtual (não versionado)
```

## 📚 Documentação da API

### Módulo `infos.main`

#### `get_all_disks() -> List[Dict[str, Any]]`

Identifica todos os discos montados no sistema.

**Returns:**
- Lista de dicionários com informações dos discos:
  - `drive`: Identificador do disco (ex: 'C:\\')
  - `mountpoint`: Ponto de montagem
  - `fstype`: Sistema de arquivos (NTFS, FAT32, etc)
  - `total_gb`: Tamanho total em GB
  - `used_gb`: Espaço usado em GB
  - `free_gb`: Espaço livre em GB
  - `percent`: Percentual de uso

**Example:**
```python
from infos.main import get_all_disks

disks = get_all_disks()
for disk in disks:
    print(f"{disk['drive']}: {disk['used_gb']:.2f}GB / {disk['total_gb']:.2f}GB")
```

#### `scan_large_files(path, min_size_gb=0.1, max_files=100, fast_mode=False) -> List[Dict[str, Any]]`

Escaneia diretório recursivamente em busca de arquivos grandes.

**Parameters:**
- `path` (str): Caminho raiz para iniciar o escaneamento
- `min_size_gb` (float): Tamanho mínimo em GB (padrão: 0.1)
- `max_files` (int): Quantidade máxima de arquivos (padrão: 100)
- `fast_mode` (bool): Se True, ignora pastas de usuário (padrão: False)

**Returns:**
- Lista de dicionários com informações dos arquivos:
  - `path`: Caminho completo do arquivo
  - `size_gb`: Tamanho em GB
  - `size_bytes`: Tamanho em bytes
  - `modified`: Data de modificação (YYYY-MM-DD HH:MM:SS)

**Example:**
```python
from infos.main import scan_large_files

files = scan_large_files('C:\\', min_size_gb=1.0, max_files=50, fast_mode=True)
for file in files:
    print(f"{file['size_gb']:.2f}GB - {file['path']}")
```

### Módulo `generators.main`

#### `generate_report(disks, all_large_files, output_file='relatorio_discos.txt') -> None`

Gera relatório detalhado em formato texto.

**Parameters:**
- `disks`: Lista de discos analisados
- `all_large_files`: Lista de arquivos grandes encontrados
- `output_file`: Nome do arquivo de saída

#### `generate_csv_report(all_large_files, output_file='relatorio_arquivos.csv') -> None`

Gera relatório em formato CSV para Excel.

**Parameters:**
- `all_large_files`: Lista de arquivos grandes encontrados
- `output_file`: Nome do arquivo CSV

## 💡 Exemplos

### Exemplo 1: Escaneamento Rápido do Drive C:

```
Selecione o(s) disco(s): 1
Modo: 1 (Rápido)
Tamanho mínimo: 1.0 GB
Arquivos por disco: 50

Resultado: ~1-2 segundos de escaneamento
```

### Exemplo 2: Escaneamento Completo de Múltiplos Discos

```
Selecione o(s) disco(s): 1,2,3
Modo: 2 (Completo)  
Tamanho mínimo: 0.5 GB
Arquivos por disco: 100

Resultado: Tempo variável, feedback em tempo real
```

### Exemplo 3: Uso Programático

```python
# Opção 1: Usar a função principal
from main import main

main()  # Executa o analisador interativo completo
```

```python
# Opção 2: Usar os módulos diretamente
from infos.main import get_all_disks, scan_large_files
from generators.main import generate_report, generate_csv_report

# Obter discos
disks = get_all_disks()
print(f"Encontrados {len(disks)} discos")

# Escanear primeiro disco
files = scan_large_files(
    disks[0]['mountpoint'], 
    min_size_gb=1.0, 
    max_files=50,
    fast_mode=True
)

# Gerar relatórios
generate_report([disks[0]], files, 'meu_relatorio.txt')
generate_csv_report(files, 'meu_relatorio.csv')
```

## ⚙️ Configurações

### Pastas Ignoradas (Modo Rápido)

O modo rápido ignora automaticamente:

**Sistema:**
- System Volume Information, Windows, Program Files
- $RECYCLE.BIN, ProgramData, WindowsApps

**Desenvolvimento:**
- node_modules, .git, .svn, __pycache__
- .cache, .npm, .nuget, packages

**Temporárias:**
- temp, tmp, AppData

**Usuário (apenas modo rápido):**
- Documents, Desktop, Downloads
- Pictures, Music, Videos
- OneDrive, Dropbox, Google Drive

### Ajuste de Logging

Edite `disk_analyzer.py` para alterar o nível de logging:

```python
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG, INFO, WARNING, ERROR
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
```

## 🔒 Segurança

### ⚠️ Informações Sensíveis nos Relatórios

Os relatórios contêm:
- Nomes de usuário do Windows
- Estrutura de pastas pessoais
- Nomes de arquivos e projetos
- Software instalado

### 🛡️ Proteção Configurada

O `.gitignore` já está configurado para proteger:
- `relatorio_*.txt` e `relatorio_*.csv`
- Ambiente virtual (`venv/`)
- Cache e arquivos temporários

### 📝 Recomendações

1. **NUNCA** compartilhe relatórios publicamente
2. **NÃO** adicione relatórios ao Git
3. **SEMPRE** revise antes de compartilhar
4. Anonimize caminhos se necessário compartilhar exemplos

### Padrões de Código

- Siga PEP 8 (estilo Python)
- Use type hints quando possível
- Adicione docstrings para funções públicas
- Mantenha compatibilidade com Python 3.6+

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

Desenvolvido por **Leandro Fernandes**

## 🆘 Suporte

Encontrou um bug ou tem uma sugestão?
- Abra uma issue [https://github.com/LeandroFernandess/Disk-Analyzer/issues]
- Entre em contato através do e-mail [leandrofernandes1600@gmail.com]

---

**⚡ Dica:** Execute como administrador para ter acesso completo a todos os arquivos!

**🎯 Objetivo:** Ajudar você a recuperar espaço em disco identificando arquivos grandes desnecessários.
