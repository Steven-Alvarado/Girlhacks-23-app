import streamlit as st
import requests
import streamlit.components.v1 as components
import codecs

st.title("Streamlit app")

# text input for user location
user_location = st.text_input("Enter your current location (latitude, longitude): ")

#button to fetch satellite information
if st.button("Get Satellite info"):
    pass

#get info function
def get_satellite_info(location):
    latitude, longitude = map(float, location.split(","))
    api_key = "VVELHC-KKU8DP-Q7D92Q-54GM"

    url = f"https://api.n2yo.com/rest/v1/satellite/above/{latitude}/{longitude}/0/70/0/?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    return data

if user_location:
    satellite_data 
    get_satellite_info(user_location)
    st.write("Satellites above your location:")
    for sat in satellite_data['above']:
        st.write(f"Name: {sat['satname']}, Altitude: {sat['satalt']} km")




def spacesite(main_html, width=700, height=1000):
    site_file = codecs.open(main_html, 'r')
    page = site_file.read()
    components.html(page, width=width, height=height, scrolling=True)

def main():
    """A Space App with Streamlit Components"""

    st.subheader("Space app")
    
    spacesite('/index.html')
 
   
 


if __name__ == '__main__':
	main()
    
    
    
    
    
##st.markdown(html_code, unsafe_allow_html=True)

