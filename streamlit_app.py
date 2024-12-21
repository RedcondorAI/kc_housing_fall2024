import streamlit as st
import requests
import json

# Streamlit app title
st.title("KC Housing Price Prediction App")

# Form inputs for prediction
st.header("Enter House Features")

grade = st.number_input("Grade", min_value=1, max_value=13, value=7)
sqft_living = st.number_input("Square Feet (Living Area)", min_value=500, max_value=10000, value=2000)
lat = st.number_input("Latitude", min_value=47.0, max_value=47.9, value=47.5)
long = st.number_input("Longitude", min_value=-122.5, max_value=-121.0, value=-122.2)
yr_built = st.number_input("Year Built", min_value=1900, max_value=2023, value=1990)
waterfront = st.selectbox("Waterfront (0: No, 1: Yes)", [0, 1])
sqft_living15 = st.number_input("Living Area of 15 Closest Homes (sqft)", min_value=500, max_value=10000, value=2000)
sqft_above = st.number_input("Square Feet (Above Ground)", min_value=500, max_value=10000, value=1500)
zipcode = st.number_input("Zipcode", min_value=98000, max_value=99999, value=98115)
sqft_lot = st.number_input("Lot Area (sqft)", min_value=500, max_value=1000000, value=5000)
# sqft_lot15 = st.number_input("Lot Area of 15 Closest Homes (sqft)", min_value=500, max_value=1000000, value=7000)
# bathrooms = st.number_input("Number of Bathrooms", min_value=0.0, max_value=10.0, value=2.0)
# view = st.number_input("View Rating (0-4)", min_value=0, max_value=4, value=0)
# id = st.number_input("ID", value=1)
# sqft_basement = st.number_input("Square Feet (Basement)", min_value=0, max_value=5000, value=500)
# bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
# condition = st.number_input("Condition Rating (1-5)", min_value=1, max_value=5, value=3)
# yr_renovated = st.number_input("Year Renovated (0 if never renovated)", min_value=0, max_value=2023, value=0)
# floors = st.number_input("Number of Floors", min_value=1.0, max_value=3.5, value=2.0)

# Submit button
if st.button("Predict Price"):
    # Prepare the payload
    payload = {
        "grade": grade,
        "sqft_living": sqft_living,
        "lat": lat,
        "long": long,
        "yr_built": yr_built,
        "waterfront": waterfront,
        "sqft_living15": sqft_living15,
        "sqft_above": sqft_above,
        "zipcode": zipcode,
        "sqft_lot": sqft_lot,
        # "sqft_lot15": sqft_lot15,
        # "bathrooms": bathrooms,
        # "view": view,
        # "id": id,
        # "sqft_basement": sqft_basement,
        # "bedrooms": bedrooms,
        # "condition": condition,
        # "yr_renovated": yr_renovated,
        # "floors": floors,
    }

    # API request
    try:
        response = requests.post("http://159.65.184.142:8002/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted House Price: ${result['prediction']:,.2f}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
