import sqlite3, spacy

nlp = spacy.load("es_core_news_md")

def run_nlp_mining():
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    rows = cur.execute("SELECT id_caso, titular FROM cases WHERE id_caso LIKE \"CR-2025-%\"").fetchall()
    print(f"🔬 [NLP-ENGINE] Minando entidades en {len(rows)} casos...")
    
    for id_caso, titular in rows:
        doc = nlp(titular)
        for ent in doc.ents:
            if ent.label_ in ["PER", "ORG", "LOC"]:
                cur.execute("INSERT INTO entities (id_caso, tipo, valor) VALUES (?, ?, ?)", (id_caso, ent.label_, ent.text))
    
    conn.commit()
    conn.close()
    print("✅ Mapeo de Entidades Finalizado.")

if __name__ == "__main__":
    run_nlp_mining()
