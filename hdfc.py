import sqlite3
 
# Connect to SQLite and create a database
conn = sqlite3.connect("proj.db")
cursor = conn.cursor() #cursor is like pointer or object for the database
 

cursor.execute('''
    CREATE TABLE IF NOT EXISTS hdfc (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            Date DATETIME,
            Prev_Close DOUBLE,
            Open DOUBLE,
            High DOUBLE,
            Low DOUBLE,
            Last DOUBLE,
            Close DOUBLE,
            VWAP DOUBLE,
            Volume INTEGER,
            Turnover DOUBLE
    )
''')


 
 

import csv
 
# Read data from the CSV file
with open('HDFC.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)
 
# Insert data into the table
for row in data:
    cursor.execute("INSERT INTO hdfc(Date, Prev_Close, Open, High,Low,Last,Close,VWAP,Volume,Turnover)VALUES (?, ?, ?, ?,?,?,?,?,?,?)",
                   ( row['Date'], row['Prev_Close'], row['Open'], row['High'],row['Low'], row['Last'],row['Close'], row['VWAP'], row['Volume'], row['Turnover']))
 
# Commit the changes
conn.commit()
 
# Close the database connection
conn.close()
 

import sqlite3
 
# Connect to the database
conn = sqlite3.connect('proj.db')  
cursor = conn.cursor()
 
# Execute a SELECT query on the "hdfc" table
cursor.execute('SELECT * FROM hdfc')


# Fetch all rows
rows = cursor.fetchall()
 
# Display the data
for row in rows:
    print(row)
 
# Close the database connection
conn.close()

# ----------------------------------------------
