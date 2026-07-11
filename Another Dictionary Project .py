# =========================================== 
# Project 09: Full Dynamic Dictionary Matrix
# =========================================== 

# 1. Building The Server Dictionary List
Server_Dictionary = {
    "Server Name": "Shadow_Server",
    "Server Activity": "Active",
    "Server IPA": "192.168.1.36"
}

# 2. displaying the server info
print(f"Deploying server info...", (Server_Dictionary))

# 3. The "Add" and "Update" weapon --> Adding a new Variables and its keys
Server_Dictionary.update({
    "Server Location": "Max's HQ base; Shadow Vault",
    "Server Owner": "Max",
    "Server Number": "3 Servers"
})

# 4. The For Loop for the sort
for sort in range (1):
    print(f"\nDisplaying The Updated Server info...", (Server_Dictionary))
    
# 5. The "del" weapon --> used for deleting the keys and its variables
del Server_Dictionary["Server Number"]

print(f"\nServers Final info after clearing some info...", (Server_Dictionary))

print("\nThe Server is completely finished now.")

