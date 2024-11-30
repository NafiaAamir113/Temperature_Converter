import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit App
def main():
    st.title("🌡️ Interactive Temperature Converter")
    st.write("Convert temperatures between **Celsius** and **Fahrenheit** effortlessly! 🔥❄️")

    # Sidebar for conversion options
    st.sidebar.header("Conversion Options")
    reset = st.sidebar.button("🔄 Reset")  # Reset button in sidebar
    if reset:
        st.session_state.clear()  # Clears all session state variables
    
    # Initialize session state for inputs
    if "conversion_option" not in st.session_state:
        st.session_state.conversion_option = "Celsius to Fahrenheit"
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.0

    st.session_state.conversion_option = st.sidebar.radio(
        "Choose the conversion direction:",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius"),
        index=0 if st.session_state.conversion_option == "Celsius to Fahrenheit" else 1,
    )

    # Temperature input and conversion
    if st.session_state.conversion_option == "Celsius to Fahrenheit":
        st.subheader("🌡️ Celsius to Fahrenheit Conversion")
        st.session_state.temperature = st.slider(
            "Select temperature in Celsius:",
            min_value=-100.0,
            max_value=100.0,
            value=st.session_state.temperature,
            step=0.1,
            help="Use the slider to select the Celsius temperature.",
        )
        if st.button("🌟 Convert to Fahrenheit"):
            fahrenheit = celsius_to_fahrenheit(st.session_state.temperature)
            st.success(f"✅ **{st.session_state.temperature}°C** is equal to **{fahrenheit:.2f}°F**.")
    elif st.session_state.conversion_option == "Fahrenheit to Celsius":
        st.subheader("🌡️ Fahrenheit to Celsius Conversion")
        st.session_state.temperature = st.slider(
            "Select temperature in Fahrenheit:",
            min_value=-148.0,
            max_value=212.0,
            value=st.session_state.temperature,
            step=0.1,
            help="Use the slider to select the Fahrenheit temperature.",
        )
        if st.button("🌟 Convert to Celsius"):
            celsius = fahrenheit_to_celsius(st.session_state.temperature)
            st.success(f"✅ **{st.session_state.temperature}°F** is equal to **{celsius:.2f}°C**.")

# Adding CSS style for customizing button hover effect
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: white; /* Normal button color */
        color: black; /* Normal text color */
        border: 2px solid #28a745; /* Green border */
        border-radius: 8px; /* Rounded corners */
        padding: 0.5em 1em; /* Add some padding */
        font-size: 16px; /* Adjust font size */
        cursor: pointer; /* Add pointer cursor on hover */
        transition: background-color 0.3s, color 0.3s; /* Smooth transition */
    }
    div.stButton > button:first-child:hover {
        background-color: #28a745; /* Green on hover */
        color: white; /* White text color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()
