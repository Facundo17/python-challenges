"""
Today we will build the following weather dashboard web app:

references/dashboard.png

Users can search for a city in the text box and the current weather information for that city will be displayed below the button:

references/dashboard2.png

You can use the Open Weather API to get current weather data. 
You need to sign up for a free account and get an API key. 
Then, build a Flask web app that makes API requests to 
the http://api.openweathermap.org/data/2.5/weather endpoint and display the received JSON data to the webpage.

Required Libraries: requests, flask
pip install flask requests
"""

import requests
from flask import Flask, render_template, request

# Replace with your OpenWeather API key
API_KEY = "37cd8e491fee1a570e67cbb4777c5526"

def get_weather(city):
    """Fetch weather data for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

#if __name__ == "__main__":
#    
#    city = input("Enter a city name: ")
#    weather_data = get_weather(city)
#    
#    if weather_data:
#        print(f"Weather in {city}:")
#        print(f"Temperature: {weather_data['main']['temp']}°C")
#        print(f"Weather: {weather_data['weather'][0]['description']}")
#    else:
#        print("Failed to retrieve temperature.")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    return "<p>Hello, World!</p>"