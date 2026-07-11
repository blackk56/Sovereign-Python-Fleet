# ==============================================================
# Project 15: MySQL Database with Python; Create Table Database
# ==============================================================


import mysql.connector # UPGRADED: Using official Enterprise MySQL database engine connection drivers


# 1. Connect to the public server first without specifying a database
engine = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="Secure_Enterprise_Password_165"
)
cursor = engine.cursor()

# 2.  create and select the target database vault before building tables
cursor.execute("CREATE DATABASE IF NOT EXISTS Enterprise_Billing_Vault")
cursor.execute("USE Enterprise_Billing_Vault")

# 3. Creating a table in the database
cursor.execute('''CREATE TABLE IF NOT EXISTS Invoice          
      (invoice_ID INT,  
      Customer_Name VARCHAR(100), 
      Pay_Date DATE)'''
);

# 4. Save the changes made to the database
engine.commit()

# 5. Shows The Table Information
cursor.execute('SELECT * FROM Invoice');

# At the end it will print a clean empty list [] because no data is injected yet
print(cursor.fetchall())

engine.close()
