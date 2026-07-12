# ===================================================================================
# Project 14: Sovereign Business Data Cleaner & Ledger Automator
# Target Client Matrix: Small business automation (FreeLance Asset)
# New Update: Injecting SQL Database System
# ===================================================================================

import sqlite3 # INJECTED: The local relational database engine pipeline

# -----------------------------------------------------------------------------------
# 1. Invoice Metrics & Business profiles And Spam logs
# -----------------------------------------------------------------------------------

# Invoice Metrics Multi-Dimensional [Invoice Number, Client Name, Sales Value, Payment Status]
Raw_Invoice_Metrics = [
    ["INV-01", "Client_Beta",  3780.0, "Paid"],
    ["INV-02", "Client_Delta", 1640.0, "Paid"],
    ["INV-03", "Client_Gamma", 5760.0, "Pending"],
    ["INV-04", "Client_Alpha", 4820.0, "Pending"],
    ["INV-05", "Client_Zeta",  6870.0, "Paid"],
    ["INV-06", "Client_Gamma", 5760.0, "Pending"],
    ["INV-07", "Client_Delta", 1640.0, "Paid"],
    ["INV-08", "Client_Omega", 1240.0, "Pending"],
    ["INV-01", "Client_Beta",  3780.0, "Paid"]
]

# Dictionary of nested Business & Tax Profiles in the system
Business_Metadata = {
    "Store_Config": {
        "Store_ID": "Retail-Core-System",
        "Tax_Rate": 0.01,
        "Currency": "USD"
    }
}

# History Logs of spam accounts (Set auto-removes duplicates)
Spam_Accounts_Logs = {
    "Acc-36", "Hacker_Bot_01", "Hacker_Bot_02", "Acc-23"
}


# ---------------------------------------------------------------------------------------
# 2. Injection of smart functional Weapons (def) & Automated inspection and disinfection
# ---------------------------------------------------------------------------------------

def execute_ledger_cleansing_scan():
    print("=======================================================================")
    print("[System Core] Launching Automated Data Cleansing Perimeter Scan...")
    print("=======================================================================\n")

execute_ledger_cleansing_scan()

# New sub menu to store pure and unique invoices after eliminating duplications
Cleaned_Invoice_Ledger = []
Total_Raw_Revenue = 0.0

# The for loop; Scans the lines one by one, for mechanical Cleaning
for invoice in Raw_Invoice_Metrics:
    try:
        # Float Security Shield: check sales value integrity
        invoice_value = float(invoice[2])

        # Calculating total gross revenues
        Total_Raw_Revenue += invoice_value

        # Smart duplicate check based on full invoice matching
        is_duplicate = False
        for clean_invoice in Cleaned_Invoice_Ledger:
            if clean_invoice == invoice:
                is_duplicate = True
                break

        if not is_duplicate:
            Cleaned_Invoice_Ledger.append(invoice)
        else:
            print(f"--> [Purged Threat] Duplicate Entry Discovered and Destroyed: {invoice[0]} | {invoice[1]}")

    except (ValueError, TypeError):
        # Silently catch and contain corrupt data without system collapse
        print(f"🚨 [MALFORMED DATA BLOCK] Alert! Invoice {invoice[0]} contains corrupt sales value '{invoice[2]}'. Dropping target for system safety.")
        continue

print(f"\n[Cleaning Complete] Unique Invoices Isolated: {len(Cleaned_Invoice_Ledger)} / {len(Raw_Invoice_Metrics)}")


# 3. Accessing the integrated dictionary to automatically extract tax rates and calculate net profits
Tax_Percentage = Business_Metadata["Store_Config"]["Tax_Rate"]
Total_Clean_Revenue = 0.0

for Clean_Invoice in Cleaned_Invoice_Ledger:
    Total_Clean_Revenue += Clean_Invoice[2]

Calculated_Tax_Pool = Total_Clean_Revenue * Tax_Percentage
Net_Sovereign_Profile = Total_Clean_Revenue - Calculated_Tax_Pool


# 4. Presenting the final impressive financial outputs and reports to the client
print("\n===================================================================================")
print("=== Final Sovereign Financial Balance Sheet ===")
print("===================================================================================")
print(f"--> Total Raw Input Revenue (With Errors): ${Total_Raw_Revenue}")
print(f"--> Total Clean Audit Revenue (Cleaned): ${Total_Clean_Revenue}")
print(f"--> Automated Tax Deduction Pool (1% Tax): ${Calculated_Tax_Pool}")
print(f"--> Net Sovereign Profit Secured (CASH): ${Net_Sovereign_Profile}")
print("===================================================================================\n")


# ------------------------------------------------------------------------------------------------
# 5. File Read & Creation; Create And Read the Sovereign Business File
# ------------------------------------------------------------------------------------------------

# Injecting MySql: create database and table schema
db_engine = sqlite3.connect('Sovereign_Assets.db')
db_cursor = db_engine.cursor()

# Drop the table if it exists to ensure fresh schema
db_engine.execute("DROP TABLE IF EXISTS Clean_Ledger_Vault")

db_engine.execute("""
CREATE TABLE IF NOT EXISTS Clean_Ledger_Vault (
     Invoice_Num TEXT PRIMARY KEY,
     Client_Name TEXT,
     Sales_Value REAL,
     Payment_Status TEXT,
     UNIQUE(Client_Name, Sales_Value, Payment_Status) 
)
""")

# INJECTED: High-velocity loop iteration to populate the secure SQL database vault permanently
for item in Cleaned_Invoice_Ledger:
    db_cursor.execute("""
    INSERT OR IGNORE INTO Clean_Ledger_Vault (Invoice_Num, Client_Name, Sales_Value, Payment_Status)
    VALUES (?, ?, ?, ?)
    """, (item[0], item[1], float(item[2]), item[3]))

db_engine.commit()  # Lock the database records permanently on hard disk storage

# INJECTED: Quick Verification Audit to read live entries directly from the SQL engine
print("--- [Live SQL Audit] Reading Clean Invoices Saved Permanently to Hard Disk ---")
db_engine.execute("SELECT * FROM Clean_Ledger_Vault ORDER BY Sales_Value DESC")
for db_row in db_cursor.fetchall():
    print(db_row)
print("===================================================================================\n")

db_engine.close() # Close database portal safely

# [Original File Logic Intact]: Writing report backup natively to plain text on disk
File_Path = "sovereign_financial_report.txt"

try:
    with open(File_Path, "w") as Creation_File:
        Creation_File.write("=== Sovereign Invoice Logs Installed Successfully ===\n")
        Creation_File.write(f"\n--> Total Raw Input Revenue (With Errors): ${Total_Raw_Revenue}")
        Creation_File.write(f"\n--> Total Clean Audit Revenue (Cleaned): ${Total_Clean_Revenue}")
        Creation_File.write(f"\n--> Net Sovereign Profit Secured (CASH): ${Net_Sovereign_Profile}\n")
# Injecting the Sets sorting system and automatically eliminating spam bots, then writing them in the report
        Creation_File.write("\n=======================================================================================================\n")
        Creation_File.write(f"--> Isolated Unique Spam Attack Signatures:    {list(Spam_Accounts_Logs)}\n")
        Creation_File.write("=======================================================================================================")
    print("--> [SUCCESS] Ultimate Financial & Security Report Written Permanently to Disk.")
except OSError:
    print("Something went wrong while writing the file.")

try:
    with open(File_Path, "r") as Check_File:
        Scan_Drive = Check_File.read()
    print("The File is being fully scanned...\n")
    print(f"Results: {Scan_Drive}")
except FileNotFoundError:
    print("Couldn't locate any file with that name.")
