#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb module
import MySQLdb
# Import sys module to access command-line arguments
import sys

# Get the arguments from the command line
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to the MySQL server on localhost at port 3306
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Execute a query that selects all states from the database and orders them by id
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Loop through each row and print it
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
db.close()
