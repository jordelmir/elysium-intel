"use client"
import React, { useEffect, useState } from "react"
import { Shield, Activity, Database, Globe, ExternalLink } from "lucide-react"

const API_BASE = "http://150.136.42.125/api"

export default function Home() {
  const [stats, setStats] = useState({ total_cases: 0, total_entities: 0 })
  const [latest, setLatest] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [sRes, lRes] = await Promise.all([
          fetch(\`\${API_BASE}/stats\`),
          fetch(\`\${API_BASE}/latest\`)
        ])
        setStats(await sRes.json())
        setLatest(await lRes.json())
      } catch (e) {
        console.error("Error connecting to Elysium Core", e)
      } finally {
        setLoading(false)
      }
    }
    fetchData()
  }, [])

  return (
    <main style={{ fontFamily: "ui-monospace, monospace", padding: "40px", maxWidth: "1200px", margin: "0 auto" }}>
      <header style={{ borderBottom: "2px solid #ff4444", paddingBottom: "20px", marginBottom: "40px" }}>
        <h1 style={{ fontSize: "2.5rem", fontWeight: "bold", letterSpacing: "-1px", color: "#fff", display: "flex", alignItems: "center", gap: "15px" }}>
          <Shield size={40} color="#ff4444" /> ELYSIUM INTEL | Command Center
        </h1>
        <div style={{ display: "flex", gap: "20px", marginTop: "10px" }}>
          <span style={{ color: "#00ff88", fontSize: "0.8rem" }}>● CORE OPERATIONAL</span>
          <span style={{ color: "#0a5080", fontSize: "0.8rem" }}>V7.0 PHASE: DOMINION</span>
        </div>
      </header>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: "20px", marginBottom: "50px" }}>
        <div style={{ background: "#040c14", border: "1px solid #0a3050", padding: "30px", borderRadius: "4px" }}>
          <Database size={24} color="#00aaff" style={{ marginBottom: "15px" }} />
          <p style={{ color: "#0a5080", fontSize: "0.7rem", fontWeight: "bold" }}>VAULT CAPACITY</p>
          <h2 style={{ fontSize: "3rem", margin: "5px 0", color: "#fff" }}>{stats.total_cases.toLocaleString()}</h2>
          <p style={{ color: "#00ff88", fontSize: "0.7rem" }}>INCIDENTES ASEGURADOS</p>
        </div>
        <div style={{ background: "#040c14", border: "1px solid #0a3050", padding: "30px", borderRadius: "4px" }}>
          <Activity size={24} color="#ffaa00" style={{ marginBottom: "15px" }} />
          <p style={{ color: "#0a5080", fontSize: "0.7rem", fontWeight: "bold" }}>NEURAL ENTITIES</p>
          <h2 style={{ fontSize: "3rem", margin: "5px 0", color: "#fff" }}>{stats.total_entities.toLocaleString()}</h2>
          <p style={{ color: "#00ff88", fontSize: "0.7rem" }}>VÍNCULOS FORENSES ACTIVOS</p>
        </div>
      </div>

      <section>
        <h3 style={{ color: "#fff", display: "flex", alignItems: "center", gap: "10px", marginBottom: "25px" }}>
          <Globe size={20} color="#ff4444" /> LIVE INTELLIGENCE FEED (TOP 20)
        </h3>
        <div style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: "0.9rem" }}>
            <thead>
              <tr style={{ textAlign: "left", color: "#0a5080", borderBottom: "1px solid #0a3050" }}>
                <th style={{ padding: "15px" }}>ID CASO</th>
                <th style={{ padding: "15px" }}>TITULAR DE EVIDENCIA</th>
                <th style={{ padding: "15px" }}>FUENTE</th>
                <th style={{ padding: "15px" }}>ACTION</th>
              </tr>
            </thead>
            <tbody>
              {latest.map((c: any) => (
                <tr key={c.id_caso} style={{ borderBottom: "1px solid #040c14", background: "#030508" }}>
                  <td style={{ padding: "15px", color: "#ff4444" }}>{c.id_caso}</td>
                  <td style={{ padding: "15px", color: "#ccc" }}>{c.titular}</td>
                  <td style={{ padding: "15px", color: "#00aaff" }}>{c.fuente}</td>
                  <td style={{ padding: "15px" }}>
                    <a href={c.url} target="_blank" rel="noopener noreferrer">
                      <ExternalLink size={16} color="#00ff88" />
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </main>
  )
}
