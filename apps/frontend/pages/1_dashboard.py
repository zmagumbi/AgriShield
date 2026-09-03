import os
import streamlit as st
import requests

# Dynamically fetch BACKEND_URL from Streamlit Cloud Secrets, falling back to Render
BACKEND_URL = st.secrets.get("BACKEND_URL") or os.getenv("BACKEND_URL", "https://agrishield-dnao.onrender.com")
API_KEY = st.secrets.get("API_KEY") or os.getenv("API_KEY", "")

st.title("🌾 AgriShield: Agricultural Risk Intelligence")

# 1. Input Controls for Users
selected_county = st.selectbox(
    "Select County",
    ["Kajiado", "Uasin Gishu", "Nakuru", "Kilifi"]
)
sector = st.radio("Select Risk Area", ["Crops", "Livestock Forage"])

# 2. Trigger Prediction Button
if st.button("Generate Risk Prediction"):
    with st.spinner("Fetching predictions and Gria AI analysis..."):
        try:
            payload = {"county": selected_county, "sector": sector}
            headers = {"X-API-Key": API_KEY} if API_KEY else {}
            
            response = requests.post(f"{BACKEND_URL}/predictions/", json=payload, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                st.success(f"Risk Score: {data.get('risk_score', 'N/A')}")
                st.subheader("🤖 Gria AI Analysis")
                st.write(data.get("gria_summary", "No AI analysis available."))
            else:
                st.error("Failed to fetch prediction from backend server.")
                
        except Exception as e:
            st.error(f"Cannot connect to backend server. Make sure FastAPI is running. Error: {e}")
