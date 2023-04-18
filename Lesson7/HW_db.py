import sqlite3

conn = sqlite3.connect('films_db')

c = conn.cursor()

c.execute('''CREATE TABLE films (
        id INTEGER PRIMARY KEY,
        title TEXT,
        director TEXT,
        release_year INTEGER)''')

conn.commit()
