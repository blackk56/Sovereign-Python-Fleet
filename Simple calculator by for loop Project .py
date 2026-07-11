# ======================================== 
# Project 02: Hybrid Interactive For-Loop
# ======================================== 

total_audits = int(input("How many revenue streams do you want to audit today, U? "))

for i in range(total_audits):
    print(f"\n--- Audit Run {i + 1} of {total_audits} ---")
    cash = float(input(f"Enter the cash value for stream #{i + 1}: "))
    
    if cash >= 100000:
        print("--> Target Met! Sovereign HQ unlocked.")
    elif cash >= 50000:
        print("--> Halfway there. Keep grinding for Georgia.")
    else:
        print("--> Sub-par returns. Pure rat level. Stay silent.")

print("\n[SUCCESS] Fixed-range interactive audit completed.")
