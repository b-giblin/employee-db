import sqlite3

# connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('my_database.db')


# Create a cursor object to interact with the database
cursor = conn.cursor()

# SQL Command to create a table
sql_command = """
CREATE TABLE employee (
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
department TEXT);
"""

# Execute the SQL command
cursor.execute(sql_command)

# insert a single record
cursor.execute("INSERT INTO employee (name, age, department) VALUES ('John', 30, 'HR')")

# INSERT multiple records at once

employees = [
  ('Alice', 25, 'Sales'),
  ('Bob', 22, 'Finance'),
  ('Charlie', 29, 'IT'),
]

cursor.executemany("INSERT INTO employee (name, age, department) VALUES (?, ?, ?)", employees)

# fetch all records
cursor.execute("SELECT * FROM employee")
rows = cursor.fetchall()

for row in rows:
  print(row)

# fetch specific records

cursor.execute("SELECT * FROM employee WHERE department = 'IT'")
it_employees = cursor.fetchall()

for employee in it_employees:
  print(employee)


# update age of John
cursor.execute("UPDATE employee SET age = 31 WHERE name = 'John'")

# Delete Johns record
cursor.execute("DELETE FROM employee WHERE name = 'John'")

# Commit the changes
conn.commit()

# Close the connection
cursor.close()
conn.close()
