payload = input("📡 [WAF-INGEST] Enter incoming payload string: ")

# Target 1: Critical Scripting Detections
if "<script>" in payload and len(payload) > 45:
    threat_level = "CRITICAL"

# Target 2: Explicit Database Queries or Compact Exploits
elif "SELECT" in payload or "UNION" in payload or "<script>" in payload:
    threat_level = "HIGH RISK"

# Target 3: Verified Parameters
else:
    threat_level = "CLEAN"

# Visual Output Table (Enforcing your 26 and 16 space padding matrix rules)
print("\n" + "="*43)
print("          APPLICATION SHIELD REGISTRY        ")
print("="*43)
print(f"{'Analyzed Payload Length:':<26}{len(payload):>16}")
print(f"{'Evaluated Threat State:':<26}{threat_level:>16}")
print("="*43 + "\n")
