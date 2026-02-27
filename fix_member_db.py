import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Check current structure of library_member table
cursor.execute("PRAGMA table_info(library_member)")
print("Current library_member table columns:")
for col in cursor.fetchall():
    print(col)

# Add missing role column
try:
    cursor.execute("ALTER TABLE library_member ADD COLUMN role varchar(10) default 'student'")
    print("\nAdded role column")
except Exception as e:
    print(f"role column: {e}")

conn.commit()

# Verify the table structure
cursor.execute("PRAGMA table_info(library_member)")
print("\nlibrary_member table columns after fix:")
for col in cursor.fetchall():
    print(col)

conn.close()
print("\nDatabase fix complete!")
