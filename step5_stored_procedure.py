"""Step 5: Create and call a stored procedure from Python.

Note: no DELIMITER is needed here. DELIMITER is only for the MySQL
command-line client; Python sends the whole CREATE PROCEDURE as one
statement.
Run it:   python step5_stored_procedure.py
"""
import mysql.connector
from config import DB_CONFIG

conn = mysql.connector.connect(**DB_CONFIG)
cur = conn.cursor()

# Create (or re-create) the procedure on the server.
cur.execute("DROP PROCEDURE IF EXISTS MajorCount")
cur.execute("""
    CREATE PROCEDURE MajorCount(IN p_Major VARCHAR(30), OUT p_Count INT)
    BEGIN
        SELECT COUNT(*) INTO p_Count
        FROM Student WHERE Major = p_Major;
    END
""")
print("Procedure MajorCount created on the server.")

# Call it once per major. The 0 is a placeholder for the OUT parameter.
for major in ("Nursing", "Mathematics", "Computer Science"):
    result = cur.callproc("MajorCount", (major, 0))
    print(f"  {major}: {result[1]} student(s)")   # result[1] is the OUT value

cur.close()
conn.close()
