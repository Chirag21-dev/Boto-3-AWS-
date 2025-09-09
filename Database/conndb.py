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
cur.execute('CREATE DATABASE new_database;')
cur.execute('SELECT datname FROM new_database;')
cur.execute('''
    CREATE TABLE my_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT
    );
''')
cur.execute("INSERT INTO my_table (name, age) VALUES (%s, %s);", ('John Doe', 30))
cur.execute("SELECT * FROM my_table;")
data = cur.fetchall()
for row in data:
    print(row)

databases = cur.fetchall()
print(databases)

# Close the cursor and connection
cur.close()
conn.close()
