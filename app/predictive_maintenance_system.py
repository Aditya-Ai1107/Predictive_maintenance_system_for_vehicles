import streamlit as st
import pandas as pd
import joblib
import json

st.set_page_config(
    page_title="Predictive Maintenance System for Vehicles",
    layout="wide"
)

# ---------------- MODEL LOAD ----------------
@st.cache_resource
def load_model():
    return joblib.load("vehicle_model.pkl")

model = load_model()

def sensor_gauge(label, value, min_val, max_val, status):

    progress = (value - min_val) / (max_val - min_val)

    st.write(f"**{label}: {value}**")

    if status == "Safe":
        st.progress(progress)

    elif status == "Warning":
        st.progress(progress)
        st.warning(f"{label} entering abnormal range")

    else:
        st.progress(progress)
        st.error(f"{label} in critical condition")

# ---------------- THRESHOLD DEFINITIONS ----------------
with open("thresholds.json") as f:
    THRESHOLDS = json.load(f)
with open("safe.json") as f:
    SAFE_THRESHOLDS = json.load(f)

with open("warning.json") as f:
    WARNING_THRESHOLDS = json.load(f)

with open("critical.json") as f:
    CRITICAL_THRESHOLDS = json.load(f)

# ---------------- SENSOR STATUS CHECK ----------------
def check_status(value, feature):

    safe_low, safe_high = SAFE_THRESHOLDS[feature]
    warn_low, warn_high = WARNING_THRESHOLDS[feature]
    crit_low, crit_high = CRITICAL_THRESHOLDS[feature]

    if crit_low <= value <= crit_high:
        return "Critical"

    elif warn_low <= value <= warn_high:
        return "Warning"

    elif safe_low <= value <= safe_high:
        return "Safe"

    else:
        return "Warning"

# ---------------- COLOR STATUS DISPLAY ----------------
def show_status(label, status):

    if status == "Safe":
        st.success(f"{label}: Safe")

    elif status == "Warning":
        st.warning(f"{label}: Warning")

    else:
        st.error(f"{label}: Critical")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🛠 Feature Thresholds")

for feature, ranges in THRESHOLDS.items():
    with st.sidebar.expander(feature.replace("_", " ").title()):
        st.success(f"Safe: {ranges['safe']}")
        st.warning(f"Warning: {ranges['warning']}")
        st.error(f"Critical: {ranges['critical']}")

# ---------------- MAIN UI ----------------
st.title("Predictive Maintenance System For Vehicles")

st.markdown(
    """
    **This system predicts vehicle failure risk using machine learning.**  
    You can manually tune parameters or let the system auto-configure a ***Safe, Warning and Critical*** risk state.
    """
)

# ---------------- AUTO PRESET BUTTONS ----------------
col_safe, col_warn, col_crit = st.columns(3)

with col_safe:
    if st.button("🟢 Set Vehicle to Safe (Normal) Condition (0 – 10% Risk)"):
        for key, value in SAFE_THRESHOLDS.items():
            st.session_state[key] = (value[0] + value[1]) / 2

with col_warn:
    if st.button("🟡 Set Vehicle to Warning Condition (10 – 40% Risk)"):
        for key, value in WARNING_THRESHOLDS.items():
            st.session_state[key] = (value[0] + value[1]) / 2

with col_crit:
    if st.button("🔴 Set Vehicle to Critical Condition (40 – 100% Risk)"):
        for key, value in CRITICAL_THRESHOLDS.items():
            st.session_state[key] = (value[0] + value[1]) / 2

# ---------------- INPUT PANEL ----------------
col1, col2, col3 = st.columns(3)

with col1:
    mileage = st.number_input("Mileage (0 km to 500000 kms)", 0, 500000, key="mileage")
    engine_temp = st.number_input("Engine Temperature (0°C to 150°C)", 0.0, 150.0, key="engine_temp")

with col2:
    oil_pressure = st.number_input("Oil Pressure (0 PSI to 100 PSI)", 0.0, 100.0, key="oil_pressure")
    vibration = st.number_input("Vibration Level (0 g to 1 g)", 0.0, 1.0, key="vibration")

with col3:
    brake_wear = st.number_input("Brake Wear (0 to 100 %)", 0.0, 100.0, key="brake_wear")
    rpm_variance = st.number_input("RPM Variance (0 to 500 RPM)", 0.0, 500.0, key="rpm_variance")


# ---------------- PREDICTION ----------------
st.markdown("---")

if st.button("🔍 Predict Failure Probability"):

    input_df = pd.DataFrame([{
        "mileage": mileage,
        "engine_temp": engine_temp,
        "oil_pressure": oil_pressure,
        "vibration": vibration,
        "brake_wear": brake_wear,
        "rpm_variance": rpm_variance,
    }])

    risk = model.predict_proba(input_df)[0, 1]

    st.metric("Predicted Failure Probability", f"{risk:.2%}")

    if risk <= 0.10:
        st.success("✅ Vehicle is in SAFE operating condition")

    elif risk <= 0.40:
        st.warning("⚠️ Moderate Risk — Maintenance Planning Suggested")

    else:
        st.error("❌ High Risk — Immediate Maintenance Required")

st.markdown("### 🔧 Sensor Health Monitoring Panel")

engine_status = check_status(engine_temp, "engine_temp")
oil_status = check_status(oil_pressure, "oil_pressure")
vibration_status = check_status(vibration, "vibration")
brake_status = check_status(brake_wear, "brake_wear")
rpm_status = check_status(rpm_variance, "rpm_variance")

col1, col2 = st.columns(2)

with col1:
    sensor_gauge("Engine Temperature (°C)", engine_temp, 0, 200, engine_status)
    show_status("Engine Temperature", engine_status)

    sensor_gauge("Oil Pressure (psi)", oil_pressure, 0, 100, oil_status)
    show_status("Oil Pressure", oil_status)

    sensor_gauge("Vibration (g)", vibration, 0, 1, vibration_status)
    show_status("Vibration", vibration_status)

with col2:
    sensor_gauge("Brake Wear (%)", brake_wear, 0, 100, brake_status)
    show_status("Brake Wear", brake_status)

    sensor_gauge("RPM Variance", rpm_variance, 0, 500, rpm_status)
    show_status("RPM Variance", rpm_status)

