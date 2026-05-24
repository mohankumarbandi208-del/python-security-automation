raw_log = "  2026-05-24 07:45:12 | STATUS:BLOCKED | SRC_IP:192.168.1.105 | REASON:Malicious_Traffic  "

# Fix 1: Clean the boundaries first
clear_log = raw_log.strip()

# Fix 2: Split the CLEAN log using " | " to eliminate padding spaces
log_segments = clear_log.split(" | ")

time_stamp = log_segments[0]
status = log_segments[1].replace("STATUS:", "")
src_ip = log_segments[2].replace("SRC_IP:", "")

# Fix 3: Chain the underscore replacement and add .strip() to clean up hidden spaces
reason = log_segments[3].replace("REASON:", "").replace("_", " ").strip()

# Print Block (Your printing logic is absolutely perfect!)
print("\n" + "="*50)
print("         GLOBAL INCIDENT RESPONSE TRACKER        ")
print("="*50)
print(f"[!] Alert Time: {time_stamp}")
print(f"[!] Source IP : {src_ip}")
print(f"[!] Action    : {status}")
print(f"[!] Trigger   : {reason.upper()}")
print("="*50 + "\n")
