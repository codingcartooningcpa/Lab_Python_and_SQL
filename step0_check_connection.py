"""Step 0: Make sure Python can reach the MySQL server.

The first time a codespace starts, MySQL needs up to a minute to get
ready. This script keeps trying for about a minute before giving up.
Run it:   python step0_check_connection.py
"""
import time
import mysql.connector
from config import DB_CONFIG

for attempt in range(1, 31):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        break
    except mysql.connector.Error:
        print(f"MySQL is still starting... (try {attempt} of 30)")
        time.sleep(2)
else:
    raise SystemExit("Could not connect. Wait a minute and run this again.")

cur = conn.cursor()
cur.execute("SELECT VERSION()")
print("Connected to MySQL", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM Student")
print("The Student table has", cur.fetchone()[0], "rows. You are ready to go!")

cur.close()
conn.close()
