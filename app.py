import streamlit as st
import time

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to simulate a weather effect (Snowflakes or others)
def snowflakes_effect():
    st.markdown(
        """
        <style>
        @keyframes snowflakes {
            0% {top: -10%;}
            100% {top: 100%;}
        }
        .snowflake {
            position: fixed;
            top: -10%;
            font-size: 1.5rem;
            color: white;
            z-index: 9999;
            animation: snowflakes 5s linear infinite;
        }
        .snowflake:nth-child(odd) {
            animation-duration: 6s;
        }
        .snowflake:nth-child(even) {
            animation-duration: 4s;
        }
        </style>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        <div class="snowflake">❄️</div>
        """,
        unsafe_allow_html=True
    )

# Streamlit App
def main():
    st.title("🌡️ Interactive Temperature Converter")
    st.write("Convert temperatures between **Celsius** and **Fahrenheit** effortlessly! 🔥❄️")

    # Initialize session state for inputs
    if "conversion_option" not in st.session_state:
        st.session_state.conversion_option = "Celsius to Fahrenheit"
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.0

    # Display dynamic image based on the conversion option
    if st.session_state.conversion_option == "Celsius to Fahrenheit":
        st.image("https://www.w3schools.com/w3images/snow.jpg", width=400)  # Snow image for Celsius to Fahrenheit
    elif st.session_state.conversion_option == "Fahrenheit to Celsius":
        st.image("https://www.w3schools.com/w3images/fog.jpg", width=400)  # Fog image for Fahrenheit to Celsius

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
            snowflakes_effect()  # Trigger snowflakes effect when result is shown
    
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
            snowflakes_effect()  # Trigger snowflakes effect when result is shown

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

if __name__ == "__main__":
    main()
