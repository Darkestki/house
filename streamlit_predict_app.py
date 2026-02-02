import streamlit as st
import pandas as pd
import joblib

# =================================
# 🎯 Page Setup
# =================================
st.set_page_config(page_title="🏠 MEDV Predictor", page_icon="🏠")

st.title("🏠 Boston House Price Prediction")
st.write("### 🤖 Random Forest MEDV Predictor with Streamlit")

# =================================
# 📦 Load Model
# =================================
model = joblib.load("random_forest_regressor_model.joblib")

st.success("✅ Model Loaded Successfully")

# =================================
# 🔑 IMPORTANT: Training column order
# (Boston dataset original order)
# =================================
FEATURES = [
    'CRIM','ZN','INDUS','CHAS','NOX','RM','AGE',
    'DIS','RAD','TAX','PTRATIO','B','LSTAT'
]

# =================================
# 🎛 Sidebar Inputs
# =================================
st.sidebar.header("⚙️ Enter House Details")

def get_user_input():

    data = {
        'CRIM': st.sidebar.slider("🚔 CRIM", 0.0, 100.0, 5.0),
        'ZN': st.sidebar.slider("🏘️ ZN", 0.0, 100.0, 10.0),
        'INDUS': st.sidebar.slider("🏭 INDUS", 0.0, 30.0, 10.0),
        'CHAS': st.sidebar.selectbox("🌊 CHAS", [0, 1]),
        'NOX': st.sidebar.slider("🌫️ NOX", 0.0, 1.0, 0.5),
        'RM': st.sidebar.slider("🛏️ RM", 1.0, 10.0, 5.0),
        'AGE': st.sidebar.slider("🏚️ AGE", 0.0, 100.0, 50.0),
        'DIS': st.sidebar.slider("🚗 DIS", 1.0, 15.0, 5.0),
        'RAD': st.sidebar.slider("🛣️ RAD", 1, 25, 5),
        'TAX': st.sidebar.slider("💰 TAX", 100, 800, 300),
        'PTRATIO': st.sidebar.slider("🎓 PTRATIO", 10.0, 30.0, 18.0),
        'B': st.sidebar.slider("👥 B", 0.0, 400.0, 300.0),
        'LSTAT': st.sidebar.slider("📉 LSTAT", 0.0, 40.0, 10.0)
    }

    df = pd.DataFrame([data])

    # ⭐⭐⭐ VERY IMPORTANT FIX ⭐⭐⭐
    # Force exact same column order
    df = df[FEATURES]

    return df


input_df = get_user_input()

# =================================
# 📋 Show Inputs
# =================================
st.subheader("📋 Input Data")
st.dataframe(input_df)

# =================================
# 🔮 Prediction
# =================================
if st.button("🚀 Predict Price"):

    try:
        prediction = model.predict(input_df)[0]

        st.balloons()

        st.success(f"🏆 Predicted MEDV = ${prediction:.2f} (in $1000s) 💵")

        if prediction > 30:
            st.info("🌟 Luxury Area")
        elif prediction > 20:
            st.info("😊 Medium Price Area")
        else:
            st.info("🏠 Budget Area")

    except Exception as e:
        st.error("❌ Feature mismatch with model.")
        st.write("Check column names or retrain model.")
        st.write(e)

# =================================
# Footer
# =================================
st.markdown("---")
st.write("Made with ❤️ Streamlit + Random Forest")
