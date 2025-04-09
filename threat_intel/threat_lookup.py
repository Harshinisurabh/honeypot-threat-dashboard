import requests

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return {
            "ip": ip,
            "city": data.get("city", "N/A"),
            "region": data.get("region", "N/A"),
            "country": data.get("country", "N/A"),
            "org": data.get("org", "N/A"),
            "loc": data.get("loc", "N/A")
        }
    except Exception as e:
        print(f"Error fetching info for IP {ip}: {e}")
        return None

# Test run
if __name__ == "__main__":
    test_ip = "8.8.8.8"  # Google DNS IP for testing
    info = get_ip_info(test_ip)
    print(info)
