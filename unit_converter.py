import streamlit as st     #streamlit is a library for building web apps


# Function to convert units based on predefined conversion factors or formulas
def convert_units(value ,unit_from, unit_to):

    conversions = {
        "meters_kilometers": 0.001,   # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,     # 1 kilometer = 1000 meter
        "grams_kilograms": 0.001,      # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000        # 1 kilogram 1000 gram
    }


    key = f"{unit_from}_{unit_to}"   # Generate a key based on the input and output units

    # logic to convert units
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"     #return a message if the conversion is not supported
    
st.title("Unit Converter")      #Set the Title of the web app

# User Input: numerical value to convert
value = st.number_input("Enter the Value:", min_value=1.0, step=1.0)


# Dropdown to select unit to convert from
unit_from = st.selectbox("Conver from:", ["meters", "kilometers", "grams", "kilograms"])

# dropdown to select unit to convert to
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Button to trigger the conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)   # Call the conversion function
    st.write(f"Converted value: {result}")              # Display the result














#---------------UNIT CONVERTER-----------------------------------
#Steps Follow-------------------------------------------------
#1. Users enters a value to convert
#2. User Selects unit (from & to)
#3. Click "Convert" button
#4. App Calculates the conversion, using a predefined fomula
#5. Result is displayed on the screen