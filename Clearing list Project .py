# ===================================== 
# Project 06: System Cleanup Protocols
# ===================================== 

# 1. A list of the connected devices 
active_connections = ["192.168.1.5", "Threat_Rat_01", "192.168.1.10", "Threat_Rat_02", "192.168.1.7", "192.168.1.9", "Threat_Rat_03"]
print(("Initial Active Firewall Ledger:", (len(active_connections))))

# 2. .remove() weapon: -> Deletes with the Full name (Value)
# Use when you know the exact name of the hacker and want to eliminate them immediately.
print("\n[STRIKE] Deploying .remove() to eliminate the Threats...")
active_connections.remove("Threat_Rat_01")
active_connections.remove("Threat_Rat_02")
print("Ledger Status After .remove():", active_connections)

# 3. .pop() weapon -> Deletes with its numerical sort (Index)
# Its used when you want to delete 
print("\n[STRIKE] Deploying .pop() to eject the latest connection...")
ejected_system = active_connections.pop(-1) # auto deletes the last element added to the list if let empty --> .pop()
print(f"--> Extracted and purged from system: {ejected_system}")
print("Final Clean Firewall Ledger:", active_connections)

print("\nThe remaining connected devices after the clean: ", (len(active_connections)))


