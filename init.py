from library.db_utils import get_db_connection
import os

#Initialize the database by creating necessary tables.
conn = get_db_connection()
cursor = conn.cursor()

schema_dir = "schemas"
for filename in sorted(os.listdir(schema_dir)):
    if filename.endswith(".sql"):
        with open(os.path.join(schema_dir, filename)) as f:
            print("Executing schema file:", filename);
            ddl = f.read()
            cursor.execute(ddl)

conn.commit()
cursor.close()
conn.close()
print("Database initialized successfully.")