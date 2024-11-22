#!/bin/sh
# Usage: sh scripts/restore.sh BACKUP DESTINATION
cp "$1" "$2"
echo "Restore complete"
