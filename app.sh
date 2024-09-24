#!/bin/bash

# Check if a service name was provided
if [ $# -eq 0 ]; then
    echo "Please provide a service name (using-chains, chat-app, or fact-finder)"
    exit 1
fi

# Run the specified service
docker-compose run --rm "$1" "${@:2}"