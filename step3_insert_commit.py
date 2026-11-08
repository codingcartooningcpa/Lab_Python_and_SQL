"""Step 3: Changing data, and why commit() matters.

Connector/Python does NOT save changes automatically. Until you call
commit(), no one else can see your INSERT. This script proves it by
checking the table from a second, separate connection.
Run it:   python step3_insert_commit.py
"""
import mysql.connector
from config import DB_CONFIG


def count_students():
    """Count rows using a brand-new connection (like another user would)."""
    other = mysql.connector.connect(**DB_CONFIG)
    c = other.cursor()
    c.execute("SELECT COUNT(*) FROM Student")
    n = c.fetchone()[0]
    c.close()
    other.close()
    return n


conn = mysql.connector.connect(**DB_CONFIG)
cur = conn.cursor()

# Start clean, in case this script was run before.
cur.execute("DELETE FROM Student WHERE StudentID = %s", (109,))
conn.commit()

print("Before the INSERT, other users see", count_students(), "students.")

cur.execute(
    "INSERT INTO Student (StudentID, FirstName, LastName, Major) VALUES (%s, %s, %s, %s)",
    (109, "Annie", "Easley", "Computer Science"),
)
print("After INSERT, before commit():  other users see", count_students(), "students.")

conn.commit()                       # now the change is saved for everyone
print("After commit():                 other users see", count_students(), "students.")

cur.close()
conn.close()
