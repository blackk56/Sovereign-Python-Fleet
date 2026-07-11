# =====================================================
# Project 15: Inserting Sql Data into MySQL Table 
# =====================================================

import mysql.connector # UPGRADED: Using official Enterprise MySQL database engine connection drivers


# 1. Connect to the local secure database engine on the disk
db_engine = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="Secure_Enterprise_Password_165"
)
db_cursor = db_engine.cursor()


# 2.  create and select the target database vault before building tables
db_cursor.execute("CREATE DATABASE IF NOT EXISTS Sales_Vault")
db_cursor.execute("USE Sales_Vault")

# 3. Build the secure data storage structure 
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer_List (
    Transaction_ID INT PRIMARY KEY,
    Client_Full_Name VARCHAR(150),
    Amount_Paid REAL,
     Transaction_Date DATE
)
 """)



# 4. Create array simulation raw incoming business logs
invoice_list = [
     (6001, 'Omega_Health_Care_Supply', 3650.25, '2026-07-02'),
     (6002, 'Delta_Farmers_Partners', 1750.75, '2026-7-02'),
     (6003, 'Alpha_Properties_Hub', 6325.50, '2026-07-02')
]

# 5. The "executemany" weapon -->  Execute high-velocity bulk insertion 
# This completely blocks SQL Injection and automates rows mapping natively  
db_cursor.executemany(""" 
INSERT IGNORE INTO Customer_List (Transaction_ID, Client_Full_Name, Amount_Paid, Transaction_Date)
VALUES (%s, %s, %s, %s)                      
""", invoice_list)

# 6. Commit changes permanenlty to disk and extract the updated storage logs
db_engine.commit()

db_cursor.execute("SELECT * FROM Customer_List")
active_logs = db_cursor.fetchall()

# 7. Display the stored databasse logs onto the local console
print("Execution Success! Bulk Data Rows Injected Successfully:")
for row in active_logs:
    print(row)

# Close the secure communication block safely
db_engine.close()