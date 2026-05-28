# Phase 1: Establish Fallback Default Values
DEFAULT_IP = "127.0.0.1"
DEFAULT_PORTS = "22, 80, 443, 445"
DEFAULT_SCORE = 4.0

# Phase 2: Capture Interactive User Inputs
user_ip = input(f"Enter the target IP (Press Enter for default {DEFAULT_IP}): ")
user_ports = input(f"Enter the opened ports (Press Enter for default {DEFAULT_PORTS}): ")
raw_score = input(f"Enter the CVSS score (Press Enter for default {DEFAULT_SCORE}): ")

# Use fallback logic if inputs are left blank
server_ip = user_ip if user_ip.strip() else DEFAULT_IP
open_ports = user_ports if user_ports.strip() else DEFAULT_PORTS
vulnerability_score = float(raw_score) if raw_score.strip() else DEFAULT_SCORE

# Phase 3: Risk Level Logic Execution
if vulnerability_score >= 7.0:
    risk_level = "HIGH Risk"
elif vulnerability_score >= 4.0:
    risk_level = "MEDIUM Risk"
else:
    risk_level = "LOW Risk"

# Phase 4: Clean Enterprise-Formatted Reporting
print("\n" + "="*45)
print("         SECURE ARCHITECTURE REPORT          ")
print("="*45)
print(f"[+] Target Host  : {server_ip}")
print(f"[+] Open Ports   : {open_ports}")
print(f"[!] Risk Category: {risk_level} (Score: {vulnerability_score})")
print("="*45 + "\n")
