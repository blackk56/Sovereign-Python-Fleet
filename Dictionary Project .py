# ============================== 
# Project 08: Dictionary Matrix
# ============================== 

# 1. Master Dictionary Configuration
secure_vault = {
    "vault_id": "Vault_Shadow_01",
    "security_level": "HIGH",
    "status": "ACTIVE",
    "cam_profile": {
        "name": {
            '/-1->': "Cam_Perimeter_Beta",
            '|-2->': "Cam_Perimeter_Gamma",
            r'\-3->': "Cam_Perimeter_Alpha"
        },
        "ip_address": {
            '/-4->': "192.168.1.46",
            '|-5->': "192.168.1.50",
            r'\-6->': "192.168.1.36"
        },
        "location": {
            '/-7->': "Main HQ Door",
            '|-8->': "HQ's Mansion Gate",
            r'\-9->': "HQ's Garage"
        },
        "status": {
            '/-10->': "ACTIVE",
            '|-11->': "ACTIVE",
            r'\-12->': "ACTIVE"
        }
    }
}

# 2. Smart UI Display Tool - Builds a clean terminal interface instead of raw code lines, Note: that UI tool ain't from my made it's the ai made
def display_terminal_dashboard(vault, section_title="SYSTEM STATUS"):
    print("\n" + "═" * 75)
    print(f" 🛡️  SHADOW VAULT HQ NETWORK  ||  {section_title}")
    print("═" * 75)

    # Clean output for global server parameters
    for key, value in vault.items():
        if key != "cam_profile":
            print(f" 💾 {key.upper():<16} : {value}")

    # Clean matrix table output for nested camera profiles
    if "cam_profile" in vault:
        print("─" * 75)
        print(f" 🛰️  CONNECTED PERIMETER CAMERAS:")
        print("─" * 75)

        # Turn dict values into clean list tracks for side-by-side looping
        names = list(vault["cam_profile"]["name"].items())
        ips = list(vault["cam_profile"]["ip_address"].values())
        locs = list(vault["cam_profile"]["location"].values())
        stats = list(vault["cam_profile"]["status"].values())

        for i in range(len(names)):
            key_tag, cam_name = names[i]
            print(f"   [{key_tag}] {cam_name:<20} ➔  IP: {ips[i]:<14} | LOC: {locs[i]:<22} | {stats[i]}")

    print("═" * 75)


# 3. Execute Initial Interface
display_terminal_dashboard(secure_vault, "INITIAL SETUP")

# 4. Extracting Elements from the Nested Dictionary
target_ip = secure_vault["cam_profile"]["ip_address"]["/-4->"]
target_loc = secure_vault["cam_profile"]["location"]["/-7->"]

print(f"\n[STRIKE] Target Stream Intercepted ➔ IP: {target_ip} | Location: {target_loc}")

# 5. The .update() Weapon -> Upgrade Server and System Protocols
print("\n[UPGRADE] Injecting sovereign server protocols...")
secure_vault.update({
    "security_level": "SOVEREIGN",  
    "ip_address": "192.168.1.99"     
})
display_terminal_dashboard(secure_vault, "PROTOCOLS UPGRADED")

# 6. The del Weapon -> Immediate Clean for Specific Key
print("\n[STRIKE] Purging vault_id from active database logs...")
del secure_vault["vault_id"]  

display_terminal_dashboard(secure_vault, "PURGE COMPLETE (FINAL ARCHIVE)")


# At the end the output would look different and maybe weird but that is because the default output wouldn't be easily readable