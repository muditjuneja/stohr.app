#!/bin/sh

if [ ! -f "/app/credentials.json" ]; then
    echo "Credentials file not found. Please mount it to /app/credentials.json"
    exit 1
fi

if [ -z "$SPREADSHEET_ID" ]; then
    echo "SPREADSHEET_ID environment variable is not set. Please set it with -e SPREADSHEET_ID=<your_spreadsheet_id>"
    exit 1
fi

exec "$@"