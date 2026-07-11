# =============================================================================================
# The last MySQL learning Projcet 19: Automated CSV External Data Extraction & SQL Pipeline
# =============================================================================================

import csv
import mysql.connector # UPGRADED: Using official Enterprise MySQL database engine connection drivers

# 1.  Connect to the local secure database engine on the disk
db_engine = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="Secure_Enterprise_Password_165"
)
db_cursor = db_engine.cursor()

# 2.  create and select the target database vault before building tables
db_cursor.execute("CREATE DATABASE IF NOT EXISTS enterprise_vault")
db_cursor.execute("USE enterprise_vault")

# 3. Build the secure database table structure with verified constrains
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS Client_Invoices (
    Invoice_ID INT PRIMARY KEY,
    Client_Name VARCHAR(150),
    Sales_Value REAL
)
""")


# 4. Open the corrected external CSV spreadsheet file safely
with open('Invoices_List.csv', mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # Skip the text header row safely


    # 5. Loop through the 10 corporate rows and inject into the database vault
    for row in csv_reader:
        if not row or len(row) < 3: # The Sanitization Shield: Ignores empty or corrupted trailing rows
            continue

        inv_id, name, value = row
        
        # The inevitable line of defense: Skip the text headings to prevent ValueError
        if inv_id == 'Invoice_ID' or not inv_id.strip().isdigit():
            continue

        db_cursor.execute("""
        INSERT IGNORE INTO Client_Invoices (Invoice_ID, Client_Name, Sales_Value)
        VALUES (%s, %s, %s)
        """, (int(inv_id), name, float(value)))


db_engine.commit() # Flush and lock the rows permanently on hard disk



# 6. Extract from SQL and format output straight into a fresh clean CSV/Excel Handshake
print("--- Final Verified Invoices Ingested Natively From The CSV Spreadsheet ---")
db_cursor.execute("SELECT * FROM Client_Invoices ORDER BY Sales_Value DESC")
final_clean_row = db_cursor.fetchall()


# 7. writing out the pure certified results into an independent verified report file
with open ('Final_Corporate_Report.csv', mode = 'w', newline = '') as output_file:
    csv_writer = csv.writer(output_file) 
    csv_writer.writerow(['Invoice_ID', 'Client_Name', 'Sales_Value']) # Write brand new header
    csv_writer.writerows(final_clean_row) # Stamp all the cleaned database records inside



db_engine.close()
