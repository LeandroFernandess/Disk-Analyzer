# Módulo Infos

Este módulo contém funções para obter informações do sistema e escanear arquivos.

## Funções Principais

### `get_all_disks() -> List[Dict[str, Any]]`
Identifica todos os discos montados no sistema.

### `scan_large_files(path, min_size_gb, max_files, fast_mode) -> List[Dict[str, Any]]`
Escaneia diretório recursivamente em busca de arquivos grandes.

### `select_disks(disks) -> List[Dict[str, Any]]`
Interface interativa para seleção de discos.

### `get_size_in_gb(size_bytes) -> float`
Converte bytes para gigabytes.

## Uso

```python
from infos import get_all_disks, scan_large_files

disks = get_all_disks()
files = scan_large_files(disks[0]['mountpoint'], min_size_gb=1.0)
```
