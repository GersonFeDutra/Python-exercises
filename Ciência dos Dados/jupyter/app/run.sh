#!/bin/bash

# Check for command line arg
case "$1" in
    down) docker-compose down exit 0 ;;
    up | "") ;;
    *) echo "Usage: $0 [down]"; exit 1 ;;
esac

docker-compose up
