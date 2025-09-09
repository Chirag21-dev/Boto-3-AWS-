import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

conn.autocommit = True

# Create a cursor object
cur = conn.cursor()

# Execute SQL queries here

# Close the cursor and connection
cur.close()
conn.close()
