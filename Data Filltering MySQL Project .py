# =============================================================
# Project 16: Production Data Automation & SQL Data Filltering 
# =============================================================

import mysql.connector # UPGRADED: Using official Enterprise MySQL database engine connection drivers

# 1.  Connect to the local secure database engine on the disk
db_engine = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="Secure_Enterprise_Password_165"
)
db_cursor = db_engine.cursor() 

# 2.  create and select the target database vault before building tables
db_cursor.execute("CREATE DATABASE IF NOT EXISTS Sales_Vault")
db_cursor.execute("USE Sales_Vault")


# 3. The "WHERE" Clause Weapon --> Perform a sovereign filter to the Database Table
db_cursor.execute("""
    SELECT * FROM Customer_List
    WHERE Transaction_ID = 6001                  
 """)  # here we filter the sort to show only the results of the typed info, which in our case the Transaction id search, so it will get the full info from the table list about the typed fitler name


high_value_invoices = db_cursor.fetchall()
for row in high_value_invoices:
    print(row)

# 4. Combining ORDER BY and LIMIT to isolate the single highest Result in the table 
db_cursor.execute("""
   SELECT Client_Full_Name, Amount_Paid FROM Customer_List
   ORDER BY Amount_Paid DESC
   LIMIT 1
 """)
top_alpha_invoice = db_cursor.fetchone() # Fetches only one single tuple row
print(top_alpha_invoice)

# Close the secure communication block safely
db_cursor.close()


