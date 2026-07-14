# =======================================================================
# Project 18: SQL Statistical & Financial Metrics Analytics Framework
# =======================================================================

import mysql.connector # UPGRADED: Using official Enterprise MySQL database engine connection drivers

# 1. connect to the locar secure database engine (Creating a fresh new vault) 
db_engine = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="Secure_Enterprise_Password_165"
)
db_cursor = db_engine.cursor()

# 2.  create and select the target database vault before building tables
db_cursor.execute("CREATE DATABASE IF NOT EXISTS Analytics_Vault")
db_cursor.execute("USE Analytics_Vault")


# 2. Build the production data list
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS  Financial_Ledger (
    Invoice_ID INT PRIMARY KEY,
    Client_Full_Name VARCHAR(150),
     Sales_Value REAL          
)
""")

# 3. Simulate structured production business data logs
corporate_logs = [
    (7001, 'Omega_Dental_Hub', 4950.00),
    (7002, 'Alpha_Health_Care', 5780.00),
    (7003, 'Delta_Clinic_Partners', 2750.00 )
]


# 4. Inject rows using high-velocity parameterized code insertion
db_cursor.executemany("INSERT IGNORE INTO Financial_Ledger VALUES (%s, %s, %s)", corporate_logs)
db_engine.commit() # Flush and lock the rows permanently on disk

# 5. The "COUNT" Weapon --> Counts the whole amount of given name found in the table list
db_cursor.execute("SELECT COUNT(Sales_Value) AS todays_invoices_amount FROM Financial_Ledger")
count = db_cursor.fetchone()[0]
print(f"--- Today's invoices amount: {count} ---")


# 6. The "MIN" Weapon --> prints the minimum value in the whole given name in the table 
db_cursor.execute("SELECT MIN(Sales_Value) AS minimum_lowest_incvoice FROM Financial_Ledger")
min_value = db_cursor.fetchone()[0]
print(f"--- Today's lowest invoice: {min_value} ---")


# 7. The "MAX" Weapon --> prints the maximum value in the whole given name in the table
db_cursor.execute("SELECT MAX(Sales_Value) AS maximum_highest_invoice FROM Financial_Ledger")
max_value = db_cursor.fetchone()[0]
print(f"--- Today's highest invoice: {max_value} ---")

# 8. The "SUM" Weapon --> Summits the whole values and the total of it in the given list name in the table
db_cursor.execute("SELECT SUM(Sales_Value) AS total_invoices_sum FROM Financial_Ledger")
sum_value = db_cursor.fetchone()[0]
print(f"--- Today's whole invoices: {sum_value} ---")

