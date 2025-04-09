import streamlit as st
import sqlite3
import pandas as pd
import os
import time
from datetime import datetime
import warnings

# Suppress FutureWarning for applymap
warnings.filterwarnings("ignore", category=FutureWarning)

# Get absolute path to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "threat_data.db")

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

# Fetch data from the database
def fetch_threat_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM threat_data ORDER BY timestamp DESC")
    data = cursor.fetchall()
    conn.close()
    columns = ['ID', 'IP Address', 'Timestamp', 'Threat Type', 'Severity', 'Severity Score', 'Location', 'Source']
    return pd.DataFrame(data, columns=columns)

# Color severity_score for conditional formatting
def color_severity(val):
    if val >= 8:
        return 'background-color: red; color: white;'
    elif val >= 5:
        return 'background-color: orange; color: black;'
    else:
        return 'background-color: lightgreen; color: black;'

# Streamlit UI configuration
st.set_page_config(page_title="Threat Intelligence Dashboard", layout="wide")
st.title("🛡️ Honeypot + Threat Intelligence Dashboard")
st.markdown("Real-time monitoring of honeypot threats with severity scores and source mapping.")

# Sidebar: Auto-refresh interval and timestamp
refresh_interval = st.sidebar.selectbox("Auto-Refresh Interval (seconds)", [5, 10, 30, 60], index=1)
st.sidebar.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Fetch and display the data
df = fetch_threat_data()

# Apply conditional formatting to Severity Score column
styled_df = df.style.applymap(color_severity, subset=['Severity Score'])

# Show the styled dataframe
st.dataframe(styled_df, use_container_width=True)

# Auto-refresh after delay
time.sleep(refresh_interval)
st.rerun()
