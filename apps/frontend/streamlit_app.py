import streamlit as st

st.set_page_config(
    page_title="AgriShield",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌾 AgriShield")
st.subheader("Protecting Kenya's Food Security, Ensuring Future Sustainability")

st.write(
    "AgriShield is an agricultural predictive intelligence system "
    "designed to help identify crop yield and livestock forage risks "
    "across Kenyan counties."
)

st.divider()

st.sidebar.header("⚙️ Risk Assessment")

county = st.sidebar.selectbox(
    "Select County",
    [
        "Uasin Gishu",
        "Kajiado",
        "Nairobi",
        "Mombasa",
        "Kisumu",
        "Nakuru"
    ]
)

focus = st.sidebar.selectbox(
    "Agricultural Focus",
    [
        "Crop",
        "Livestock Forage"
    ]
)

st.header("📊 Agricultural Risk Assessment")

col1, col2 = st.columns(2)

with col1:
    st.info(f"**Selected County:** {county}")

with col2:
    st.info(f"**Focus Area:** {focus}")


st.write("")

if st.button("🔍 Predict Agricultural Risk", use_container_width=True):

    st.success("Prediction request submitted!")

    st.metric(
        label="Risk Level",
        value="LOW"
    )

    st.metric(
        label="Yield Forecast",
        value="2,500 kg/ha"
    )

st.divider()

st.header("🤖 Gria AI Assistant")

st.write(
    "Ask Gria about agricultural risks, predictions, "
    "or recommendations for a selected county."
)

question = st.text_input(
    "Ask Gria a question",
    placeholder="e.g. What is causing the agricultural risk?"
)

if st.button("💬 Ask Gria"):

    if question:
        st.info("Gria response will appear here once the backend is connected.")
    else:
        st.warning("Please enter a question first.")

st.divider()

st.header("📄 Agricultural Risk Report")

st.write(
    "Generate a professional report containing the prediction, "
    "visualizations and Gria's recommendations."
)

st.button(
    "📥 Download PDF Report",
    disabled=True
)
