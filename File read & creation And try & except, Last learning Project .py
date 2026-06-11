# ==================================================================== 
# The last learning Project 12: File Read & Creation And try & except
# ====================================================================

# 1. Type the file path
File_Path = "I O File & try, except  Project .py"

# 2. The with & open Weapon --> Used to read the file or edit it or delete it or even create it
try:   
    with open(File_Path, "x") as Creation_File:
        Creation_File.write("=== Py File is installed successfully ===\n")
        
        Creation_File.write("Status: The Shadow Vault is clear and safe\n")
        
except FileExistsError:
    print("File already exist")

print("[Success] Tactical logs created and saved permanetly to your disk\n")


# 3. The try & Except Weapon --> Handles the error code's messages so the pc don't crash
try:
    with open(File_Path, "r") as Check_File: # Try to check with a fake file name
        Scan_Drive = Check_File.read()
    print("The Drive is being fully scanned...\n")
    print(f"Results: {Scan_Drive}")

except FileNotFoundError:
    print("No File detected, Please make sure of what you are looking for and try again.")



