import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from getpass import getpass

conn = sqlite3.connect('proj.db')
cursor = conn.cursor()

# Execute SQL queries and load results into Pandas DataFrames

# 1. hdfc

# Data Analysis:
#percentage of volume for all stocks:
q1 = pd.read_sql_query("SELECT Date, Volume FROM hdfc", conn)
print(q1)

# Study the number of trades executed for all stocks:
q2= pd.read_sql_query("SELECT Date, COUNT(*) AS num_trades FROM hdfc ", conn)
print(q2)

# Explore the relationship between trading volume and stock price movements for all stocks:
q3 = pd.read_sql_query("SELECT Date, volume, close FROM hdfc ORDER BY Date", conn)
print(q3)

#Perform a comparative analysis of multiple stocks' VWAP:
q4= pd.read_sql_query("SELECT AVG(VWAP) AS avg_vwap FROM hdfc", conn)
print(q4)

# Calculate the daily turnover for all stocks:
q5 = pd.read_sql_query("SELECT Date, SUM(turnover) AS daily_turnover FROM hdfc GROUP BY Date", conn)
print(q5)




# 2.tcs

# Data Analysis:

# percentage of deliverable volume for all stocks:
q6 = pd.read_sql_query("SELECT Date, Volume FROM wipro", conn)
print(q6)

# Study the number of trades executed for all stocks:
q7= pd.read_sql_query("SELECT Date, COUNT(*) AS num_trades FROM wipro ", conn)
print(q7)

# relationship between trading volume and stock price movements for all stocks:
q8= pd.read_sql_query("SELECT Date, volume, close FROM wipro ORDER BY Date", conn)
print(q8)

#analysis of multiple stocks' VWAP:
q9 = pd.read_sql_query("SELECT AVG(VWAP) AS avg_vwap FROM wipro", conn)
print(q9)

# Calculate the daily turnover for all stocks:
q10 = pd.read_sql_query("SELECT Date, SUM(turnover) AS daily_turnover FROM wipro GROUP BY Date", conn)
print(q10)



# A.Data Analysis

# 1. Analyze the percentage of volume for all stocks:
# import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


# Convert 'date' column to datetime format
q1['Date'] = pd.to_datetime(q1['Date'])
q6['Date'] = pd.to_datetime(q6['Date'])

# Group by year and calculate the mean (or any other aggregation) for each year
q1_yearly = q1.groupby(q1['Date'].dt.year)['Volume'].mean()
q2_yearly = q6.groupby(q6['Date'].dt.year)['Volume'].mean()


# Plotting the relationship year-wise
plt.figure(figsize=(10, 6))

plt.plot(q1_yearly.index, q1_yearly.values, label='HDFC', marker='o', linestyle='-', linewidth=2)
plt.plot(q2_yearly.index, q2_yearly.values, label='WIPRO', marker='o', linestyle='-', linewidth=2)

plt.xlabel('Year')
plt.ylabel('Average Volume')
plt.title('Relationship between Year and Average Volume')
plt.legend()
plt.grid(True)

plt.show()


