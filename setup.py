"""Setup configuration for Disk Analyzer."""

from setuptools import setup, find_packages
from pathlib import Path

# Lê o README para a descrição longa
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="disk-analyzer",
    version="1.0.0",
    author="GitHub Copilot",
    author_email="",
    description="Analisador de discos e arquivos grandes para otimização de armazenamento",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/cleaner",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Filesystems",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    keywords="disk analyzer storage files cleanup optimization",
    python_requires=">=3.6",
    install_requires=[
        "psutil>=5.9.0",
    ],
    entry_points={
        "console_scripts": [
            "disk-analyzer=disk_analyzer:analyzer",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/seu-usuario/cleaner/issues",
        "Source": "https://github.com/seu-usuario/cleaner",
        "Documentation": "https://github.com/seu-usuario/cleaner#readme",
        "Changelog": "https://github.com/seu-usuario/cleaner/blob/main/CHANGELOG.md",
    },
)
