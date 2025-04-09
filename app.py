import streamlit as st
import json
import pandas as pd
import os
from datetime import datetime

# Load threat data
file_path = os.path.join("threat_intel", "threat_data.json")

if os.path.exists(file_path):
    with open(file_path, "r") as f:
        raw_data = json.load(f)
    
    # Convert nested dict to list of records
    records = []
    for ip, details in raw_data.items():
        if 'timestamp' in details:
            details['timestamp'] = pd.to_datetime(details['timestamp'])
        records.append(details)

    # Create DataFrame
    df = pd.DataFrame(records)

    # Streamlit app UI
    st.set_page_config(page_title="Threat Intelligence Dashboard", layout="wide")
    st.title("🛡️ Honeypot + Threat Intelligence Dashboard")

    st.subheader("🔍 Raw JSON Preview")
    st.json(raw_data)

    st.subheader("📊 Summary Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total IPs", len(df))
    col2.metric("Unique Countries", df['country'].nunique())
    col3.metric("Organizations", df['org'].nunique())

    st.subheader("🌍 Filter by Country")
    countries = sorted(df['country'].unique())
    selected_countries = st.multiselect("Select country code(s):", countries, default=countries)

    filtered_df = df[df['country'].isin(selected_countries)]

    st.subheader("📌 Threat Data Table")
    st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

    # 🕒 Threats over time
    if 'timestamp' in df.columns:
        st.subheader("📈 Threats Over Time")
        time_df = filtered_df.copy()
        time_df['date'] = time_df['timestamp'].dt.date
        timeline = time_df.groupby('date').size().reset_index(name='attack_count')
        st.line_chart(timeline.set_index('date'))

    # 💾 Export as CSV
    st.subheader("⬇️ Export Threat Data")
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="threats.csv", mime='text/csv')

else:
    st.warning("⚠️ No data records found in the JSON file.")
