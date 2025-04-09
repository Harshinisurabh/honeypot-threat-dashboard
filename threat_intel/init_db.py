import sqlite3

# Connect to database in the same folder
conn = sqlite3.connect("threat_data.db")
cursor = conn.cursor()

# Create table with severity_score
cursor.execute("""
CREATE TABLE IF NOT EXISTS threat_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    timestamp TEXT,
    threat_type TEXT,
    severity TEXT,
    severity_score INTEGER,
    location TEXT,
    source TEXT
)
""")

conn.commit()
conn.close()

print("✅ threat_data table with severity_score created successfully!")
