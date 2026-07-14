# ==================================== 
#  Project 07: Multi-Dimensional List
# ==================================== 

# 1. Build a servers info list 
# Every List in the menu contain: [Server's Name, IP Addresses, Safety Status]
server_matrix = [
    ["Server_Alpha", "192.168.1.1", "SECURED"],
    ["Server_Beta",  "192.168.1.2", "SECURED"],
    ["Server_Gamma", "192.168.1.3", "SECURED"],
    ["Server_Delta",  "192.168.1.4", "COMPROMISED"],
    ["Server_Zelta", "192.168.1.5", "SECURED"],
    ["Server_Zeta",  "192.168.1.6", "SECURED"]
]

print(f"Full Grid Security Status: {len(server_matrix)}: \n")

print("[SECURITY PROTOCOL ACTIVATED] Scanning all lines for compromises...")

# The For Loop: automatically parses the matrix and scans index 2 of each row
for check in server_matrix:
    if check[2] == "COMPROMISED":
        print(f"--> [ALERT - BREACH DETECTED] !!! Target: {check[0]} (IP: {check[1]}) is HACKED!")
    else:
        print(f"--> [CLEAN] {check[0]} (IP: {check[1]}) is Safe.")

print("\n[SUCCESS] Full grid scan operations completed.")
