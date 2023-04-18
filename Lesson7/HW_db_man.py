import sqlite3

conn = sqlite3.connect('films_db')

c = conn.cursor()

c.execute("INSERT INTO films VALUES (1, 'Back to the Future', 'Robert Lee Zemeckis', 1989)")
c.execute("INSERT INTO films VALUES (2, 'Robocop', 'Paul Verhoeven', 1987)")
c.execute("INSERT INTO films VALUES (3, 'Terminator', 'James Francis Cameron', 1984)")

c.execute("UPDATE films SET release_year = 2001 WHERE title = 'Terminator'")

c.execute("SELECT * FROM films")
rows = c.fetchall()

conn.commit()

for row in rows:
    print(row)

c.execute("DELETE from films")
conn.commit()
