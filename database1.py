import sqlite3

db = sqlite3.connect("contacts.db")
cursor = db.cursor()


# cursor.execute("CREATE TABLE IF NOT EXISTS contacts (name text, phone integer, email text)")
# cursor.execute("INSERT INTO contacts values ('Three',333,'Three@email.com')")
# cursor.execute("DELETE FROM contacts WHERE name LIKE 'one'")

# query = "DELETE FROM contacts WHERE name = ?"
# cursor.execute(query, ("Three",))

# db.commit()
cursor.execute("SELECT * FROM contacts")
# results = cursor.__next__()

# results = cursor.fetchall()

for (name, number, email) in cursor.fetchall():
    print(name)
    print(email)

cursor.close()
db.close()
