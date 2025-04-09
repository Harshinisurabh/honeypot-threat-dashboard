import folium
from threat_intel.data_fetcher import get_threat_data
from threat_intel.severity import calculate_severity

def get_marker_color(severity):
    if severity >= 7:
        return 'red'
    elif severity >= 4:
        return 'orange'
    else:
        return 'green'

def generate_map():
    data = get_threat_data()
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=2)

    for entry in data:
        # Extract needed values
        attempts = entry.get("failed_attempts", 0)
        reputation = entry.get("reputation", 0)
        attack_type = entry.get("attack_type", "Unknown")

        severity = calculate_severity(attempts, reputation, attack_type)
        color = get_marker_color(severity)

        folium.CircleMarker(
            location=entry["location"],
            radius=10,
            popup=(
                f"IP: {entry['ip']}<br>"
                f"Attempts: {attempts}<br>"
                f"Reputation: {reputation}<br>"
                f"Type: {attack_type}<br>"
                f"<b>Severity:</b> {severity}/10"
            ),
            color=color,
            fill=True,
            fill_color=color
        ).add_to(m)

    m.save("threat_map.html")
    print("✅ Map saved as threat_map.html")

if __name__ == "__main__":
    generate_map()
