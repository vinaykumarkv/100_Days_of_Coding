import sqlite3


def init_db():
	conn = sqlite3.connect('books.db')
	cursor = conn.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS books (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			title TEXT NOT NULL,
			author TEXT NOT NULL,
			rating INTEGER NOT NULL
		)
		''')
	conn.commit()
	conn.close()


if __name__ == '__main__':
	init_db()
