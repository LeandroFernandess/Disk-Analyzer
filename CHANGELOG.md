# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2026-02-07

### ✨ Adicionado
- **Estrutura modular aprimorada** com pasta `analyzer/` dedicada
- **Ponto de entrada dedicado** (`main.py`) para melhor organização
- Sistema de seleção interativa de discos
- Modo Rápido e Modo Completo de escaneamento
- Logging profissional com timestamps
- Feedback em tempo real durante escaneamento
- Alertas imediatos para arquivos >= 5GB
- Métricas detalhadas de tempo de execução
- Type hints em todas as funções
- Docstrings completas seguindo PEP 257
- Arquivo .gitignore para proteger relatórios
- Documentação completa no README.md
- Guia de contribuição (CONTRIBUTING.md)
- Licença MIT
- Arquivo `__init__.py` na raiz do projeto

### 🎯 Características Principais
- Identificação automática de todos os discos
- Geração de relatórios em TXT e CSV
- Ignora automaticamente pastas de sistema
- Contador de progresso (a cada 100 pastas)
- Tratamento robusto de erros de permissão
- Compatibilidade com Windows, Linux e macOS

### 📊 Performance
- Escaneamento rápido: ~1-2 segundos para disco C:\
- Modo completo otimizado com feedback constante
- Filtragem inteligente de pastas desnecessárias

### 🛡️ Segurança
- Operação somente leitura (nunca modifica arquivos)
- Proteção de informações sensíveis (.gitignore)
- Validação de entradas do usuário
- Tratamento seguro de exceções

### 📚 Documentação
- README completo com exemplos
- Docstrings em todas as funções públicas
- Type hints para melhor IDE support
- Guia de contribuição detalhado
- Changelog para rastrear versões

### 🔧 Módulos
- `analyzer/`: Módulo de análise de discos
  - `disk_analyzer.py`: Função principal de análise
- `infos/`: Funções de sistema e escaneamento
- `generators/`: Geradores de relatórios
- Estrutura modular completa com `__init__.py` em todos os módulos

## [0.1.0] - 2026-02-07 (Beta Inicial)

### Adicionado
- Versão inicial do projeto
- Escaneamento básico de arquivos
- Geração de relatórios simples

---

## Tipos de Mudanças

- `✨ Adicionado`: para novas funcionalidades
- `🔄 Modificado`: para mudanças em funcionalidades existentes
- `🗑️ Removido`: para funcionalidades removidas
- `🐛 Corrigido`: para correções de bugs
- `🔒 Segurança`: para vulnerabilidades
- `📚 Documentação`: para mudanças apenas em documentação
- `⚡ Performance`: para melhorias de performance

---

[1.0.0]: https://github.com/seu-usuario/cleaner/releases/tag/v1.0.0
[0.1.0]: https://github.com/seu-usuario/cleaner/releases/tag/v0.1.0
