import { NextResponse } from "next/server"
export async function GET() {
  return NextResponse.json({ status: "200 OK", engine: "Elysium Next.js Core" })
}
