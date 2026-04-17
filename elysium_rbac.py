import sqlite3, hashlib

def create_user(username, password, role):
    db_path = "/home/ubuntu/elysium_intel_v2.db"
    pw_hash = hashlib.sha256(password.encode()).hexdigest()
    with sqlite3.connect(db_path) as conn:
        try:
            conn.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)", (username, pw_hash, role))
            print(f"✅ Usuario {username} creado con rol {role}.")
        except sqlite3.IntegrityError:
            print("⚠️ Usuario ya existe.")

if __name__ == "__main__":
    create_user("admin", "elysium_master_2026", "ADMIN")
    create_user("analista", "elysium_analyst", "ANALYST")
