# =========================================== 
# Project 04: Dynamic Asset Injection Ledger
# =========================================== 

# 1. Establishing the initial headquarters list
secured_assets = ["HQ Land", "Server Cluster Alpha", "Mini-HQ House"]
print("Initial Operational Assets:", secured_assets)

# 2. Dynamically injecting and expanding the menu using.append()
print("\n[UPGRADE] Injecting new tactical defense assets...")
secured_assets.append("G-System")
secured_assets.append("G-Protocols")
secured_assets.append("G-Main-HQ")

# 3. Enforce strict alphabetical order using.sort()
secured_assets.sort()
print(f"Total Sorted Assets Found: {len(secured_assets)}\n")

# 4. The for loop
for asset in secured_assets:
    print(f"--> [SECURED]: {asset}")

# 5. The Conditional Defence line
target_assets_is_secured = True

if target_assets_is_secured:
    print("\n[STATUS] Perimeter integrity verified. Continue proceeding.")
else:
    print("\n[CRITICAL] Security compromise detected! Deploying Protocol 03.")
