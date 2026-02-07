# Guia de Contribuição

Obrigado por considerar contribuir para o Disk Analyzer! 🎉

## 🚀 Como Contribuir

### 1. Reportar Bugs

Se você encontrou um bug:

1. Verifique se já não existe uma [issue](https://github.com/LeandroFernandess/Disk-Analyzer/issues) aberta
2. Crie uma nova issue incluindo:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs. obtido
   - Versão do Python e sistema operacional
   - Logs relevantes

### 2. Sugerir Melhorias

Para sugerir novas funcionalidades:

1. Abra uma issue com o label "enhancement"
2. Descreva claramente a funcionalidade desejada
3. Explique por que seria útil
4. Se possível, sugira uma implementação

### 3. Contribuir com Código

#### Preparando o Ambiente

```bash
# 1. Fork o repositório
# 2. Clone seu fork
git clone https://github.com/seu-usuario/cleaner.git
cd cleaner

# Estrutura do projeto:
# cleaner/
# ├── main.py          (ponto de entrada)
# ├── analyzer/        (lógica de análise)
# ├── infos/           (informações do sistema)
# └── generators/      (geração de relatórios)

# 3. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows

# 4. Instale dependências
pip install -r requirements.txt

# 5. Crie uma branch para sua feature
git checkout -b feature/minha-funcionalidade
```

#### Padrões de Código

**Seguir PEP 8:**
```python
# Bom ✅
def calculate_size(bytes_value: int) -> float:
    """Calcula tamanho em GB."""
    return bytes_value / (1024 ** 3)

# Ruim ❌
def calc(b):
    return b/(1024**3)
```

**Usar Type Hints:**
```python
from typing import List, Dict, Any

def process_disks(disks: List[Dict[str, Any]]) -> None:
    """Processa lista de discos."""
    pass
```

**Docstrings Completas (PEP 257):**
```python
def scan_files(path: str, min_size: float = 1.0) -> List[str]:
    """Escaneia arquivos grandes em um diretório.
    
    Args:
        path: Caminho do diretório a escanear
        min_size: Tamanho mínimo em GB (padrão: 1.0)
        
    Returns:
        Lista de caminhos de arquivos encontrados
        
    Raises:
        PermissionError: Se não houver permissão de acesso
        
    Example:
        >>> files = scan_files('/home/user', min_size=2.0)
        >>> print(len(files))
        5
    """
    pass
```

**Logging ao invés de Print:**
```python
import logging

# Bom ✅
logger.info("Escaneamento iniciado")
logger.error(f"Erro ao acessar: {path}")

# Ruim ❌
print("Escaneamento iniciado")
print(f"Erro: {path}")
```

#### Fazendo Commit

**Mensagens de commit claras:**
```bash
# Bom ✅
git commit -m "feat: adiciona suporte para discos Linux"
git commit -m "fix: corrige erro ao escanear pastas com acentos"
git commit -m "docs: atualiza README com exemplos de uso"

# Ruim ❌
git commit -m "alterações"
git commit -m "fix"
```

**Convenção de commits:**
- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `style:` Formatação (sem mudança de código)
- `refactor:` Refatoração de código
- `test:` Adiciona ou corrige testes
- `chore:` Tarefas de manutenção

#### Pull Request

1. Certifique-se de que seu código:
   - Segue PEP 8
   - Tem type hints
   - Tem docstrings
   - Não quebra funcionalidades existentes

2. Atualize a documentação se necessário

3. Crie o Pull Request:
   ```bash
   git push origin feature/minha-funcionalidade
   ```

4. Descreva claramente:
   - O que foi alterado
   - Por que foi alterado
   - Como testar

## 🧪 Testes

Antes de enviar um PR:

```bash
# Execute o script para verificar se funciona
python disk_analyzer.py

# Teste com diferentes configurações
# - Modo rápido vs completo
# - Diferentes tamanhos mínimos
# - Múltiplos discos
```

## 📝 Checklist do Contributor

- [ ] Código segue PEP 8
- [ ] Funções têm type hints
- [ ] Funções têm docstrings completas
- [ ] Comentários explicam o "porquê", não o "o quê"
- [ ] Logging ao invés de prints
- [ ] README atualizado se necessário
- [ ] Testado localmente
- [ ] Commits seguem convenção
- [ ] Pull Request tem descrição clara

## 💬 Dúvidas?

- Abra uma issue com o label "question"
- Entre em contato através de [email]

## 🙏 Obrigado!

Toda contribuição é valiosa, seja código, documentação, ou reportar bugs!
