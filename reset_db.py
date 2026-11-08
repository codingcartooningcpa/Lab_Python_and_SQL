"""Put the Student table back to its starting data.

Run it any time:   python reset_db.py
"""
import mysql.connector
from config import DB_CONFIG

with open("sql/01_schema.sql") as f:
    # Drop comment lines, then split the file into single statements.
    text = "\n".join(line for line in f if not line.strip().startswith("--"))
statements = [s.strip() for s in text.split(";") if s.strip()]

conn = mysql.connector.connect(**DB_CONFIG)
cur = conn.cursor()
for statement in statements:
    cur.execute(statement)
conn.commit()
cur.close()
conn.close()
print("Student table reset to its original 8 rows.")
