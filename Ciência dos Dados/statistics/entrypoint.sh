#!/bin/bash
set -e

print_info() {
    printf "$(tput bold)$(tput setaf 4)%s$(tput sgr0)\n" "$1"
}

print_success() {
    printf "$(tput bold)$(tput setaf 2)%s$(tput sgr0)\n" "$1"
}

# Inicia o JupyterLab em background
jupyter-lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root &
JUPYTER_PID=$!

# Aguarda o servidor subir
print_info "Aguardando Jupyter iniciar..."
until jupyter server list 2>/dev/null | grep -q '::'; do
  sleep 1
done

# Captura o token atual
TOKEN=$(jupyter server list | grep -oP 'token=\K\S+')

# Cria arquivo .env no /app (volume montado)
echo "JUPYTER_TOKEN=$TOKEN" > /app/.env
print_success ".env criado com token atual: $TOKEN"

# Mantém o processo vivo
wait $JUPYTER_PID
