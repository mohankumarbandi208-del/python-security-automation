# Day 5 Lab: Enterprise File-Driven SIEM Metrics Parser

# Step 1: Read the external data stream dynamically
with open("siem_metrices.txt", "r") as file:
    line = file.read().strip()

# Step 2: Split the raw comma-separated string into data chunks
data = line.split(",")

# Step 3: Extract and cast text items to respective numeric types
cloud_region = data[0]
curr_sec_alerts = int(data[1])
max_allow_alerts = int(data[2])
current_nw_speed = float(data[3])
max_nw_speed = float(data[4])
system_status = data[5]

# Step 4: Calculate environmental capacity consumption ratios
alert_percentage = (curr_sec_alerts / max_allow_alerts) * 100
nw_percentage = (current_nw_speed / max_nw_speed) * 100

# Step 5: Format layout columns with strict alignment matrix wrappers
# Labels are left-aligned with width 30. Values are right-aligned with width 15.
line_region = f"{'Deployment Cloud Zone:':<30}{cloud_region:>15}"
line_alerts = f"{'Active Incident Count:':<30}{f'{curr_sec_alerts}/{max_allow_alerts}':>15}"
line_pct    = f"{'Alert Threshold Capacity:':<30}{f'{alert_percentage:.1f}%':>15}"
line_net    = f"{'Throughput Consumption:':<30}{f'{nw_percentage:.2f}%':>15}"
line_status = f"{'System Integrity State:':<30}{system_status:>15}"

# Step 6: Render UI Dashboard Interface
print("\n" + "="*48)
print("       📊 AUTONOMOUS AGENT METRICS MONITOR      ")
print("="*48)
print(line_region)
print(line_alerts)
print(line_pct)
print(line_net)
print(line_status)
print("-"*48)

# Step 7: Continuous Autonomous Gate Logic Execution
if curr_sec_alerts >= max_allow_alerts:
    print("❌ CRITICAL FAULT: Incident limits breached!")
elif nw_percentage >= 80 or system_status == "DEGRADED":
    print("⚠️  HIGH RISK MODE: Operational anomalies detected.")
else:
    print("✅ GREEN PARAMETERS: Infrastructure baseline normal.")

print("="*48 + "\n")
