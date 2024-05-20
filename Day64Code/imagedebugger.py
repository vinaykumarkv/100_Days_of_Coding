import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute('SELECT img_url FROM movies WHERE id = ?', (1,))
img_url = cursor.fetchone()[0]

print(img_url)  # Debug print statement