#!/bin/bash
source ~/.bashrc

urls="urls.m3u"
if [[ ! -f "$urls" ]]; then
  printf "\033[31mPlease create a $urls file\033[m\n"
  exit 1
fi

function notify() {
  if [[ -f /mnt/c/wsl-notify-send/wsl-notify-send.exe ]]; then
    timeout 5s /mnt/c/wsl-notify-send/wsl-notify-send.exe "$1 completed!" --category Batch &
  elif ! type "notify-send" > /dev/null ; then
    echo "$1 completed!"
    tput bel
  else
    timeout 5s notify-send "$1 completed!" --category Batch &
  fi
}

script=$(readlink -f ./screenshots.py)
list=$(readlink -f ./urls.m3u)
dir='screenshots'

# Passo 1: criar o diretório do lote
first_line=$(head -n 1 "$urls")
case "$first_line" in
  "#PLAYLIST:"*) dir="${first_line#*:}" ;;
esac
if [[ -d "$dir" ]]; then
  printf "\33[31m$dir directory already exists\33[m\n"
  exit 1
else
  mkdir "$dir"
  printf "\33[32m'$dir' batch-directory created\33[m\n"
fi

# Passo 2: Processar cada URL no arquivo
count=0
title=''
portion=0.0
while read -r _curr
do
  case "$_curr" in
    "#TITLE:"*)
      title="${_curr#*:}"
    ;;
    "#PORTION:"*)
      portion="${_curr#*:}"
    ;;
    "#"* | "") ;;
    "http"*)
      echo "<$_curr>|<$title>($portion)"
      if [[ -n "$title" ]]; then
        "$script" "$_curr" "$dir/$title" -p "$portion"
        notify "$title"
        title="" # Limpa o título para a próxima URL
      else
        "$script" "$_curr" "$dir/$count" -p "$portion"
        notify "$count"
        count=$((count+1))
      fi
      portion=0.0 # Reseta a porção para a próxima URL
    ;;
  esac
done < "$list"

echo "done"
notify "All"
