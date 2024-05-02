import streamlit as st
import requests

st.title("Weather App")

city = st.text_input("Enter city name:")
fetch_button = st.button("Fetch Weather")

if fetch_button:
    api_key = "API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
            weather = data["weather"][0]["description"]
            st.write(f"Weather in {city}:")
            st.write(f"Temperature: {temperature:.1f}°C")
            st.write(f"Weather: {weather}")
        else:
            st.error(f"Error: {response.json()['message']}")
    except Exception as e:
        st.error("An error occurred:", e)
