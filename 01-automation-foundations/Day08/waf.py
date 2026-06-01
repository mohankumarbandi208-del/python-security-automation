payload = input("Enter the log")
if "<script>" in payload and  len(payload)>40:
    threat_level = "CRITICAL"
elif "SELECT" in payload or "UNION" in payload or "<script>" in payload and len(payload)> 45:
    threat_level = "HIGH RISK"

else:
    threat_level = "Clean"

print("="*40)
print(f"{'Threat_level :' :<26} {threat_level :>16}")

print("\n", "="*40 )