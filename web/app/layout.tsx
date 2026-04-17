import "./globals.css"
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body style={{ background: "#030508", margin: 0, color: "#c8d8e8" }}>{children}</body>
    </html>
  )
}
