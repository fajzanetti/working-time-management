#!/bin/bash -x

# Limpa o terminal
clear

# Carrega variáveis do .env
set -o allexport
source ~/Projetos/PY/.env
set +o allexport

# Carrega o script
cd "$PROJECT_DIR" && python3 index.py && cd ~

