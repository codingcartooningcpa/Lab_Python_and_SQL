"""Step 4: SQL injection - the unsafe way vs. the safe way.

Both queries look up students by last name. The "user" types a
malicious value. Watch what each version returns.
Run it:   python step4_sql_injection.py
(This only runs SELECT queries, so no data is changed.)
"""
import mysql.connector
from config import DB_CONFIG

evil_input = "x' OR '1'='1"
print("The user types:", evil_input)
print()

conn = mysql.connector.connect(**DB_CONFIG)
cur = conn.cursor()

# UNSAFE: the input is glued into the SQL text with an f-string.
unsafe_sql = f"SELECT FirstName, LastName FROM Student WHERE LastName = '{evil_input}'"
print("UNSAFE query sent to MySQL:")
print("   ", unsafe_sql)
cur.execute(unsafe_sql)
rows = cur.fetchall()
print("    Rows returned:", len(rows), " <-- every student leaked!")
print()

# SAFE: a placeholder, with the input sent separately as data.
safe_sql = "SELECT FirstName, LastName FROM Student WHERE LastName = %s"
print("SAFE query sent to MySQL:")
print("   ", safe_sql)
cur.execute(safe_sql, (evil_input,))
rows = cur.fetchall()
print("    Rows returned:", len(rows), " <-- treated as a strange last name; no match")

cur.close()
conn.close()
