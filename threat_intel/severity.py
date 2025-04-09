# threat_intel/severity.py

def calculate_severity(failed_attempts, reputation, attack_type):
    score = 0

    if failed_attempts > 5:
        score += 3
    if reputation < 50:
        score += 2
    if attack_type == "brute_force":
        score += 4

    return score

# ✅ TEST BLOCK: Add this if not present
if __name__ == "__main__":
    print(calculate_severity(7, 45, "brute_force"))  # Expected: 9
    print(calculate_severity(3, 60, "scan"))         # Expected: 0
    print(calculate_severity(9, 30, "scan"))         # Expected: 5
