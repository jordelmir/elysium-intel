#!/bin/bash
# Copiar el último reporte al vault de la web
LATEST=$(ls -t ~/elysium_vault/scan_*.json | head -1)
cp $LATEST ~/elysium_vault/latest.json
echo "📦 Sync completada: $LATEST -> latest.json"

# Trigger de Webhook a Vercel (si tienes la URL del deploy hook configurada)
# Reemplaza con tu Vercel Deploy Hook URL
if [ -f ~/.vercel_deploy_hook ]; then
    HOOK_URL=$(cat ~/.vercel_deploy_hook)
    curl -X POST $HOOK_URL
    echo "🚀 Redeploy en Vercel solicitado."
fi
