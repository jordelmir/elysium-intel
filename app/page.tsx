import React from "react"
import { Shield, Database, Activity } from "lucide-react"
import fs from "fs"
import path from "path"

async function getData() {
  // En Vercel, lee el archivo JSON directamente (generado en tu último scan)
  const vaultPath = path.join(process.cwd(), "../elysium_vault/latest.json")
  if (fs.existsSync(vaultPath)) {
    return JSON.parse(fs.readFileSync(vaultPath, "utf-8"))
  }
  return { casos: [], analisis: { total_unicos: 0 } }
}

export default async function Home() {
  const data = await getData()
  return (
    <main style={{ fontFamily: "monospace", padding: "40px", background: "#030508", color: "#c8d8e8", minHeight: "100vh" }}>
      <h1 style={{ color: "#fff", borderBottom: "2px solid #ff4444" }}>🏛️ ELYSIUM INTEL | PUBLIC PORTAL</h1>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px", marginTop: "40px" }}>
        <div style={{ border: "1px solid #333", padding: "20px" }}>
          <p>CASOS TOTALES (SSG)</p>
          <h2>{data.casos ? data.casos.length : 0}</h2>
        </div>
      </div>
    </main>
  )
}
