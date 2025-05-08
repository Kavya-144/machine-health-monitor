import streamlit as st
import random
import time

def get_sensor_data():
    temperature = random.uniform(20, 80)
    vibration = random.uniform(0.2, 2.0)
    return temperature, vibration

def check_health(temp, vib):
    if temp > 70 or vib > 1.5:
        return "❌ Warning: High risk of failure!", "red"
    elif temp > 50 or vib > 1.0:
        return "⚠ Maintenance needed soon.", "orange"
    else:
        return "✅ Machine is healthy.", "green"

st.set_page_config(page_title="Machine Health Monitor", layout="centered")

st.title("🛠️ AI Co-Pilot - Machine Health Monitor")
st.write("Simulated readings of temperature and vibration...")

# Button to start simulation
if st.button("Start Monitoring"):
    for i in range(10):
        temp, vib = get_sensor_data()
        status, color = check_health(temp, vib)

        st.markdown(f"### Reading {i+1}")
        st.markdown(f"**Temperature:** `{temp:.2f}°C`")
        st.markdown(f"**Vibration:** `{vib:.2f}`")
        st.markdown(f"<span style='color:{color}; font-size:20px;'>{status}</span>", unsafe_allow_html=True)

        time.sleep(1)
        st.write("---")
