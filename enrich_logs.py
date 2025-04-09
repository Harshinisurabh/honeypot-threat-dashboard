import re
import json
import os
from threat_intel.threat_lookup import get_ip_info

# Path to your attack log file
log_file_path = os.path.join("logs", "attack_logs.txt")

# Read the log file and extract all IPs
with open(log_file_path, "r") as file:
    log_data = file.read()

# Use regex to find all IPv4 addresses
ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
all_ips = re.findall(ip_pattern, log_data)
unique_ips = list(set(all_ips))

print(f"🧠 Found {len(unique_ips)} unique attacker IPs.")

# Dictionary to hold enriched data
enriched_data = {}

# Enrich each IP
for ip in unique_ips:
    info = get_ip_info(ip)
    if info:
        enriched_data[ip] = info
        print(f"✅ Enriched: {ip}")
    else:
        print(f"⚠️ Skipped: {ip}")

# Save the data to a JSON file
output_path = os.path.join("threat_intel", "enriched_threat_data.json")
with open(output_path, "w") as f:
    json.dump(enriched_data, f, indent=4)

print(f"\n🚀 Enriched data saved to {output_path}")
