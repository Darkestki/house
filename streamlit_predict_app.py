import streamlit as st
import pandas as pd
import joblib

# =============================
# 🎯 Page Config
# =============================
st.set_page_config(
    page_title="🏠 MEDV House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# =============================
# 🎉 Title Section
# =============================
st.title("🏠 Boston House Price Prediction App")
st.markdown("### 📊 Predict MEDV (Median House Value) using Machine Learning 🤖")

# =============================
# 📦 Load Model
# =============================
model = joblib.load("random_forest_regressor_model.joblib")

st.success("✅ Model Loaded Successfully!")

# =============================
# 🎛 Sidebar Inputs
# =============================
st.sidebar.header("⚙️ Enter House Features")

def user_input():

    CRIM = st.sidebar.slider("Crime Rate (CRIM) 🚔", 0.0, 100.0, 5.0)
    ZN = st.sidebar.slider("Residential Land (ZN) 🏘️", 0.0, 100.0, 10.0)
    INDUS = st.sidebar.slider("Industry Area (INDUS) 🏭", 0.0, 30.0, 10.0)
    CHAS = st.sidebar.selectbox("Near River? (CHAS) 🌊", [0, 1])
    NOX = st.sidebar.slider("Pollution (NOX) 🌫️", 0.0, 1.0, 0.5)
    RM = st.sidebar.slider("Rooms (RM) 🛏️", 1.0, 10.0, 5.0)
    AGE = st.sidebar.slider("Old Houses % (AGE) 🏚️", 0.0, 100.0, 50.0)
    DIS = st.sidebar.slider("Distance to Jobs (DIS) 🚗", 1.0, 15.0, 5.0)
    RAD = st.sidebar.slider("Highway Access (RAD) 🛣️", 1, 25, 5)
    TAX = st.sidebar.slider("Property Tax (TAX) 💰", 100, 800, 300)
    PTRATIO = st.sidebar.slider("Student-Teacher Ratio (PTRATIO) 🎓", 10.0, 30.0, 18.0)
    B = st.sidebar.slider("Black Population (B) 👥", 0.0, 400.0, 300.0)
    LSTAT = st.sidebar.slider("Low Income % (LSTAT) 📉", 0.0, 40.0, 10.0)

    data = {
        'CRIM':[CRIM], 'ZN':[ZN], 'INDUS':[INDUS], 'CHAS':[CHAS],
        'NOX':[NOX], 'RM':[RM], 'AGE':[AGE], 'DIS':[DIS],
        'RAD':[RAD], 'TAX':[TAX], 'PTRATIO':[PTRATIO], 'B':[B], 'LSTAT':[LSTAT]
    }

    return pd.DataFrame(data)


input_df = user_input()

# =============================
# 📋 Show Input Data
# =============================
st.subheader("📋 Your Input Data")
st.write(input_df)

# =============================
# 🔮 Prediction
# =============================
if st.button("🚀 Predict House Price"):

    prediction = model.predict(input_df)[0]

    st.balloons()

    st.success(f"🏆 Predicted MEDV Value: **${prediction:.2f} (in $1000s)** 💵")

    if prediction > 30:
        st.info("🌟 Luxury Area!")
    elif prediction > 20:
        st.info("😊 Medium Price Area")
    else:
        st.info("🏠 Budget Friendly Area")

# =============================
# Footer
# =============================
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit + Random Forest")
