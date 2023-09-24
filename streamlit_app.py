import streamlit as st
import requests

st.title("Space Satellite Coordinator")

st.image("images/Weather Satellite Images_ If the Earth Took a Selfie.jpeg", caption="Image 1", width=50)

# Function to get satellite info based on location
def get_satellite_info(location):
    latitude, longitude = map(float, location.split(","))
    api_key = "VVELHC-KKU8DP-Q7D92Q-54GM"

    url = f"https://api.n2yo.com/rest/v1/satellite/above/{latitude}/{longitude}/0/70/0/?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    return data

# Text input for user location
user_input_location = st.text_input("Enter any location to find the 10 closest satellites floating above it in space. (latitude, longitude) press Enter: ")

# Button to fetch satellite information based on user input
if st.button("Or find the 10 closest satellites using your current location"):
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        if "loc" in data:
            current_location = data["loc"]
            satellite_data = get_satellite_info(current_location)
            st.write("10 closest satellites above your current location:")
            for i, sat in enumerate(satellite_data['above']):
                if i >= 10:  # Display only the first 10 satellites
                    break
                st.write(f"Name: {sat['satname']}, Altitude: {sat['satalt']} km")
        else:
            st.error("Error fetching user location.")
    except Exception as e:
        st.error(f"Error fetching user location: {e}")

elif user_input_location:
    satellite_data = get_satellite_info(user_input_location)
    st.write(f"Satellites above the specified location ({user_input_location}):")
    for i, sat in enumerate(satellite_data['above']):
        if i >= 10:  # Display only the first 10 satellites
            break
        st.write(f"Name: {sat['satname']}, Altitude: {sat['satalt']} km")
