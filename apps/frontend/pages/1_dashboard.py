import streamlit as st
import requests

# Set backend URL (Local URL for testing, replace with live Render URL later)
BACKEND_URL = st.secrets.get("BACKEND_URL") or os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

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
            # Send inputs to backend prediction endpoint
            payload = {"county": selected_county, "sector": sector}
            response = requests.post(f"{BACKEND_URL}/predictions/", json=payload)
            
            if response.status_code == 200:
                data = response.json()
                
                # Display Prediction Score
                st.success(f"Risk Score: {data.get('risk_score', 'N/A')}")
                
                # Display Gria AI Insights
                st.subheader("🤖 Gria AI Analysis")
                st.write(data.get("gria_summary", "No AI analysis available."))
            else:
                st.error("Failed to fetch prediction from backend server.")
                
        except Exception as e:
            st.error(f"Cannot connect to backend server. Make sure FastAPI is running. Error: {e}")
