import streamlit as st
import random

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    st.title("Smart Home Control")

    # General on/off button
    general_status = st.button("General On")
    general_status_off = st.button("General Off")

    # Temperature control
    st.header("Temperature Control")
    temperature_status = st.button("Temperature On")
    temperature_status_off = st.button("Temperature Off")

    temperature_unit = st.radio("Select Temperature Unit", ["Celsius", "Fahrenheit"])
    min_temp = 28 if temperature_unit == "Celsius" else celsius_to_fahrenheit(28)
    max_temp = 40 if temperature_unit == "Celsius" else celsius_to_fahrenheit(40)

    temperature_value = st.number_input(f"Set Temperature ({temperature_unit})", min_value=float(min_temp), max_value=float(max_temp), step=1.0)

    # Camera control
    st.header("Camera Control")
    camera_status = st.button("Camera On")
    camera_status_off = st.button("Camera Off")

    # Light control
    st.header("Light Control")
    light_status = st.button("Light On")
    light_status_off = st.button("Light Off")

    # Display weight randomly
    st.header("Weight Display")
    weight_value = random.uniform(100, 300)
    st.write(f"Weight: {weight_value:.2f} pounds")

    # Show status based on button clicks
    st.write("\n**Status:**")
    st.write(f"- General: {'On' if general_status else 'Off'}")
    st.write(f"- Temperature: {'On' if temperature_status else 'Off'}")
    st.write(f"- Camera: {'On' if camera_status else 'Off'}")
    st.write(f"- Light: {'On' if light_status else 'Off'}")

if __name__ == "__main__":
    main()
