import sqlite3

# Connect to the database file, creating it if it doesn't exist
conn = sqlite3.connect('vicious_clue_database.db')

# Commit the changes and close the connection
conn.commit()
conn.close()
