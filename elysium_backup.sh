#!/bin/bash
BACKUP_DIR="/home/ubuntu/elysium_vault/backups"
DB_FILE="/home/ubuntu/elysium_intel_v2.db"
mkdir -p $BACKUP_DIR
TIMESTAMP=$(date +%Y%m%d_%H%M)
cp $DB_FILE $BACKUP_DIR/elysium_intel_$TIMESTAMP.db
# Limpiar backups de más de 30 días
find $BACKUP_DIR -type f -mtime +30 -delete
echo "📦 Vault Backup Completado: elysium_intel_$TIMESTAMP.db"
