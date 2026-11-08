"""Step 2: Let the user choose the major.

Same pattern as Step 1, but the value now comes from the keyboard.
Run it:   python step2_user_input.py
Try:      Nursing, Mathematics, Computer Science, Art
"""
import mysql.connector
from config import DB_CONFIG

major = input("Which major? ")

conn = mysql.connector.connect(**DB_CONFIG)
cur = conn.cursor()

sql = "SELECT StudentID, FirstName, LastName FROM Student WHERE Major = %s ORDER BY LastName"
cur.execute(sql, (major,))

rows = cur.fetchall()               # every row at once, as a list
print(len(rows), "student(s) found in", major)
for (student_id, first, last) in rows:
    print(f"  {student_id}  {first} {last}")

cur.close()
conn.close()
