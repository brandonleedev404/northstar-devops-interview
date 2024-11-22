#!/bin/sh
# Usage: sh scripts/backup.sh SOURCE BACKUP
cat "$1" > "$2"
echo "Backup complete"
