
with open("test-file.txt", "r") as file :
    lines = file.readlines()

leak = False
for line in lines:
    if "AWS_SECRET_KEY" in line :
        print("Yes Lead detected ", line)
        leak = True

if not leak:
    print("[+] Credentials are safe No leak detected")