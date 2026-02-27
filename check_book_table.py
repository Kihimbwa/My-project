import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Check current structure of library_book table
cursor.execute("PRAGMA table_info(library_book)")
print("Current library_book table columns:")
for col in cursor.fetchall():
    print(col)

conn.close()
