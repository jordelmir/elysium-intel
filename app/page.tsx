import { Shield, Activity, Database, Globe } from "lucide-react"

export default function Home() {
  return (
    <main style={{ fontFamily: "monospace", padding: "40px" }}>
      <header style={{ borderBottom: "1px solid #ff444466", paddingBottom: "20px", marginBottom: "40px" }}>
        <h1 style={{ fontSize: "2rem", letterSpacing: "4px", color: "#fff", display: "flex", alignItems: "center", gap: "15px" }}>
          <Shield color="#ff4444" /> ELYSIUM INTEL | National Command
        </h1>
        <p style={{ color: "#0a5080", fontSize: "0.9rem" }}>SISTEMA DE VIGILANCIA CRIMINAL v7.0 • COSTA RICA</p>
      </header>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))", gap: "20px" }}>
        <div style={{ background: "#040c14", border: "1px solid #0a3050", padding: "20px" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "10px" }}>
            <Database size={18} color="#00aaff" /> <span style={{ fontSize: "0.8rem", color: "#0a5080" }}>VAULT STATUS</span>
          </div>
          <h2 style={{ fontSize: "2.5rem", margin: 0 }}>11.6k+</h2>
          <p style={{ fontSize: "0.7rem", color: "#00ff88" }}>REGISTROS ASEGURADOS</p>
        </div>
        <div style={{ background: "#040c14", border: "1px solid #0a3050", padding: "20px" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "10px" }}>
            <Activity size={18} color="#ffaa00" /> <span style={{ fontSize: "0.8rem", color: "#0a5080" }}>NETWORK HEALTH</span>
          </div>
          <h2 style={{ fontSize: "2.5rem", margin: 0 }}>100%</h2>
          <p style={{ fontSize: "0.7rem", color: "#00ff88" }}>UPTIME TRIPLE CAPA</p>
        </div>
      </div>

      <section style={{ marginTop: "60px" }}>
        <h3 style={{ color: "#fff", fontSize: "1.2rem", marginBottom: "20px", display: "flex", alignItems: "center", gap: "10px" }}>
          <Globe size={18} color="#ff4444" /> LIVE INTELLIGENCE FEED
        </h3>
        <div style={{ color: "#3a6a8a", borderLeft: "2px solid #0a3050", paddingLeft: "20px" }}>
          [SISTEMA EN STANDBY] Conectando con Oracle API...
        </div>
      </section>
    </main>
  )
}
