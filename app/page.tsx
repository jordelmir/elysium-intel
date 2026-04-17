"use client"
import React, { useEffect, useState } from "react"
import { Shield, Activity, Database, Globe, ExternalLink } from "lucide-react"

const API_BASE = "http://150.136.42.125/api"

export default function Home() {
  const [stats, setStats] = useState({ total_cases: 0, total_entities: 0 })
  const [latest, setLatest] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      try {
        const sRes = await fetch(API_BASE + "/stats")
        const lRes = await fetch(API_BASE + "/latest")
        setStats(await sRes.json())
        setLatest(await lRes.json())
      } catch (e) {
        console.error("Error core", e)
      }
    }
    fetchData()
  }, [])

  return (
    <main style={{ fontFamily: "monospace", padding: "40px", maxWidth: "1200px", margin: "0 auto", background: "#030508", color: "#c8d8e8", minHeight: "100vh" }}>
      <header style={{ borderBottom: "2px solid #ff4444", paddingBottom: "20px", marginBottom: "40px" }}>
        <h1 style={{ fontSize: "2rem", fontWeight: "bold", color: "#fff", display: "flex", alignItems: "center", gap: "15px" }}>
          <Shield size={40} color="#ff4444" /> ELYSIUM INTEL | Command Center
        </h1>
      </header>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: "20px" }}>
        <div style={{ background: "#040c14", border: "1px solid #0a3050", padding: "30px" }}>
          <p style={{ color: "#0a5080" }}>VAULT CAPACITY</p>
          <h2 style={{ fontSize: "3rem", margin: 0 }}>{stats.total_cases}</h2>
        </div>
        <div style={{ background: "#040c14", border: "1px solid #0a3050", padding: "30px" }}>
          <p style={{ color: "#0a5080" }}>NEURAL ENTITIES</p>
          <h2 style={{ fontSize: "3rem", margin: 0 }}>{stats.total_entities}</h2>
        </div>
      </div>
    </main>
  )
}
