from database.database import get_connection
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS certificate_verifications (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        candidate_name TEXT,

        certificate_name TEXT,

        issuing_body TEXT,

        credential_id TEXT,

        issue_date TEXT,

        expiry_date TEXT,

        verification_method TEXT,

        verification_url TEXT,

        status TEXT,

        confidence_score INTEGER,

        notes TEXT,

        verified_at TEXT
    )
    """)

    conn.commit()
    conn.close()