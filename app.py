import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit App
def main():
    st.title("🌡️ Temperature Converter")
    st.write("Convert temperatures between Celsius and Fahrenheit with ease!")

    # User selects conversion direction
    option = st.radio(
        "Choose the conversion direction:",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
    )
    # User inputs temperature
    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", format="%.2f")
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
    
    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")

     # Add CSS style for customizing button color
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #28a745; /* Green color */
        color: white; /* White text color */
        border-radius: 8px; /* Optional: rounded corners */
        border: none; /* Remove border */
        padding: 0.5em 1em; /* Add some padding */
        font-size: 16px; /* Optional: adjust font size */
        cursor: pointer; /* Add pointer cursor on hover */
    }
    div.stButton > button:first-child:hover {
        background-color: #218838; /* Darker green on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)


if __name__ == "__main__":
    main()

