import sqlite3

def create_database():
    # Connect to SQLite database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Create movies table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            description TEXT NOT NULL,
            rating REAL NOT NULL,
            ranking INTEGER NOT NULL,
            review TEXT NOT NULL,
            img_url TEXT NOT NULL
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

def insert_test_data():
    # Connect to SQLite database
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Insert test data into movies table
    movies_data = [
        ("The Shawshank Redemption", 1994, "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", 9.3, 1, "Amazing movie!", "https://image.url"),
        ("The Godfather", 1972, "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", 9.2, 2, "Masterpiece!", "https://image.url"),
    ]
    cursor.executemany('''
        INSERT INTO movies (title, year, description, rating, ranking, review, img_url)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', movies_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    insert_test_data()
    print("Test data inserted.")
