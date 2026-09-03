import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

# Backend configuration
BACKEND_URL = https://agrishield-dnao.onrender.com/
st.set_page_config(page_title="County Risk Map", page_icon="🗺️", layout="wide")

st.title("🗺️ Kenya Agricultural Risk Map")
st.write("Interactive spatial visualization of crop yield shocks and livestock forage deficits across counties.")

# Sample county coordinates and mock risk levels for map rendering
COUNTY_DATA = [
    {"county": "Kajiado", "lat": -1.8523, "lon": 36.7768, "risk": "High Risk", "color": "red", "score": "82%"},
    {"county": "Uasin Gishu", "lat": 0.5143, "lon": 35.2698, "risk": "Low Risk", "color": "green", "score": "15%"},
    {"county": "Nakuru", "lat": -0.3031, "lon": 36.0800, "risk": "Moderate Risk", "color": "orange", "score": "48%"},
    {"county": "Kilifi", "lat": -3.5107, "lon": 39.9093, "risk": "High Risk", "color": "red", "score": "76%"},
]

# Create Folium Map centered on Kenya
m = folium.Map(location=[0.0236, 37.9062], zoom_start=6, tiles="OpenStreetMap")

# Add County Risk Markers
for item in COUNTY_DATA:
    folium.Marker(
        location=[item["lat"], item["lon"]],
        popup=f"<b>{item['county']}</b><br>Status: {item['risk']}<br>Risk Score: {item['score']}",
        tooltip=f"{item['county']} ({item['risk']})",
        icon=folium.Icon(color=item["color"], icon="info-sign")
    ).add_to(m)

# Render Map in Streamlit
st_data = st_folium(m, width=900, height=500)

st.markdown("""
**Legend:**
* 🔴 **Red Marker:** High Risk (Immediate Action Required)
* 🟠 **Orange Marker:** Moderate Risk (Monitor Closely)
* 🟢 **Green Marker:** Low Risk (Stable Conditions)
""")
