import sqlite3
from datetime import datetime

# Connect to the same database
conn = sqlite3.connect("threat_data.db")
cursor = conn.cursor()

# Sample data with severity_score
sample_data = [
    ("192.168.1.10", datetime.now().isoformat(), "Brute Force", "High", 90, "India", "Honeypot"),
    ("103.21.244.0", datetime.now().isoformat(), "SQL Injection", "Medium", 60, "USA", "Threat Intel"),
    ("203.0.113.5", datetime.now().isoformat(), "Port Scan", "Low", 30, "Germany", "Honeypot"),
    ("8.8.8.8", datetime.now().isoformat(), "DDoS", "Critical", 95, "USA", "Threat Intel"),
    ("172.16.0.1", datetime.now().isoformat(), "Phishing", "Medium", 55, "India", "Honeypot"),
]

# Insert data
cursor.executemany("""
INSERT INTO threat_data (ip, timestamp, threat_type, severity, severity_score, location, source)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", sample_data)

conn.commit()
conn.close()

print("✅ Sample threat data inserted successfully!")
