#!/bin/bash
echo "═══════════════════════════════════════════════════════════════"
echo "  ELYSIUM-INTEL SYSTEM STATUS REPORT"
echo "═══════════════════════════════════════════════════════════════"
printf "🏛️ CASOS EN VAULT: "
sqlite3 /home/ubuntu/elysium_intel_v2.db "SELECT count(*) FROM cases"
printf "🌐 API STATUS: "
systemctl is-active elysium-api
printf "📊 DASHBOARD STATUS: "
systemctl is-active elysium-dashboard
echo "═══════════════════════════════════════════════════════════════"
