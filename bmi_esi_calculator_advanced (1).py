
import streamlit as st

# Define BMI multiplier function
def get_bmi_multiplier(bmi):
    if bmi < 18.5:
        return 0.85
    elif bmi <= 24.9:
        return 1.0
    else:
        return 1.43

# Define gender modifier
def gender_modifier(gender):
    return 1.1 if gender == "Female" else 1.0

# Define age modifier
def age_modifier(age):
    if age < 30:
        return 1.0
    elif age < 50:
        return 1.1
    else:
        return 1.25

# Define terrain modifier
def terrain_modifier(terrain):
    modifiers = {
        "Flat": 1.0,
        "Hilly": 1.2,
        "Mountainous": 1.4
    }
    return modifiers.get(terrain, 1.0)

# Base ESI values for NTFPs (from field ergonomic model)
base_esi = {
    "Bamboo": 8.80,
    "Rattan": 8.23,
    "Cinnamon": 5.87,
    "Star Anise": 3.67,
    "Pine Resin": 7.47,
    "Agarwood": 3.33,
    "Malva Nut": 3.00,
    "Bamboo Shoot": 3.00,
    "Wild Honey": 8.50
}

# Streamlit App
st.title("NTFP Ergonomic Stress Calculator (BMI, Gender, Age, Terrain)")
st.write("Estimate how physically stressful an NTFP load is based on your body and environmental factors")

# User inputs
bmi = st.slider("Enter your Body Mass Index (BMI):", 15.0, 35.0, 21.2)
gender = st.selectbox("Select your gender:", ["Male", "Female"])
age = st.slider("Enter your age:", 18, 70, 30)
terrain = st.selectbox("Select terrain type:", ["Flat", "Hilly", "Mountainous"])
ntfp_choice = st.selectbox("Select an NTFP you are collecting:", list(base_esi.keys()))

# Calculate adjusted ESI
bmi_mult = get_bmi_multiplier(bmi)
gender_mult = gender_modifier(gender)
age_mult = age_modifier(age)
terrain_mult = terrain_modifier(terrain)
base = base_esi[ntfp_choice]

adjusted_esi = round(base * bmi_mult * gender_mult * age_mult * terrain_mult, 2)

# Display results
st.markdown(f"### Result for {ntfp_choice}:")
st.write(f"**Your BMI**: {bmi} → Multiplier: {bmi_mult}")
st.write(f"**Gender**: {gender} → Multiplier: {gender_mult}")
st.write(f"**Age**: {age} → Multiplier: {age_mult}")
st.write(f"**Terrain**: {terrain} → Multiplier: {terrain_mult}")
st.write(f"**Base ESI**: {base}")
st.success(f"**Adjusted Ergonomic Stress Index (ESI): {adjusted_esi}**")
