import streamlit as st
import pickle
import numpy as np
import os
st.write("🚀 App Started Successfully!")
st.title("✅ Streamlit Deployment Test")
st.write("If you see this, your app is working!")

# Get model file path
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model_pickle.pkl")

# Debugging: Check if file exists
if os.path.exists(MODEL_PATH):
    st.write(f"✅ Model file found at: {MODEL_PATH}")
else:
    st.error("❌ Model file NOT found! Check the file path.")

# Load the model
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    st.write("✅ Model Loaded Successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")


# Streamlit App
st.title("🎓 Placement Prediction App")

st.sidebar.header("Enter Student Details")

# User input fields
CGPA = st.sidebar.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
Internships = st.sidebar.number_input("Number of Internships", min_value=0, max_value=10, step=1)
Projects = st.sidebar.number_input("Number of Projects", min_value=0, max_value=10, step=1)
Workshops = st.sidebar.number_input("Workshops/Certifications", min_value=0, max_value=10, step=1)
AptitudeTestScore = st.sidebar.number_input("Aptitude Test Score", min_value=0, max_value=100, step=1)
SoftSkillsRating = st.sidebar.number_input("Soft Skills Rating", min_value=0.0, max_value=10.0, step=0.1)
SSC_Marks = st.sidebar.number_input("SSC Marks", min_value=0, max_value=100, step=1)
HSC_Marks = st.sidebar.number_input("HSC Marks", min_value=0, max_value=100, step=1)

# Derived features
Total_Marks = SSC_Marks + HSC_Marks
Experience = Internships + Projects

ExtracurricularActivities = st.sidebar.radio("Extracurricular Activities", ["Yes", "No"])
PlacementTraining = st.sidebar.radio("Placement Training", ["Yes", "No"])

# Convert Yes/No to 1/0
ExtracurricularActivities = 1 if ExtracurricularActivities == "Yes" else 0
PlacementTraining = 1 if PlacementTraining == "Yes" else 0

# Prediction
if st.sidebar.button("Predict Placement Status"):
    input_data = np.array([CGPA, Internships, Projects, Workshops, AptitudeTestScore,
                           SoftSkillsRating, SSC_Marks, HSC_Marks, Total_Marks, Experience,
                           ExtracurricularActivities, PlacementTraining]).reshape(1, -1)
    
    prediction = model.predict(input_data)
    result = "✅ Placed" if prediction[0] == 1 else "❌ Not Placed"
    
    st.success(f"📢 Prediction: **{result}**")
