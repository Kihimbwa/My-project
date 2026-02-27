import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Add missing columns to library_borrowrecord table
try:
    cursor.execute("ALTER TABLE library_borrowrecord ADD COLUMN expected_return_date date")
    print("Added expected_return_date column")
except Exception as e:
    print(f"expected_return_date: {e}")

try:
    cursor.execute("ALTER TABLE library_borrowrecord ADD COLUMN actual_return_date date")
    print("Added actual_return_date column")
except Exception as e:
    print(f"actual_return_date: {e}")

try:
    cursor.execute("ALTER TABLE library_borrowrecord ADD COLUMN penalty integer default 0")
    print("Added penalty column")
except Exception as e:
    print(f"penalty: {e}")

conn.commit()

# Verify the table structure
cursor.execute("PRAGMA table_info(library_borrowrecord)")
print("\nBorrowRecord table columns after fix:")
for col in cursor.fetchall():
    print(col)

conn.close()
print("\nDatabase fix complete!")
