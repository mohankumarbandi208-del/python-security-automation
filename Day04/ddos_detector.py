# Step 1: Establish System Metrics 
baseline_packets_per_sec = 1500
critical_multiplier = 3.5

# Step 2: Calculate the Security Threshold
max_allowed_packets = baseline_packets_per_sec * critical_multiplier

# Step 3: Capture Live Network Data Input
current_packets_input = int(input("Enter the current incoming traffic: "))

# Step 4: Run Threat Evaluation Logic
is_attack_active = current_packets_input >= max_allowed_packets

# Step 5: Generate the Threat Detection Dashboard
print("\n" + "="*50)
print("     GLOBAL EDGE INTRUSION DETECTION SYSTEM      ")
print("="*50)
print(f"[+] Max Allowed Threshold: {max_allowed_packets} packets/sec")
print(f"[+] Current Traffic Load : {current_packets_input} packets/sec")
print("-"*50)

if is_attack_active:
    print("🚨 ALERT: ACTIVE DDoS ATTACK DETECTED! ISOLATING ROUTING PATHS.")
else:
    print("✅ SYSTEM STATUS: NORMAL. Traffic within safe operating parameters.")

print("="*50 + "\n")
