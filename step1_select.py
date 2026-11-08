"""Step 1: The universal pattern - connect, execute, fetch, close.

Lists every student in the Nursing major.
Run it:   python step1_select.py
"""
import mysql.connector
from config import DB_CONFIG

# 1. CONNECT
conn = mysql.connector.connect(**DB_CONFIG)

# 2. CREATE A CURSOR
cur = conn.cursor()

# 3. EXECUTE - %s is a placeholder; the value is passed separately
sql = "SELECT FirstName, LastName FROM Student WHERE Major = %s"
cur.execute(sql, ("Nursing",))      # the comma makes a one-item tuple

# 4. FETCH - the cursor hands back one row at a time
for (first, last) in cur:
    print(last + ", " + first)

# 5. CLOSE - the cursor first, then the connection
cur.close()
conn.close()
