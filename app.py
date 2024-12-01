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

    # Initialize session state for inputs
    if "conversion_option" not in st.session_state:
        st.session_state.conversion_option = "Celsius to Fahrenheit"
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.0

    # Conversion direction
    st.session_state.conversion_option = st.radio(
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

    # Reset button below Convert button
    if st.button("🔄 Reset"):
        # Reset session state values for temperature and conversion option
        st.session_state.temperature = 0.0
        st.session_state.conversion_option = "Celsius to Fahrenheit"
        st.write("The app state has been reset.")

    # Footer Section
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center;">
            <p>Created with ❤️ by [Your Name]</p>
            <p>Check out the code on <a href="https://github.com/your-repo-url" target="_blank">GitHub</a></p>
            <p>For inquiries, please contact us at: <a href="mailto:contact@your-email.com">contact@your-email.com</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Adding CSS style for customizing button hover effect
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #f8f9fa; /* Light background by default */
        color: #495057; /* Dark text color */
        border: 2px solid #28a745; /* Green border */
        border-radius: 8px; /* Rounded corners */
        padding: 0.5em 1em; /* Add some padding */
        font-size: 16px; /* Adjust font size */
        cursor: pointer; /* Add pointer cursor on hover */
        transition: background-color 0.3s, color 0.3s; /* Smooth transition */
    }
    div.stButton > button:first-child:hover {
        background-color: #28a745; /* Green background on hover */
        color: white; /* White text color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()

