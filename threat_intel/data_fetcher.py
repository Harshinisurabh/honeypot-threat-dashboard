# threat_intel/data_fetcher.py

import random

def get_threat_data():
    # Simulated IP threat data
    data = [
        {
            "ip": "192.168.1.10",
            "location": [28.6139, 77.2090],  # Delhi, India
            "failed_attempts": random.randint(1, 10),
            "reputation": random.randint(10, 100),
            "attack_type": "brute_force"
        },
        {
            "ip": "10.0.0.5",
            "location": [40.7128, -74.0060],  # New York, USA
            "failed_attempts": random.randint(1, 10),
            "reputation": random.randint(10, 100),
            "attack_type": "scan"
        },
        {
            "ip": "172.16.0.20",
            "location": [51.5074, -0.1278],  # London, UK
            "failed_attempts": random.randint(1, 10),
            "reputation": random.randint(10, 100),
            "attack_type": "brute_force"
        }
    ]
    return data
if __name__ == "__main__":
    threats = get_threat_data()
    for t in threats:
        print(t)
