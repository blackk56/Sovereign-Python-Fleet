# ==============================================================================
# Project 19: Enterprise Medical CRM & Diagnostic Asset Ingestion Engine
# Target Client Matrix: Healthcare Facility Resource Management 
# ==============================================================================

import csv
import mysql.connector # UPGRADED: Using official Enterprise MySQL database engine connection drivers

# 1.  Initialize local relational storage database wrapper
db_engine = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="Secure_Enterprise_Password_165"
)
db_cursor = db_engine.cursor()

# 2.  create and select the target database vault before building tables
db_cursor.execute("CREATE DATABASE IF NOT EXISTS Medical_Operations_Vault")
db_cursor.execute("USE Medical_Operations_Vault")


# Purge legacy table schema and enforce fresh structural initialization
db_cursor.execute("DROP TABLE IF EXISTS Diagnostic_Inventory")

# 3. Build multi-typed corporate table infrastructure with composite UNIQUE shield
db_cursor.execute("""
CREATE TABLE Diagnostic_Inventory (
    Item_Code VARCHAR(100),
    Equipment_Name VARCHAR(150),
    Stock_Count INT,
    Unit_Value REAL,
    Safety_Status VARCHAR(50),
    UNIQUE(Item_Code, Equipment_Name, Unit_Value)
)
""")

# 4. Open the external raw medical csv ledger and process input strings safely
with open('medical_raw_stock.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # Overleap text column headers to insulate integer parsing loop
    
    # 5. Ingestion stream loop executing dynamic parsing validations
    for row in csv_reader:
        if not row or len(row) < 5: # Guard Shield 1: Bypasses blank trailing garbage
            continue
            
        code, name, count, val, status = row
        
        # Guard Shield 2: Bypasses corrupted text strings within number allocations
        if not count.strip().isdigit():
            continue
            
        # Parametric insertion writing verified records permanently to database memory
        db_cursor.execute("""
        INSERT IGNORE INTO Diagnostic_Inventory (Item_Code, Equipment_Name, Stock_Count, Unit_Value, Safety_Status)
        VALUES (%s, %s, %s, %s, %s)
        """, (code, name, int(count), float(val), status))

db_engine.commit() # Flush raw cached data inputs permanently down to hard disk sectors

# 6. Multi-Conditional Server-Side Analytical Math Interrogation
db_cursor.execute("""
SELECT Item_Code, Equipment_Name, (Stock_Count * Unit_Value) AS Asset_Valuation
FROM Diagnostic_Inventory 
WHERE Safety_Status = 'Critical' OR Stock_Count <= 3
ORDER BY Asset_Valuation DESC
""")
critical_financial_report = db_cursor.fetchall()

# 7. Deliverable Presentation Export Handshake Layer
with open('Clean_Medical_Asset_Report.csv', mode='w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['Item_Code', 'Equipment_Name', 'Total_Asset_Valuation'])
    csv_writer.writerows(critical_financial_report) # Stamp the calculated analytical matrices

db_engine.close() # Securely close backend portal connection lines
