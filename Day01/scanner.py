# Open the target file safely
with open("test-file.txt", "r") as file:
    lines = file.readlines()

leak = False

# Iterate and scan for compromised infrastructure keys
for line in lines:
    if "AWS_SECRET_KEY" in line:
        # Use .strip() to clean up trailing whitespace/newlines in the output log
        print("[!] CRITICAL: Security leak detected ->", line.strip())
        leak = True

# Final compliance check statement
if not leak:
    print("[+] Compliance Check Pass: Credentials are safe, no leak detected.")
