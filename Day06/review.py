with open("network_inventory.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    data = line.split(",")
    region = data[0]
    server = data[1]
    ports = data[2].replace("-", " ")
    active_vuln = int(data[3])
    compliance = data[4].strip()

# Enforce exact structural column widths (labels width 28, values width 15)
line_region = f"{'Deployment Region:':<28}{region:>15}"
line_server = f"{'Target Server Asset:':<28}{server:>15}"
line_ports  = f"{'Exposed Ports Layer:':<28}{ports:>15}"
line_vuln   = f"{'Active Vulnerabilities:':<28}{active_vuln:>15}"
line_comp   = f"{'Compliance Posture:':<28}{compliance:>15}"

# Render the Architecture UI Dashboard
print("\n" + "="*45)
print("         GLOBAL CLOUD ASSET AUDITOR          ")
print("="*45)
print(line_region)
print(line_server)
print(line_ports)
print(line_vuln)
print(line_comp)
print("-"*45)

# Execute the Autonomous Governance Logic
if active_vuln >= 5:
    print("❌ CRITICAL RISK ALERT: Breach threshold reached!")
elif active_vuln > 2 or compliance == "NON_COMPLIANT":
    print("⚠️  HIGH-RISK WARNING: Infrastructure drift detected.")
else:
    print("✅ SYSTEM SECURE: Infrastructure is fully compliant.")

print("="*45 + "\n")
