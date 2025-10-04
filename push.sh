#!/bin/bash

# Adiciona todas as mudanças locais
git add .

# Commit
git commit -m "update"

# Envia para o GitHub
git push origin main

# Printa na tela que foi enviado
echo "Repositório atualizado e enviado!"