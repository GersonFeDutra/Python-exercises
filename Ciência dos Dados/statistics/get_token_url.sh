#!/bin/bash

print_info() {
    printf "$(tput bold)$(tput setaf 4)%s$(tput sgr0)\n" "$1" >&2
}

print_error() {
    printf "$(tput bold)$(tput setaf 1)%s$(tput sgr0)\n" "$1" >&2
}

if [ ! -f app/.env ]; then
    print_info "File .env does not exists. Make sure to run 'docker-compose up' first."
    exit 1
fi

source app/.env
url=http://127.0.0.1:8888/?token=$JUPYTER_TOKEN
if grep -qi "microsoft" /proc/version; then
    echo $url | clip.exe  # wsl
else
    echo $url | xclip
fi

print_info "URL copied to clipboard: $url"
