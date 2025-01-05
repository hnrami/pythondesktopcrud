import sqlite3

# Function to set up the database and create the table
def setup_db():
    conn = sqlite3.connect("client_data.db")
    cursor = conn.cursor()
    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            country TEXT,
            dob TEXT,
            occupation TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to save form data into the database
def save_to_db(data):
    conn = sqlite3.connect("client_data.db")
    cursor = conn.cursor()
    # Insert data into the table
    cursor.execute("""
        INSERT INTO user_data (name, email, phone, address, city, state, zip_code, country, dob, occupation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()
