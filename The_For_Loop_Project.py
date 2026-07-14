# ==================================== 
# Project 03: Advanced Server Auditor
# ==================================== 

# 1. taking the amount of servers needed to be checked tonight
total_servers = int(input("Enter number of servers to audit, G: "))

for server_id in range(1, total_servers + 1):
    print(f"\n--- Activating Scan on Server #{server_id} ---")

    # 2. checking threat level inside the server
    threat_level = int(input(f"Enter Threat Level for Server #{server_id} (0 to 100): "))

    # 3. "continue" weapon: if the server is compeletly safe, moves immediately to the next server without wasting time
    if threat_level == 0:
        print(f"--> Server #{server_id} is Clean. Skipping further checks.")
        continue # moves immediately to the next server Loop and skips the rest of the codes below

    # 4. "break" weapon: if it discoveres a chaos attack (more than 90), closes the entire operation immediately
    elif threat_level > 90:
        print(f"[CRITICAL BREACH] Server #{server_id} Compromised! Activating Total Lockdown (03).")
        break # breaks the loop entierly and close the program

    # 5. handles mid attacks
    elif threat_level >= 50 and threat_level <= 90:
        print("--> Status: HIGH RISK. Deploying automated firewalls.")

    elif threat_level > 0 and threat_level < 50:
        print("--> Status: LOW RISK, Enabling Protoccol LOW_RATE is requiered ")
    
    else:
        print("--> Status: Unknown RISK. Caution is required.")

print("\n[PROCESS ENDED] Audit sequence completed.")
