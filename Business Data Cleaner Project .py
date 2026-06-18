# ===================================================================================
# Project 13: Sovereign Business Data Cleaner & Ledger Automator
# Target Client Matrix: Small business automation (FreeLance Asset)
# ===================================================================================


# -----------------------------------------------------------------------------------
# 1. Invoice Metrics & Business profiles And Spam logs
# -----------------------------------------------------------------------------------

# Invoice Metrics Multi-Dimensional [Invoice Number, Client Name, Sales Value, Payment Status]
raw_invoice_metrics = [
    ["INV-01", "Client_Beta",  3780.0, "Paid"],
    ["INV-02", "Client_Delta", 1640.0, "Paid"],
    ["INV-03", "Client_Gamma", 5760.0, "Pending"],
    ["INV-04", "Client_Alpha", 4820.0, "Pending"],
    ["INV-05", "Client_Zeta",  6870.0, "Paid"],
    ["INV-06", "Client_Gamma", 5760.0, "Paid"],
    ["INV-07", "Client_Delta", 1640.0, "Paid"],
    ["INV-08", "Client_Omega", 1240.0, "Pending"],
    ["INV-09", "Client_Beta",  3780.0, "Paid"]
]

# Dictionary of nested Business & Tax Profiles in the system
business_metadata = {
    "Store_Config": {
        "Store_ID": "Retail-Core-System",
        "Tax_Rate": 0.01,
        "Currency": "USD"
    }
}

# History Logs of spam accounts (Set auto-removes duplicates)
spam_accounts_Logs = {
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
cleaned_invoice_ledger = []
total_raw_revenue = 0.0

# The for loop; Scans the lines one by one, for mechanical Cleaning
for invoice in raw_invoice_metrics:
    try:
        # Float Security Shield: check sales value integrity
        invoice_value = float(invoice[2])

        # Calculating total gross revenues
        total_raw_revenue += invoice_value

        # Smart duplicate check based on full invoice matching
        is_duplicate = False
        for clean_invoice in cleaned_invoice_ledger:
            if clean_invoice == invoice:
                is_duplicate = True
                break

        if not is_duplicate:
            cleaned_invoice_ledger.append(invoice)
        else:
            print(f"--> [Purged Threat] Duplicate Entry Discovered and Destroyed: {invoice[0]} | {invoice[1]}")

    except (ValueError, TypeError):
        # Silently catch and contain corrupt data without system collapse
        print(f"🚨 [MALFORMED DATA BLOCK] Alert! Invoice {invoice[0]} contains corrupt sales value '{invoice[2]}'. Dropping target for system safety.")
        continue

print(f"\n[Cleaning Complete] Unique Invoices Isolated: {len(cleaned_invoice_ledger)} / {len(raw_invoice_metrics)}")


# 3. Accessing the integrated dictionary to automatically extract tax rates and calculate net profits
tax_percentage = business_metadata["Store_Config"]["Tax_Rate"]
total_clean_revenue = 0.0

for clean_invoice in cleaned_invoice_ledger:
    total_clean_revenue += clean_Invoice[2]

calculated_tax_pool = total_clean_revenue * tax_percentage
net_sovereign_profile = total_clean_revenue - calculated_tax_pool


# 4. Presenting the final impressive financial outputs and reports to the client
print("\n===================================================================================")
print("=== Final Sovereign Financial Balance Sheet ===")
print("===================================================================================")
print(f"--> Total Raw Input Revenue (With Errors): ${total_raw_revenue}")
print(f"--> Total Clean Audit Revenue (Cleaned): ${total_clean_revenue}")
print(f"--> Automated Tax Deduction Pool (1% Tax): ${calculated_tax_pool}")
print(f"--> Net Sovereign Profit Secured (CASH): ${net_sovereign_profile}")
print("===================================================================================\n")


# ------------------------------------------------------------------------------------------------
# 5. File Read & Creation; Create And Read the Sovereign Business File
# ------------------------------------------------------------------------------------------------

file_path = "sovereign_financial_report.txt"

try:
    with open(file_path, "w") as creation_file:
        creation_file.write("=== Sovereign Invoice Logs Installed Successfully ===\n")
        creation_file.write(f"\n--> Total Raw Input Revenue (With Errors): ${total_raw_revenue}")
        creation_file.write(f"\n--> Total Clean Audit Revenue (Cleaned): ${total_clean_revenue}")
        creation_file.write(f"\n--> Net Sovereign Profit Secured (CASH): ${net_sovereign_profile}\n")


# Injecting the Sets sorting system and automatically eliminating spam bots, then writing them in the report
        creation_file.write("\n=====================================================================\n")
        
        creation_file.write(f"--> Isolated Unique Spam Attack Signatures:    {list(spam_accounts_logs)}\n")
        creation_file.write("=====================================================================")

    print("--> [SUCCESS] Ultimate Financial & Security Report Written Permanently to Disk.")

except OSError:
    print("Something went wrong while writing the file.")

try:
    with open(file_path, "r") as check_file:
        scan_drive = check_file.read()
    print("The File is being fully scanned...\n")
    print(f"Results: {scan_drive}")
except FileNotFoundError:
    print("Couldn't locate any file with that name.")
