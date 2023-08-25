import psycopg2

# Database connection parameters
host = "10.127.100.13"
database = "bank_withdraw"
user = "postgres"
password = "1234"
schema = "bank_atm_transactions"  # Replace with the name of the schema you want to list tables from

# Connect to the PostgreSQL database
connection = psycopg2.connect(host=host, database=database, user=user, password=password)

# Create a cursor
cursor = connection.cursor()

# Query to fetch table names from the specified schema
query = f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{schema}';"

# Execute the query
cursor.execute(query)

# Fetch all results
table_names = cursor.fetchall()

# Print the table names
print(f"Tables in the '{schema}' schema:")
for table in table_names:
    print(table[0])

# Close the cursor and connection
cursor.close()
connection.close()
